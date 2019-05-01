from urllib2 import HTTPError
import xml.etree.ElementTree
import os,re,sys
import argparse
import httplib
from urlparse import urlparse
from urlXmlUtil import *

## go inside the Nat_Methods folder, and get the file list
if len(sys.argv) < 2:
  print 'Journal directory name required as first parameter.'
  exit(1)

journal = sys.argv[1]
dir_location = journal + '/'
all_xml = os.listdir(dir_location)
output_abstract = open("abstractLinks.prepared.tsv","a")
output_body = open(dir_location + "bodyLinks.prepared.tsv","a")
for paperName in all_xml:
  paperName = dir_location + paperName
  output_abstract.write( getHttpStatus(paperName,'abstract',journal) + "\n" )
  output_body.write( getHttpStatus(paperName,'body',journal) + "\n" )

output_abstract.close()
output_body.close()

## see output in the format

## PubmedId, Year, KeyWord related to link, Link, LinkStatus, StatusCode.
## 18463117 2008 tool www.oboedit.org -1 null http://compbio.uchsc.edu/Hunter_lab/Bada/nonalignments_2008_03_06.html -1

## KeyWords are:
# "here", "pipeline", "code", "software", "available", "publicly", "tool", "method", "algorithm", "download", "application", "apply", "package", "library"

## Status code:
# -1: Connection Timeout
# 200-299: working link
# 300-399: redirected link
# 400 and over: broken link
