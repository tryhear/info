import os
import os.path
import time
import math

#sudo apt install ocrmypdf
#sudo apt install tesseract-ocr-chi-sim


def changeTime(allTime):
    day = 24*60*60
    hour = 60*60
    min = 60
    if allTime <60:        
        return  "%d 秒"%math.ceil(allTime)
    elif  allTime > day:
        days = divmod(allTime,day) 
        return "%d 天, %s"%(int(days[0]),changeTime(days[1]))
    elif allTime > hour:
        hours = divmod(allTime,hour)
        return '%d 小时, %s'%(int(hours[0]),changeTime(hours[1]))
    else:
        mins = divmod(allTime,min)
        return "%d 分钟, %d 秒"%(int(mins[0]),math.ceil(mins[1]))



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
print("\n处理 %s 个文件一共耗时 %s.\n" %(count,changeTime(elapsd)))
