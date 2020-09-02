import os
import glob 
f=open("fonts.txt","r").read().split("\n")[:-1]
lfont=glob.glob("font/*")
for x in lfont:
    if(x.split("/")[-1] not in f):
        os.remove(x)
