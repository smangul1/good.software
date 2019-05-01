# Archival stability pipeline

Multiple scripts were combined to collect and evaluate the data in the "archival stability" section of our study.

## Step 0: Download code

These instructions make several assumptions: first, that your analysis is being performed within the repository directories, and second, that the commands are being performed in a Linux-like shell (either Linux, OSX, or a Bash environment in Windows). To begin, download all the code by running:

```sh
git clone https://github.com/smangul1/good.software.git
cd good.software/download.parse.data
```

## Step 1: Download data

We used data pulled directly from PubMed Central for this part of the study. The entire open access dataset can be downloaded at **[ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/](ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/)**

The collections are organized by the first letter of the journal name; for example, running this command would download the data for all journals starting with `A` or `B`:

```sh
wget ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/non_comm_use.A-B.xml.tar.gz
```

Extracting the files from this archive will reveal a set of directories, one for each journal. Within each of these directories, there is an XML file for each article. We provide an example journal directory (compressed) at [download.parse.data/Nat_Methods.tar.gz](https://github.com/smangul1/good.software/blob/master/download.parse.data/Nat_Methods.tar.gz) and an example XML file at [download.parse.data/PMC2427163.nxml](https://github.com/smangul1/good.software/blob/master/download.parse.data/PMC2427163.nxml).

The example directory is for the journal _Nature Methods_, but we pulled data from the FTP repository above for 10 journals:

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

To complete this step download the data for whatever journals you want to evaluate, and place their directories directly within the `good.software/download.parse.data` directory. For example, if you only wanted to evaluate articles from the example, _Nature Methods_, your directory structure would look like this:

```
good.software/
    download.parse.data/
        Nat_Methods/
```

## Step 2: Extract links, perform initial checks

Once the journal directories are all organized, navigate to the `good.software/download.parse.data/` directory in your terminal and run the `getLinksStatus.py` script, which takes a single parameter: the name of a single journal. This parameter should match the name of the journal's directory. For example, to process the links for _Nature Methods_:

```sh
python getLinksStatus.py Nat_Methods
```

**IMPORTANT NOTE:** Though most of the steps in this process use Python 3, **the `getLinksStatus.py` script requires Python 2.**

Running this script for each journal you want to evaluate will put two files in the `download.parse.data/` directory: `abstractLinks.prepared.tsv` and `bodyLinks.prepared.tsv`.









```sh
cd raw.data.broken.links
./reproduce.sh  # Creates file at analysis/links.bulk.csv

```