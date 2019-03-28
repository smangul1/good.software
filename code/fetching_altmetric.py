from altmetric import Altmetric
import os, os.path

# importing body links
setLinks = open('../analysis/links.bulk.csv', 'r')

numLines2Skip = 4500

# altmetric
outputFileName = '../analysis/links.bulk.altmetric.csv'
listpmid_alreadyDone = []

s = ','  # separator

if os.path.isfile(outputFileName):
    outputFile_r = open(outputFileName, 'r')
    for line in outputFile_r:
        listpmid_alreadyDone.append( line.split(',')[0] )
    outputFile_r.close()

    outputFile = open(outputFileName, 'a')

else:
    outputFile = open(outputFileName, 'w')
    outputFile.write( 'pmid, score, numReaders, cited (altmetric), scopus\n' )


am_metadata = Altmetric()

c = 0
for line in setLinks:
    if c > numLines2Skip:
        parsedData    = line.split('\n')[0].split(',')
        pmid = parsedData[2]
        if not( pmid in listpmid_alreadyDone):
            paperMetadata = am_metadata.pmid( pmid )
            if paperMetadata != None:
                print( 'Evaluating pmid ' + pmid )
                score      = paperMetadata['score']
                numReaders = paperMetadata['readers_count']
                cited_by = 0
                for key in paperMetadata.keys():
                    if 'cited_by_' in key:
                            cited_by += paperMetadata[key]
                if 'scopus_subjects' in paperMetadata.keys():
                    scopus_subjects = paperMetadata['scopus_subjects']
                outputFile.write( pmid + s + str(score) + s + str(numReaders) + s +  \
                                    str(cited_by) + s + str(scopus_subjects) + '\n' )
            else:
                print( 'None found, pmid ' + pmid )
        else:
            print( 'Already added, pmid ' + pmid )

    print('line ' + str(c))
    c += 1

outputFile.close()
