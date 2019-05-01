
The entire open access data in XML can be downloaded at

> ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/

We download and extract the files: `[something].xml.tar.gz.` For example, you can download one set by using

```sh
wget ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/non_comm_use.A-B.xml.tar.gz
```

Then extract it
```sh
mkdir pubDataOpenAccXml
tar -xf non_comm_use.A-B.xml.tar.gz -C pubDataOpenAccXml/comm_use.A-B
```

To avoid having you downloading very large data, in this github, we provide an example for the journal Nature Methods `Nat_Methods`. You can use extract this zip folder `tar -xf Nat_Methods.tar.gz -C Nat_Methods`. You will see there are 505 open accessed papers.

We focus only on these journals

```
BMC_Genomics
Genet_Res
Genome_Med
Nat_Methods
PLoS_Comput_Biol
BMC_Bioinformatics
BMC_Syst_Biol
Genome_Biol
Nat_Biotechnol
Nucleic_Acids_Res
```



Do the following in the terminal, to download the example XML and all python scripts and run the example. (**NOTE: This example requires Python 2.**)

```sh
git clone https://github.com/smangul1/good.software.git
cd good.software/getAbstract
python getLinksStatus.py
```

We focus on the follow groups of HTTP status:
```
-1: Connection Timeout
200-299: working link
300-399: redirected link
400 and over: broken link
```

To run the code over many xml files, you can follow the code below. This is an example for the folder `Nat_Methods`. 

```
from urllib2 import HTTPError
import xml.etree.ElementTree
import os,re,sys
import argparse
import httplib
from urlparse import urlparse
from urlXmlUtil import * 

## go inside the Nat_Methods folder, and get the file list 
all_xml = os.listdir('your/path/to/folder/Nat_Methods')
output_abstract = open("abstract_link_status.txt","w")
output_body = open("body_link_status.txt","w")
for paperName in all_xml: 
  output_abstract.write( getHttpStatus(paperName,'abstract') + "\n" ) 
  output_body.write( getHttpStatus(paperName,'body') + "\n" )
 
output_abstract.close() 
output_body.close() 
```

