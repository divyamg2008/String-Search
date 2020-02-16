import os
import csv

dirPath = os.path.dirname(__file__)
f= open(r"{}\string.txt".format(dirPath),"r")
search = []
for each in f:
    search.append(each.strip("\n"))
# print(search)

logs =os.listdir(r"{}\input".format(dirPath))
fo= open(r"{}\Output.csv".format(dirPath),"w+", newline='')
fieldNames = ["File Name", "Word Searched", "Matches"]
writer = csv.DictWriter(fo,fieldNames)
writer.writeheader()
fo.write("~"*30+"\n")
tcount = 0
matches ={}
def matchSearch():
    global tcount
    global matches
    for i in logs:
        fi = open(r"{0}\input\{1}".format(dirPath,i), "r")
        
        for word in search:
            wcount = 0

            lc = 0
            for line in fi:
                lc+=1
                if line.count(word)!=0:
                    wcount+=1

                    matches[i+":lno.:"+str(lc)] = line.strip("\n")

            fi.seek(0)
            tcount= tcount+ wcount
            if(wcount !=0):

                writer.writerow({"File Name": i, "Word Searched": word, "Matches" : wcount})
  
matchSearch()
fo.write("~"*30+"\n")
writer.writerow({"File Name": "Total Matches","Matches": tcount})  
fo.write("~"*30+"\n")
fo.write("Matched Lines"+"\n")
for each in matches:
    writer.writerow({"File Name": each, "Matches": matches[each]})     

fo.write("~"*15+"EOF"+"~"*15+"\n")   