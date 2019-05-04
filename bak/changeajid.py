# -*- coding: UTF-8 -*-

import re
import sys

def changeajid(file,nm):
    nm = int(nm)
    cp = re.compile(r'<案卷')
    dt = re.compile(r'Id="[0-9]*"')
    file_data = ""
    with open(file,'r',encoding='utf-8') as f:
        for line in f:
            k=re.search(cp,line)
            if k:
                l=re.search(dt,line)
                if l:
                    ll=l.group(0)
                    nn=dt.sub(r'Id="%s"'%nm,line)
                    nm+=1
                    file_data += nn
                else:
                    file_data += line
            else:
                file_data += line

    with open (file,'w+',encoding='utf-8') as f:
        f.write(file_data)
    print ('\nok!')

if __name__ =='__main__':
    changeajid(sys.argv[1],sys.argv[2])