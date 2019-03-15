import requests
import requests_ftp
import re

requests_ftp.monkeypatch_session()
s = requests.Session()
timeout = 10

def makereq(url, protocol):
  tosend = f'{protocol}://{url}'

  try:
    if protocol != 'ftp':
      r = requests.get(tosend, timeout=timeout, allow_redirects=False) # TODO: Maybe we SHOULD follow redirects?
    else:
      r = s.list(tosend, timeout=timeout)
  except requests.exceptions.Timeout:
    print(f'  {protocol}: Timeout')
    return -1
  # except requests.exceptions.SSLError as e:
  #   if protocol != 'https':
  #     print(f'  {protocol}: SSL certificate error')
  #     return makereq(url, 'https')
  #   else:
  #     print(f'  {protocol}: {e}')
  #     return -1
  except requests.exceptions.ConnectionError:
    print(f'  {protocol}: Probably DNS resolution failure')
    return -1
  except requests.exceptions.InvalidSchema as e:
    if protocol == 'ftp':
      print(f'  {protocol}: No connection adapter???')
      return -1
    else:
      print(f'  {protocol}: WEIRD invalid schema: {e} ({type(e)})')
  except Exception as e:
    print(f'  {protocol}: WEIRD: {e} ({type(e)})')
    return -1

  print(f'  {protocol}: {r.status_code}')
  if r.status_code < 400:
    print(f'***\n  ***{protocol}: Successful response: {r.status_code}\n***\n')
    if r.status_code == 226:
      print('\n\n\n\nFTP?!?!?!\n\n!!!!\n\n\n')
  elif protocol == 'ftp':
    print(f'  {protocol}: Trying RETR instead of LIST')
    r = s.retr(tosend,timeout=timeout)
    if r.status_code == 226:
      print('\n\n\n\nFTP?!?!?!\n\n!!!!\n\n\n')
    print(f'  {protocol}: {r.status_code}')
  return r.status_code

fileWithLinks = open('../analysis/links.bulk.csv', 'r')
skipFirstLine = fileWithLinks.readline()

httpfile = open('retry_http.csv', 'w', 1)
httpfile.write('type,journal,id,year,link,code,flag.uniqueness,newtest,oldcode\n')
TO_SKIP = 0
linecount = 0
for line in fileWithLinks:
  linecount += 1
  if linecount < TO_SKIP:
    continue
  elements = line.split(',')
  code  = int(elements[5])

  if code not in [-1, 405]:
    httpfile.write(','.join(elements))
    continue

  elements[6] = elements[6][0] # trim linebreak from last element
  url = re.sub('^https?://', '', elements[4])

  print(f'{linecount} Testing {url}')
  ftpresult = -1
  httpresult = makereq(url, 'http')

  elements.append('http')
  elements.append(str(code))
  if httpresult < 200 or httpresult > 399:
    ftpresult = makereq(url, 'ftp')
  elements[5] = str(httpresult if ftpresult == -1 else ftpresult)
  elements[-2] = str('http' if ftpresult == -1 else 'ftp')
  httpfile.write(f'{",".join(elements)}\n')
httpfile.close()