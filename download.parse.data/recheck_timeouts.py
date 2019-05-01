import requests
import requests_ftp
import re
import sys
import urllib3

urllib3.disable_warnings()
# NOTE: urllib warnings are disabled because https certificate validation is disabled.
# In general, this is not a secure practice; see more here: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
# It was disabled here because of request failures caused by certificate-related errors
# that are encountered by automated scripts but not web users.

def makereq(url, protocol, timeout=10, allow_redirects=False):
  # Sends a request using the specified protocol and interprets
  # the response, returning either the HTTP/FTP status code or,
  # in the case of request errors such as timeouts, "-1"
  tosend = f'{protocol}://{url}'
  try:
    if protocol != 'ftp':
      # NOTE: To avoid annoying quirks with SSL cert validation, this doesn't check whether
      # the certs are valid.
      r = requests.get(tosend, timeout=timeout, verify=False, stream=True, allow_redirects=allow_redirects)
    else:
      r = s.list(tosend, timeout=timeout)
  except requests.exceptions.Timeout:
    print(f'  {protocol}: Timeout')
    return -1
  except requests.exceptions.ConnectionError as e:
    print(f'  {protocol}: Connection error: {e}')
    return -1
  except Exception as e:
    print(f'  {protocol}: WEIRD: {e} ({type(e)})')
    return -1

  # if the request completed:
  print(f'  {protocol}: {r.status_code}')

  # If the request got a redirect response, follow the redirection to make
  # sure the destination actually works:
  if protocol == 'http' and r.status_code in range(300,400) and not allow_redirects:
    print(f'  {protocol}: Following redirects...')
    new = makereq(url, protocol, timeout, True)
    if new != 200: # TODO: Check why 200+ successful calls were recorded as 200s and not 301s
      print(f'  {protocol}: Broken redirect: Saving redirected status code {new}')
      return new

  if protocol == 'ftp' and r.status_code > 399:
    # if the URL is to a file instead of a directory:
    print(f'  {protocol}: Trying SIZE instead of LIST')
    r = s.size(tosend,timeout=timeout)
    print(f'  {protocol}: {r.status_code}')
  return r.status_code

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print("Script expects two command-line arguments: source file and output file.")
    print("Example: `python recheck_timeouts.py ../analysis/links.bulk.csv output_new.csv`")
    exit(1)

  # Drag in the ftp adapter for the "requests" module:
  requests_ftp.monkeypatch_session()
  s = requests.Session()
  # set a timeout that can be used for all the requests:
  timeout = 10

  with open(sys.argv[2], 'w', 1) as httpfile, open(sys.argv[1], 'r') as fileWithLinks:
    skipFirstLine = fileWithLinks.readline() # skip header row

    httpfile.write('type,journal,id,year,link,code,flag.uniqueness,oldcode,newlink\n')

    linecount = 0
    for line in fileWithLinks:
      linecount += 1
      elements = line.split(',')
      code  = int(elements[5])

      # NOTE: This is where you can set which responses you want to double-check.
      # Any entry for which this conditional returns True will get skipped.
      if code not in range(300,400):
        httpfile.write(','.join(elements))
        continue

      elements[6] = elements[6][0] # trim linebreak from last element
      elements.append(elements[5]) # save value in 'oldcode' column

      # remove (valid) protocols from URLs
      url = re.sub('^https?://', '', elements[4])
      url = re.sub('^s?ftps?://', '', url)

      print(f'{linecount} Testing {url}')
      ftpresult = -1
      httpresult = makereq(url, 'http', timeout)

      # if the http call isn't in our "success" category, try FTP:
      if httpresult < 200 or httpresult > 399:
        ftpresult = makereq(url, 'ftp', timeout)

      # If we made an FTP call that didn't time out, record that status,
      # otherwise use whatever the HTTP call returned:
      elements[5] = str(httpresult if ftpresult == -1 else ftpresult)
      elements.append(str('http' if ftpresult == -1 else 'ftp'))
      # write the new entry to disk
      httpfile.write(f'{",".join(elements)}\n')
