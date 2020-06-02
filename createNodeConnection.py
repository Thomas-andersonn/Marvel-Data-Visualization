import json
f= open("jsonFile.json",)
data=json.load(f)
# print(data["links"]);
dict={}
for x in data["links"]:
    tempDict = {}
    tempDict["text"] = x["target"];
    tempDict["value"] = x["value"];
    if x["source"] in dict:
        dict[x["source"]].append(tempDict)
    else:
        dict[x["source"]]=[];
        dict[x["source"]].append(tempDict);
with open('nodeConnections.json', 'w') as outfile:
    json.dump(dict, outfile)