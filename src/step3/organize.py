import os, sys, operator
from step3fcn import *

ppath = sys.argv[1]      #project path where the output of step2 lives
dictfile = sys.argv[2]   #terminology file
noteMdata = sys.argv[3]  #note metadata
ptAntfile = sys.argv[4]  #annotation file

# TARGET CLASSES #
target_class_dir = ["snomed"]
datasource = ["mimic3"]
termDict = getTerminology(dictfile)  #get terminology

noteMDict = loadMimicNoteMdata(noteMdata)
print("NOTES:", len(noteMDict))

seqDict = {}
print("TARGETS:",len(target_class_dir))
for target in target_class_dir:
    print("TARGET:",target)
    seqFile = ppath + "/extraction*.tsv"
    #print seqFile
    # passing loadSeqs the extraction files, note metadata and dictionary
    tmpDict = loadSeqs(seqFile,noteMDict,termDict)
    #print tmpDict
    seqDict.update(tmpDict)
print(len(seqDict))
print("CANDIDATE EVENTS:", str(len(seqDict)))

fout = open(ptAntfile,"w")
for sid in seqDict:
    tmp = seqDict[sid]
    sinfo = tmp.split("|")
    print(tmp, file=fout)
fout.close()
