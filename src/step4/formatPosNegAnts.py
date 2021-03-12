import os, sys

label_dir = sys.argv[1]
termDict = "/share/pi/stamang/nlp/clever-snomed/res/dicts/newTermFile.txt"
fneg = label_dir + "allNeg.txt"
fpos = label_dir + "allPos.txt"
fout = open(label_dir+"labeledAnts.txt","w")
#5000|a and b waves reduced|SNOMED|277007008|DISO

with open(termDict) as f:
    tdict = {}
    for line in f:
        tmp = line.strip().split("|")
        tdict[tmp[1]]=[tmp[3],tmp[4]]
f.close()

with open(fneg) as f:
    for line in f:
        tmp = line.strip().split("|")
        snippet = tmp[17].lstrip("SNIPPET: ")
        tinfo = tdict[tmp[5]]
        print >> fout, tmp[5]+"|"+tinfo[0]+"|"+tinfo[1]+"|"+tmp[0]+"|"+tmp[1]+"|"+tmp[8]+"|"+tmp[9]+"|"+tmp[12]+"|"+snippet
        print tmp[5]+"|"+tinfo[0]+"|"+tinfo[1]+"|"+tmp[0]+"|"+tmp[1]+"|"+tmp[8]+"|"+tmp[9]+"|"+tmp[12]+"|"+snippet
f.close()


with open(fpos) as f:
    for line in f:
        tmp = line.strip().split("|")
        snippet = tmp[17].lstrip("SNIPPET: ")
        tinfo = tdict[tmp[5]]
        print >> fout, tmp[5]+"|"+tinfo[0]+"|"+tinfo[1]+"|"+tmp[0]+"|"+tmp[1]+"|"+tmp[8]+"|"+tmp[9]+"|"+tmp[12]+"|"+snippet
        print tmp[5]+"|"+tinfo[0]+"|"+tinfo[1]+"|"+tmp[0]+"|"+tmp[1]+"|"+tmp[8]+"|"+tmp[9]+"|"+tmp[12]+"|"+snippet
f.close()
