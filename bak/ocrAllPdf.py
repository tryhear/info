import os
import os.path
import time

#sudo apt install ocrmypdf
#sudo apt install tesseract-ocr-chi-sim

start=round(time.time())
rootdir = "./"
countfile=0

for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        if filename.endswith(".pdf"):
            countfile+=1

count=countfile

for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        if filename.endswith(".pdf"):
            thefile = parent+'/'+filename
            print(thefile,countfile)
            countfile-=1
            #os.system("ocrmypdf --force-ocr -l chi_sim %s %s" %(thefile,thefile))
            os.system("ocrmypdf --output-type pdf -l chi_sim %s %s" %(thefile,thefile))

elapsd=(round(time.time())-start)
print("\n处理 %s 个文件一共耗时 %s 分钟.\n" %(count,round(elapsd/60)))
