## make a .sh script to auto download files. 

import re
fin = open ("/u/flashscratch/d/datduong/pubmedAbstractBaseLineYearly/index.html",'r')
script = "" 
for line in fin: 
  path = re.findall("href=.+\"",line)
  if len(path)==0:
    continue
  path = re.sub ( "href=\"","",path[0] )
  path = re.sub ( "\"","",path )
  if "gz.md5" in path: 
    continue
  script = script + "wget " + path + " -P /u/flashscratch/d/datduong/pubmedAbstractBaseLineYearly/baseline \n"

fout = open ("/u/flashscratch/d/datduong/pubmedAbstractBaseLineYearly/download.sh",'w')
fout.write(script)
fout.close() 
