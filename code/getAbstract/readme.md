
The entire open access data in XML can be downloaded at

> ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/

We download and extract the files: ```articles[something].txt.tar.gz.```

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

Download the example XML and all python scripts. Go inside ```getLinksStatus.py```, run the code to extract the software links in this paper. 

Description for the output is inside ```getLinksStatus.py```.
