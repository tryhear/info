# -*- coding: UTF-8 -*-

import re
import sys
import os
import tkinter as tk
from tkinter import filedialog

def changezdjh(file):
    nm=input('起始总登记号:')
    nm=int(nm)
    cp = re.compile(r'<案卷')
    dt = re.compile(r'Zdjh="[0-9]*"')
    file_data = ""
    with open(file,'r',encoding='utf-8') as f:
        for line in f:
            k=re.search(cp,line)
            if k:
                l=re.search(dt,line)
                if l:
                    ll=l.group(0)
                    nn=dt.sub(r'Zdjh="%s"'%nm,line)
                    nm+=1
                    file_data += nn
                else:
                    file_data += line
            else:
                file_data += line
    print('终止总登记号:',end='')
    print(nm-1,end='')
    with open (file,'w+',encoding='utf-8') as f:
        f.write(file_data)
    
def changefilenum(file):
    cp = re.compile(r'<文件')
    cp1 = re.compile(r'<案卷')
    id = re.compile(r'\bId="([0-9]*)"')
    dt1 = re.compile(r'\bFileId="([0-9]*)"')
    dt2 = re.compile(r'\bAjh="([0-9]*)"')
    file_data = ""
    ajid=0
    fileid=0
    with open(file,'r',encoding='utf-8') as f:
        for line in f:
            k=re.search(cp,line)
            kk=re.search(cp1,line)
            if k:
                l=re.search(id,line)
                if l:
                    nn=dt1.sub(r'FileId="%s"' % fileid,line)
                    file_data += nn
                else:
                    file_data += line
            elif kk:
                l=re.search(id,line)
                if l:
                    ajid+=1
                    nn=id.sub(r'Id="%s"' % ajid,line)
                    nn=dt2.sub(r'Ajh="%s"' % ajid,nn)
                    fileid+=1
                    file_data+=nn
            else:
                file_data += line

    with open (file,'w+',encoding='utf-8') as f:
        f.write(file_data)

if __name__ =='__main__':
    root=tk.Tk()
    root.withdraw()
    fn=filedialog.askopenfilename(filetypes=(('XML源','*.xml'),('所有源','*.*')))
    oschdir=os.path.dirname(fn)
    os.chdir(oschdir)
    fn=fn.split('/')[-1]
    changezdjh(fn)
    changefilenum(fn)
    input()
    # print ('\nok!')