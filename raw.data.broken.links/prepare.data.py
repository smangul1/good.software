import csv
import argparse
import sys
from collections import Counter

def is_number(var):
    try:
        if var == int(var):
            return True
    except Exception:
        return False

# 0 - timeout, -1 broken, 2 - redirection, 3 - normal
def classify_link(n):
    # broken link >=400
    # -1 - tme out
    # [300,400) - redirection
    if n==-1:
        return 0
    elif n>=400:
        return -1
    elif n>=300 and n<400:
        return 2
    else:
        return 3





#####################################
ap = argparse.ArgumentParser()
ap.add_argument('input_abstract', help='input')
ap.add_argument('input_body', help='input')
ap.add_argument('manual', help='list of manually checked links which were time out')
ap.add_argument('output', help='output')
args = ap.parse_args()







#List of links cheked manually
#Journal,ID,Year,Keyword,Link,Status,manual.flag
#Bioinformatics,18940825,2008,available,http://sitepredict.org/,-1,0

#0 means is it really -1 status

goodLinks=set()
file=open(args.manual)
reader=csv.reader(file)
next(reader,None)
for line in reader:
    if line[6]=='1':
        goodLinks.add(line[4])


print ("Number of manually identified good links",len(goodLinks))


#-----------------------------------------
#-----------------------------------------
#-----------------------------------------
#ABSTRACT





file=open(args.input_abstract,"r")
reader=csv.reader(file)


#['PLoS_Comput_Biol', '19381256', '2009', 'null', 'http://purl.org/net/cito/', '502',
# 'available', 'http://dx.doi.org/10.1371/journal.pntd.0000228.x001', '303']


linksSetAbstract=set()
dataAbstract=[]

for line in reader:

    #Bioinformatics,25173419,2015
    journal=line[0]
    id=line[1]
    year=line[2]

    if line[3]!="abstractNotFound":

        #print (line[3:len(line)-1],line)

        if len(line[3:len(line)-1]) % 3==0:
            #print(line[0:3], line[3:len(line)-1],len(line[3:len(line)-1]),len(line[3:len(line)-1]) % 3)
            for i in range(3,len(line)-1,3):
                status = line[i + 2]

                link=line[i+1]
                if ('http' in link or 'www' in link or 'ftp' in link) and (status.isdigit() or status=='-1'):
                    status=int(status)
                    if status==-1 and link in goodLinks:
                        status=200
                    linksSetAbstract.add(link)
                    dataAbstract.append((journal,id,year,link,status))


file.close()


print ("Number of links from abstracts",len(linksSetAbstract))


dict_year_Abstract={}


dictLinksAbstract={}

for d in dataAbstract:
    link = d[3]
    dict_year_Abstract[link]=[]

for d in dataAbstract:
    year=d[2]
    link=d[3]
    dict_year_Abstract[link].append(d)


new_dict_Abstract={}


fileOut=open(args.output,"w")


final_set_Abstract=set()

flag={}

for d in dataAbstract:
    link = d[3]



    if len(dict_year_Abstract[link])>1:

        tList=[]

        for i in dict_year_Abstract[link]:
            tList.append(int(i[2]))

        Min=min(tList)


        for i in dict_year_Abstract[link]:
            year=int(i[2])
            if year==Min:
                final_set_Abstract.add((i[0],i[1],i[2],i[3],i[4],'1'))


        #print (min(dict_year[link]),max(dict_year[link]))
        #new_dict[link]=min(dict_year[link])
    else:
        final_set_Abstract.add((d[0], d[1], d[2], d[3], d[4], '0'))
        flag[link] = 0 # was only mentioned onece in the body of the paper


fileOut.write("type,journal,id,year,link,code,flag.uniqueness")
fileOut.write("\n")


for i in final_set_Abstract:

    fileOut.write("abstract,"+str(i[0])+","+str(i[1])+","+str(i[2])+","+str(i[3])+","+str(i[4])+","+str(i[5]))
    fileOut.write("\n")







#----------------------------------------------------------
#----------------------------------------------------------
#Body

dict_year={}


file=open(args.input_body,"r")
reader=csv.reader(file)


#['PLoS_Comput_Biol', '19381256', '2009', 'null', 'http://purl.org/net/cito/', '502',
# 'available', 'http://dx.doi.org/10.1371/journal.pntd.0000228.x001', '303']


linksSet=set()
data=[]

for line in reader:

    #Bioinformatics,25173419,2015
    journal=line[0]
    id=line[1]
    year=line[2]

    if line[3]!="abstractNotFound" or line[2]!="NoLink":

        if len(line[3:len(line)-1]) % 3==0:
            #print(line[0:3], line[3:len(line)-1],len(line[3:len(line)-1]),len(line[3:len(line)-1]) % 3)
            for i in range(3,len(line)-1,3):
                status = line[i + 2]

                link=line[i+1]
                if ('http' in link or 'www' in link or 'ftp' in link) and (status.isdigit() or status=='-1'):
                    if link not in linksSetAbstract: #already was present in the abstract
                        status=int(status)
                        if status==-1 and link in goodLinks:
                            status=200
                        linksSet.add(link)
                        data.append((journal,id,year,link,status))


file.close()


print ("Number of links in the body exluding the one from the abstract",len(linksSet))

dictLinks={}

for d in data:
    link = d[3]
    dict_year[link]=[]

for d in data:
    year=d[2]
    link=d[3]
    dict_year[link].append(d)


new_dict={}




final_set=set()

flag={}

for d in data:
    link = d[3]



    if len(dict_year[link])>1:

        tList=[]

        for i in dict_year[link]:
            tList.append(int(i[2]))

        Min=min(tList)


        for i in dict_year[link]:
            year=int(i[2])
            if year==Min:
                final_set.add((i[0],i[1],i[2],i[3],i[4],'1'))


        #print (min(dict_year[link]),max(dict_year[link]))
        #new_dict[link]=min(dict_year[link])
    else:
        final_set.add((d[0], d[1], d[2], d[3], d[4], '0'))
        flag[link] = 0 # was only mentioned onece in the body of the paper


for i in final_set:

    fileOut.write("body,"+str(i[0])+","+str(i[1])+","+str(i[2])+","+str(i[3])+","+str(i[4])+","+str(i[5]))
    fileOut.write("\n")


fileOut.close()