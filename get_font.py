import glob
f=open("fonts.txt","w+")
for x in glob.glob("testFont/*"):
    f.writelines((x[:-4]).split('/')[-1]+"\n")