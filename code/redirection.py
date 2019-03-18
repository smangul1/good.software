from urllib.request import urlopen
import urllib
import re

def http2httpsRedirectionCheck(URL):
    """
    Checks if the server is redirecting from HTTP to HTTPS, or
    HTTPS to HTTP. If that's the case, True is returned.

    If there is no redirection, this function will also return true.
    """

    try:
        page = urlopen(URL, timeout=10)
    except TimeoutError:
        return -1
    except urllib.error.URLError as e:
        print(e)
        return -1
    except:
        return -2 # sys.exc_info()[0]

    if page.url != URL :
        print(f'  Redirected to new URL: {page.url}')
        # Evaluates the address without protocol
        finalPageAddress_noProt = (page.url).split( '://' )[1]
        orignlURLAddress_noProt = URL.split( '://' )[1]
        return finalPageAddress_noProt == orignlURLAddress_noProt

    else:
        # No redirection, returns True anyway
        return True

# fileWithLinks = open('../download.parse.data/retry_http.csv', 'r')
fileWithLinks = open('../download.parse.data/newdata/revised_links.bulk.csv', 'r')
skipFirstLine = fileWithLinks.readline() # skip header row

outfile = open('../download.parse.data/newdata/revised_http2https.redirected.csv', 'w', 1)

checked = 0
for line in fileWithLinks:
    pid   = line.split(',')[2]
    url   = line.split(',')[4]
    code  = int(line.split(',')[5])

    if ( code >= 300 ) and ( code < 400 ):
        checked += 1
        print(f'checking: {checked}\n  {url}')

        url = re.sub('^https?://', '', url)
        url = re.sub('^s?ftps?://', '', url)
        url = 'http://' + url

        outfile.write( pid + ',' + url + ',' + str(code) + ',' )
        outfile.write( str(http2httpsRedirectionCheck( url )) )
        outfile.write('\n')

outfile.close()
