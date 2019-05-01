# Analysis of the usability and archival stability of omics computational tools

[![Preprint Available](https://img.shields.io/badge/Preprint-online-green.svg)](https://doi.org/10.1101/452532) [![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/smangul1/good.software/master)


This project contains the links to the datasets and the code that was used for our study : ["A comprehensive analysis of the usability and archival stability of omics computational tools and resources"](https://www.biorxiv.org/content/early/2018/10/25/452532)

**Table of contents**

* [How to cite this study](#how-to-cite-this-study)
* [Datasets](#datasets)
  * [Archival stability](#archival-stability)
  * [Usability](#usability)
* [Reproducing results](#reproducing-results)
* [License](#license)
* [Contact](#contact)


# How to cite this study

> Mangul, Serghei, et al. "A comprehensive analysis of the usability and archival stability of omics computational tools and resources." bioRxiv, doi: https://doi.org/10.1101/452532


# Datasets

## Archival stability

[![Hosted on Figshare-DOI: 10.6084/m9.figshare.7738901](https://img.shields.io/badge/Hosted%20on%20Figshare-DOI:%2010.6084/m9.figshare.7738901-blue.svg)](https://doi.org/10.6084/m9.figshare.7738901)

We downloaded open access papers via PubMed from 10 systems and computational biology journals. Raw data in XML format is available [here](https://drive.google.com/drive/folders/1m-2I5qCJqEpYC26jFHSxuqJ-tLMHksFf). Our approach to extract software links from the downloaded papers and verify the archival stability of links is described in the Methods section of the [paper](https://www.biorxiv.org/content/early/2018/10/25/452532) and [Figure S1](https://github.com/smangul1/good.software/blob/master/Fig_S1.png).  Timeout links were manually [verified](https://github.com/smangul1/good.software/blob/master/manual.evaluation/manual.test.csv).

Links extracted from the abstracts and the body of the surveyed papers (n=48,393) are available in CSV format  [here](https://github.com/smangul1/good.software/blob/master/analysis/links.bulk.csv). The CVS file contains the following fields:
* The type of link. The links were classified as extracted from abstract or the body of the paper
* Name of the journal
* Year the paper was published
* URL
* HTTP status: 0-300 - success. 300-400 redirection. 400 - broken link. -1 - timeout.   See more details [here](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
* Binary flag to indicates if the link was present in one paper or was shared across multiple papers.

## Usability

[![Hosted on Figshare-DOI: 10.6084/m9.figshare.7738949](https://img.shields.io/badge/Hosted%20on%20Figshare-DOI:%2010.6084/m9.figshare.7738949-blue.svg)](https://doi.org/10.6084/m9.figshare.7738949)

We have randomly chosen 99 tools across various domains of computational biology. The methodology used to select tools and list of domains is presented in the Methods section of our [paper](https://www.biorxiv.org/content/early/2018/10/25/452532).

Information about the usability of 99 tools is presented in CSV format  [here](https://github.com/smangul1/good.software/blob/master/analysis/usability.99.tools.csv). The CVS file contains the following fields:
* tool ID
* Name of the package manager from which the tools was available, or "NA" if the tool was not available via a package manager
* Number of citations per year
* Number of commands executed during the installation process
* Number of commands suggested in the installation manual of the tool
* The proportion of undocumented commands (not specified in the manual)
* Binary flag to indicate if the tool passed automatic installation test. Tools that require no manual intervention are considered to pass automatics installation test.
* The total installation time
* Binary flag to indicate how easy was to install the software tool. We categorized a tool as ‘easy to install’ if it could be installed in 15 minutes or less; ‘complex installation’ if it required more than 15 minutes but was successfully installed before the two-hour limit; and ‘not installed’ if the tool could not be successfully installed within two hours
* Binary flag to indicate if the example dataset was provided

# Reproducing results

We have prepared Jupyter Notebooks that utilize the raw data described above to reproduce the results and figures presented in our [manuscript](https://www.biorxiv.org/content/early/2018/10/25/452532).

* [Figure 1 Jupyter Notebook](http://nbviewer.jupyter.org/github/smangul1/good.software/blob/master/analysis/Figure1.ipynb)
* [Figure 2 Jupyter Notebook](https://github.com/smangul1/good.software/blob/master/analysis/Figure2.ipynb)

For more information about reproducing the data collection process used in the archival stability section of our study, see the README.md file in the [download.parse.data/ directory](https://github.com/smangul1/good.software/blob/master/download.parse.data/README.md).

**Would you like to play with our data and code?** There is no need to download or install anything, we set this repository up compatible with Binder:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/smangul1/good.software/master)


# Further acknowledgements

We thank the input from our peer reviewers, as well as online commenters in social media, in suggesting making the figures colorblind  friendly. We acknowledge the following resources, which help us achieve the final result:
* Northwestern University's Knight Lab post on [Three tools to help you make colorblind-friendly graphics](https://knightlab.northwestern.edu/2016/07/18/three-tools-to-help-you-make-colorblind-friendly-graphics/).
* Somersalt18:24's article on [designing colorblind-friendly scientific figures](http://www.somersault1824.com/tips-for-designing-scientific-figures-for-color-blind-readers/).
* [Color Oracle](colororacle.org), which simulates different colorblind conditions.

# License

This repository is under MIT license. For more information, please read our [LICENSE.md](./LICENSE.md) file.


# Contact

Please do not hesitate to contact us (smangul@ucla.edu, thiago.mosqueiro@gmail.com, blekhman@umn.edu) if you have any comments, suggestions, or clarification requests regarding the study or if you would like to contribute to this resource.
