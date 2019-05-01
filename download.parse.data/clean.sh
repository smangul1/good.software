#Body
awk '{if(NF<50) {for(i=1;i<=NF;i++) {printf "%s,", $i}; printf "\n"}}' bodyLinks.prepared.tsv | grep -v "$^" >bodyLinks.prepared.clean.csv

#Abstract
awk '{if(NF<50) {for(i=1;i<=NF;i++) {printf "%s,", $i}; printf "\n"}}' abstractLinks.prepared.tsv | grep -v "^$" >abstractLinks.prepared.clean.csv

# Prepare final file

python prepare.data.py abstractLinks.prepared.clean.csv bodyLinks.prepared.clean.csv links.unchecked.csv
