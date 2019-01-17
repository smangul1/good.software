# HTS mappers - Notes

Here we will log all relevant information to reproduce the installation tests for HTS mappers.

* List of HTS mappers: [https://www.ebi.ac.uk/~nf/hts_mappers/#features](https://www.ebi.ac.uk/~nf/hts_mappers/#features)

| Open source | Binaries only | Commercial license |
|---|---|---|
| 85.7% | 3.1% | 11.2% |



### Batches of experiments

* [Batch 1](./notes-batch1.md) - 10 tools randomly chosen (Dec 15, 2017)

* Batch 2 - 20 tools chosen to increase our sample size (...)


### Fresh install of CentOS 7

Each software was tested with a completely clean system:
```
vagrant destroy && vagrant up
vagrant ssh
sudo yum update -y
sudo yum install wget -y
```

Whenever the package was available through Anaconda, we installed Anaconda using the following commands:
```
wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
sh Anaconda3-5.0.1-Linux-x86_64.sh
```


### Testing pipeline

To test whether the tools were succesfully installed, we used the Lambda Phage genome. To obtain the necessary files, simply run:
```
# Reference genome
wget https://raw.githubusercontent.com/BenLangmead/bowtie2/master/example/reference/lambda_virus.fa
# Example of reads for test alignment
wget https://github.com/BenLangmead/bowtie2/raw/master/example/reads/reads_1.fq

```
