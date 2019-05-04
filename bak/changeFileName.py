# -*- coding: UTF-8 -*-

import re

def changes1(file): #修改的文件名及起始文件编号
    cp = re.compile(r'<文件')

    qsy=re.compile(r'\bQsy="([0-9]*)"')
    zzy=re.compile(r'\bZzy="([0-9]*)"')
    sl=re.compile(r'\bSl="([0-9]*)"')
    file_data = ""
    with open(file,'r',encoding='utf-8') as f:
        for line in f:
            k=re.search(cp,line)
            if k:
                q=re.search(qsy,line).group(1)
                q=int(q)
                print(q)
                z=re.search(zzy,line).group(1)
                z=int(z)
                print(z)
                num=z-q+1
                num=str(num)
                print (num)
                nn=sl.sub(r'Sl="%s"'% num,line)
                file_data+=nn
            else:
                file_data += line

    with open ('2.xml','w+',encoding='utf-8') as f: #生成的文件
        f.write(file_data)

changes1('info.xml')
