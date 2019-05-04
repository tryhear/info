# -*- coding: UTF-8 -*-

import re
import sys

def changefilenum(file):
    # nm = int(nm)
    cp = re.compile(r'<文件')
    cp1 = re.compile(r'<案卷')
    id = re.compile(r'\bId="([0-9]*)"')
    dt1 = re.compile(r'\bFileId="([0-9]*)"')
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
                    # nm+=1
                    file_data += nn
                else:
                    file_data += line
            elif kk:
                l=re.search(id,line)
                if l:
                    ajid+=1
                    nn=id.sub(r'Id="%s"' % ajid,line)
                    fileid+=1
                    file_data+=nn
            else:
                file_data += line

    with open (file,'w+',encoding='utf-8') as f:
        f.write(file_data)
    print ('\nok!')

if __name__ =='__main__':
    changefilenum(sys.argv[1])