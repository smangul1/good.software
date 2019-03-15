import requests
import requests_ftp
import re
import sys

def makereq(url, protocol):
  # Sends a request using the specified protocol and interprets
  # the response, returning either the HTTP/FTP status code or,
  # in the case of request errors such as timeouts, "-1"
  tosend = f'{protocol}://{url}'
  try:
    if protocol != 'ftp':
      r = requests.get(tosend, timeout=timeout, allow_redirects=False) # TODO: Maybe we SHOULD follow redirects?
    else:
      r = s.list(tosend, timeout=timeout)
  except requests.exceptions.Timeout:
    print(f'  {protocol}: Timeout')
    return -1
  except requests.exceptions.ConnectionError:
    print(f'  {protocol}: Probably DNS resolution failure')
    return -1
  except requests.exceptions.InvalidSchema as e:
    if protocol == 'ftp':
      print(f'  {protocol}: No connection adapter???')
    else:
      print(f'  {protocol}: WEIRD invalid schema: {e} ({type(e)})')
    return -1
  except Exception as e:
    print(f'  {protocol}: WEIRD: {e} ({type(e)})')
    return -1

  # if the request completed:
  print(f'  {protocol}: {r.status_code}')
  if r.status_code < 400:
    print(f'    Successful response!')
  elif protocol == 'ftp':
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

  with open(sys.argv[2], 'w') as httpfile, open(sys.argv[1], 'r') as fileWithLinks:
    skipFirstLine = fileWithLinks.readline() # skip header row

    httpfile.write('type,journal,id,year,link,code,flag.uniqueness,newtest,oldcode\n')

    linecount = 0
    for line in fileWithLinks:
      linecount += 1
      elements = line.split(',')
      code  = int(elements[5])

      # if it's not a code that we're reevaluating, just write
      # the existing data into the revised file:
      if code not in [-1, 405]:
        httpfile.write(','.join(elements))
        continue

      elements[6] = elements[6][0] # trim linebreak from last element
      # remove (valid) protocols from URLs
      url = re.sub('^https?://', '', elements[4])
      url = re.sub('^s?ftps?://', '', elements[4])

      print(f'{linecount} Testing {url}')
      ftpresult = -1
      httpresult = makereq(url, 'http')

      elements.append('http') # 'newtest' column
      elements.append(str(code)) # 'oldcode' column

      # if the http call isn't in our "success" category, try FTP:
      if httpresult < 200 or httpresult > 399:
        ftpresult = makereq(url, 'ftp')

      # If we made an FTP call that didn't time out, record that status,
      # otherwise use whatever the HTTP call returned:
      elements[5] = str(httpresult if ftpresult == -1 else ftpresult)
      elements[-2] = str('http' if ftpresult == -1 else 'ftp')
      # write the new entry to disk
      httpfile.write(f'{",".join(elements)}\n')
