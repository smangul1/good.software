from urllib2 import HTTPError
import xml.etree.ElementTree
import os,re,sys
import argparse
import httplib
from urlparse import urlparse
from urlXmlUtil import * 
  
paperName = "PMC2427163.nxml" 
getHttpStatus(paperName,'abstract') ## get http links in abstract
getHttpStatus(paperName,'body') ## get http links in body

## see outpt in the format

## PubmedId, Year, KeyWord related to link, Link, LinkStatus, StatusCode. 
## 18463117 2008 tool www.oboedit.org -1 null http://compbio.uchsc.edu/Hunter_lab/Bada/nonalignments_2008_03_06.html -1

## KeyWords are: 
# "here", "pipeline", "code", "software", "available", "publicly", "tool", "method", "algorithm", "download", "application", "apply", "package", "library" 

## Status code: 
# -1 is Connection Timeout 
# 200-299: working link
# 300-399: redirected link 
# 400 and over: broken link
