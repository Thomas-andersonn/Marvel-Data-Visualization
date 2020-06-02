import csv
import json
heroSet=set();
linkList=[];
nodeList=[]
dict={}
heroCount={};
topHeros={};
numberOfHeroes=50;
topHeroLinkList=[];
linkCount={}
with open('trimmed_edges.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    fields=next(csv_reader);
    i=0;
    for row in csv_reader:
        tempDict={};
        if row[0] in heroCount:
            heroCount[row[0]]+=1;
        else:
            heroCount[row[0]]=1;
        if row[1] in heroCount:
            heroCount[row[1]]+=1;
        else:
            heroCount[row[1]]=1;
        tempDict["source"]=row[0];
        tempDict["target"]=row[1];
        linkList.append(tempDict);
i=0;
for w in sorted(heroCount, key=heroCount.get, reverse=True):
    if i>=numberOfHeroes:
        break;
    topHeros[w]=heroCount[w];
    tempDict={}
    tempDict["id"]=w;
    nodeList.append(tempDict);
    i+=1;


for x in linkList:
    if x["source"] in topHeros and x["target"] in topHeros:
        if x["source"]+"$$"+x["target"] in linkCount:
            linkCount[x["source"]+"$$"+x["target"]]+=1;
        else:
            linkCount[x["source"]+"$$"+x["target"]]=1;
for x in linkCount:
    txt=x.split("$$");
    tempDict={}
    tempDict["source"]=txt[0];
    tempDict["target"]=txt[1]
    tempDict["value"]=linkCount[x];
    topHeroLinkList.append(tempDict);
dict["nodes"]=nodeList;
dict["links"]=topHeroLinkList;
print(dict)
with open('jsonFile.json', 'w') as outfile:
    json.dump(dict, outfile)
