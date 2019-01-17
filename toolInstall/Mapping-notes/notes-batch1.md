# HTS mappers - Batch 1

Tools chosen in this batch:

* [bowtie 2](./notes-batch1.md#mt1-bowtie-2)
* [NextGenMap](./notes-batch1.md#mt2-nextgenmap)
* [Erne](./notes-batch1.md#mt3-erne)
* [Mummer](./notes-batch1.md#mt4-mummer)
* [SOAP 2](./notes-batch1.md#mt5-soap2)
* [SHRiMP](./notes-batch1.md#mt6-shrimp)
* [mrFast](./notes-batch1.md#mt7-mrfast)
* [seqMap](./notes-batch1.md#mt8-seqmap)
* [CRAC](./notes-batch1.md#mt9-crac)
* Zoom (discarded!)
* [HISAT2](./notes-batch1.md#mj10-HISAT2)

<br />

## mt1: bowtie 2

**URL:** http://bowtie-bio.sourceforge.net/bowtie2/index.shtml

**Version tested:** 2.2.4

**How to find a list of releases?**<br />
http://bowtie-bio.sourceforge.net/bowtie2/news.shtml<br />
(ctfl F - Version 2.)

**Github?** Yes<br />
https://github.com/BenLangmead/bowtie2

**Package manager?** Yes<br />
http://bioconda.github.io/recipes/bowtie2/README.html

Commands:
```
./anaconda3/bin/conda config --add channels bioconda
./anaconda3/bin/conda install bowtie2
```

**Correctly installed?** Yes

Commands:
```
# Indexing a reference genome
XXXXX --- lost this command
bowtie2 -x lambda_virus_test -U reads_1.fq -S eg1.sam
```



## mt2: Nextgenmap

**URL:** http://cibiv.github.io/NextGenMap/

**Version tested:** 0.5.2

**How to find a list of releases?**<br />
Had to combine:<br />
https://github.com/Cibiv/NextGenMap/wiki/Changelog-(old)<br />
https://github.com/Cibiv/NextGenMap/releases

**Github?**  Yes

**Package manager?** Yes<br />
https://bioconda.github.io/recipes/nextgenmap/README.html

Commands:
```
sh Anaconda3-5.0.1-Linux-x86_64.sh
./anaconda3/bin/conda config --add channels conda-forge
./anaconda3/bin/conda config --add channels defaults
./anaconda3/bin/conda config --add channels r
./anaconda3/bin/conda config --add channels bioconda
./anaconda3/bin/conda install nextgenmap
```

**Correctly installed?** Yes

Commands:
```
wget https://raw.githubusercontent.com/BenLangmead/bowtie2/master/example/reference/lambda_virus.fa
wget https://github.com/BenLangmead/bowtie2/raw/master/example/reads/reads_1.fq
./ngm -q reads_1.fq -r lambda_virus.fa -o eg1.sam -t 4
```



## mt3: Erne

**URL:** http://erne.sourceforge.net/

**Version tested:** 2.1.1

**How to find a list of releases?**<br />
https://sourceforge.net/projects/erne/files/

**Github?** No

**Package manager?** Yes<br />

Commands:
```
./anaconda3/bin/conda config --add channels bioconda
./anaconda3/bin/conda install erne
```

**Correctly installed?** Yes

Commands:
```
erne-create --output lambda --fasta lambda_virus.fa
erne-map --reference lambda.ebh --query1 reads_1.fq --output eg1.bam
```



## mt4: Mummer

**URL:** http://mummer.sourceforge.net/

**Version tested:** 2.23

**How to find a list of releases?**<br />
https://sourceforge.net/projects/mummer/files/mummer/

**Github?** No

**Package manager?** Yes<br />
https://bioconda.github.io/recipes/mummer/README.html

Commands:
```
./anaconda3/bin/conda config --add channels bioconda
./anaconda3/bin/conda install mummer
```

**Correctly installed?** Yes

Commands:
```
mummer lambda_virus.fa reads_1.fq
```



## mt5: SOAP2

**URL:** http://soap.genomics.org.cn/soapaligner.html

**Version tested:**

* How to find a list of releases?< br/>
Home page.

**Github?** No

**Package manager?** Yes<br />
https://anaconda.org/biobuilds/soapaligner

Commands:
```
conda install -c biobuilds soapaligner
```


**Correctly installed?** Yes

Commands:
```
2bwt-builder lambda_virus.fa
soap -a reads_1.fq -D lambda_virus.fa.index -o test
```


## mt6: SHRiMP

**URL:** http://compbio.cs.toronto.edu/shrimp/

**Version tested:**

* How to find a list of releases?

**Github?** No

**Package manager?** Yes<br />
https://anaconda.org/biobuilds/shrimp

Commands:
```
conda install -c biobuilds shrimp
```


**Correctly installed?** Yes

Commands:
```
gmapper-cs reads_1.fq lambda_virus.fa \-N 4 -o 5 -h 80% >map.out 2>map.log
```



## mt7: mrFast

**URL:** http://mrfast.sourceforge.net/

**Version tested:**

**How to find a list of releases?**<br />
Only have available releases in 2.?: http://mrfast.sourceforge.net/

**Github?**  No

**Package manager?** Yes<br />
https://anaconda.org/biobuilds/mrfast

Commands:
```
conda install -c biobuilds mrfast
```


**Correctly installed?** Yes

Commands:
```
mrfast --index lambda_virus.fa
mrfast --search lambda_virus.fa --seq reads_1.fq -o map.out
```


## mt8: seqMAP

**URL:** http://www-personal.umich.edu/~jianghui/seqmap/index.html

**Version tested:**

**How to find a list of releases?**<br />
Looked into the most recent HISTORY file

**Github?**  No

* Package manager? No

* Source available? Yes

Commands:
```
sudo yum install unzip gcc-c++ -y
wget http://www-personal.umich.edu/~jianghui/seqmap/download/seqmap-1.0.13-src.zip
make seqmap
```

**Correctly installed?** Yes

Commands:
```
/seqmap 2 lambda_virus.fa test.fa output.txt
```


## mt9: CRAC

**URL:** http://crac.gforge.inria.fr/

**Version tested:** 2.5.0

* How to find a list of releases?
https://gforge.inria.fr/frs/?group_id=3008&release_id=9605

**Github?**  No

* Package manager? Yes, but failed (required HTS)

Commands:
```
wget https://gforge.inria.fr/frs/download.php/file/35497/crac-2.5.0-1.x86_64.rpm
sudo yum install crac-2.5.0-1.x86_64.rpm -y
```

This returns the following error:
```
--> Finished Dependency Resolution
Error: Package: crac-2.5.0-1.x86_64 (/crac-2.5.0-1.x86_64)
           Requires: libhts.so.1()(64bit)
```


* Available through source? Yes

```
wget https://gforge.inria.fr/frs/download.php/file/35495/crac-2.5.0.tar.gz
tar -xvzf crac-2.5.0.tar.gz
cd crac-2.5.0/
./configure

## Both of the installs below are necessary
sudo yum groupinstall "Development Tools"
sudo yum install zlib-devel


## Let's try from source
sudo yum install bzip2-devel xz-devel
# the following ones are not NECESSARY
sudo yum install libcurl-devel openssl-devel
wget https://github.com/samtools/htslib/releases/download/1.6/htslib-1.6.tar.bz2
tar -vxjf htslib-1.6.tar.bz2
cd htslib-1.6/
./configure
make
sudo make install

## HTS must be installed from the source!!

## Going back to CRAC
cd ../crac-2.5.0
./configure
make
make check  # error -- can't load libhts.so.2

# it's not on LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib

make check          # IT SHOULD PASS

sudo make install
make installcheck   # IT SHOULD PASS
```

_Installation note:_ you NEED to install HTS from the source (I'll try with LD_LIBRARY_PATH later.....). If you install it from BioConda, CRAC will not find htslib.so.(1/2). This is how I did it:
```
## it also requires htslib (https://anaconda.org/bioconda/htslib)
wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
sh Anaconda3-5.0.1-Linux-x86_64.sh
conda install -c bioconda htslib
./configure
```


**Correctly installed?** Yes

Commands:
```
crac-index index LambdaVirus lambda_virus.fa
crac -i LambdaVirus -k 22 -r reads_1.fq -o reads.bam
```


## mj10: HISAT2

**URL:** http://ccb.jhu.edu/software/hisat2/index.shtml

**Version tested:** 2.1.0

**How to find a list of releases?**<br />
ftp://ftp.ccb.jhu.edu/pub/infphilo/hisat2/downloads/<br />


**Github?** Yes<br />
https://github.com/infphilo/hisat2

**Package manager?** Yes<br />
https://anaconda.org/bioconda/hisat2

Commands:
```
./anaconda3/bin/conda install -c bioconda hisat2
./anaconda3/bin/conda info hisat2
./anaconda3/bin/conda install python=3.5
./anaconda3/bin/conda install -c bioconda hisat2
sudo yum install perl -y
```

**Correctly installed?** Yes

Commands:
```
# Indexing a reference genome
./anaconda3/bin/hisat2-build lambda_virus.fa lambda_index
./anaconda3/bin/hisat2 -x lambda_index -U reads_1.fq -S test.sam
```
