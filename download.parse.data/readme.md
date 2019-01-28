
The entire open access data in XML can be downloaded at

> ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/

We download and extract the files: ```[something].xml.tar.gz.``` For example, you can download one set by using 

```
wget ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/non_comm_use.A-B.xml.tar.gz
```

Then extract it
```
mkdir pubDataOpenAccXml
tar -xf non_comm_use.A-B.xml.tar.gz -C pubDataOpenAccXml/comm_use.A-B
```

To avoid having you downloading very large data, in this github, we provide an example for the journal Nature Methods ```Nat_Methods```. You can use extract this zip folder ```tar -xf Nat_Methods.tar.gz -C Nat_Methods```. You will see there are 505 open accessed papers. 

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

As an example, consider the paper ```PMC2427163.nxml``` (included here). This file is in XML format. 

Download the example XML and all python scripts. Go inside ```getLinksStatus.py```, run the code to extract the software links in this paper. Do the following in the terminal 

```git clone https://github.com/datduong/archival-stability-of-computational-biology-software.git
cd archival-stability-of-computational-biology-software/getAbstract
```

Go inside open the file ```getLinksStatus.py```, and copy paste its code: 

```from urllib2 import HTTPError
import xml.etree.ElementTree
import os,re,sys
import argparse
import httplib
from urlparse import urlparse
from urlXmlUtil import * 
  
paperName = "PMC2427163.nxml" 
getHttpStatus(paperName,'abstract') ## get http links in abstract
## you will see the output 
## '18463117 2008 tool www.oboedit.org -1 null http://compbio.uchsc.edu/Hunter_lab/Bada/nonalignments_2008_03_06.html -1 '
## 18463117 is the Pubmed Id number for this paper. 
## 2008 is the year of this paper. 
## www.oboedit.org is the 1st link found in the abstract, and the HTTP status is -1. 
## http://compbio.uchsc.edu/Hunter_lab/Bada/nonalignments_2008_03_06.html is the 2nd link found in the abstract and the HTTP status is -1

## To get the links inside the body of the paper, paste next line of code: 

getHttpStatus(paperName,'body')

```

We focus on the follow groups of HTTP status: 
```
-1 is Connection Timeout 
200-299: working link
300-399: redirected link 
400 and over: broken link
```

