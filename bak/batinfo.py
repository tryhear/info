import os

rootdir = ".\\"
for parent,dirnames,filenames in os.walk(rootdir):
    #for dirname in dirnames:
    #    thedir = parent+'\\'+dirname
        #print(thedir)
    for filename in filenames:
        if filename.split('.')[-1]=='xlsx':
            #print(parent+'\\'+filename)
            os.system("info_bat.py "+parent+'\\'+filename)
