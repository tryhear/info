import os,sys
import os.path
#from tabulate import tabulate
import tableprint
from PyPDF2 import PdfFileReader
import random
import uuid
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import time


rootdir = os.getcwd()
count = 0
a4 = 0
a3 = 0
a2 = 0
a1 = 0
a0 = 0
file_num = 0
for parent, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
        if filename.endswith('.pdf'):
            thefile = parent + '\\' + filename
            reader = PdfFileReader(thefile)
            #print(reader.documentInfo)
            mes='非双层PDF'
            #try:
            #    reader.pages[0]['/Resources']['/Font']
            #except:
            #    mes='非双层PDF '
            for i in range(len(reader.pages)):
                try:
                    if reader.pages[i]['/Resources']['/Font']:
                        mes = ''
                        break
                    else:
                        msg = '非双层PDF '
                except:
                    msg = '非双层PDF '
            numpages = reader.getNumPages()
            print(parent + '\\' + filename + '   共' + str(numpages) + '页',end='')
            for i in range(reader.numPages):
                dic = reader.pages[i]
                #try:
                #    dic['/Resources']['/Font']
                    #print(dic)
                #except:
                #    print('\n第%s页不是双层PDF'%str(i+1))
                for (k, v) in dic.items():
                    #print('%s:%s'%(k,v),end='')
                    if k == '/MediaBox':
                        sot = sorted(v)
                        #print("第%s页 : %s x %s" % (i + 1, sot[2] // 72 * 300, sot[3] // 72 * 300),end='')
                        duanbian = int(sot[2]) // 72 * 300
                        changbian = int(sot[3]) // 72 * 300
                        if changbian <= 4959:
                            a4 += 1
                            #print("    A4")
                            continue
                        elif changbian <= 7017:
                            a3 += 1
                            #print("    A3")
                            continue
                        elif changbian <= 9917:
                            a2 += 1
                            #print("    A2")
                            continue
                        elif changbian <= 14034:
                            a1 += 1
                            #print("    A1")
                            continue
                        else:
                            a0 += 1
                            #print("    A0")
                            

            #print('\x1b[3;31;40m %s \x1b[0m'%mes)
            print('   '+mes)

            #print (os.path.dirname(thefile))
            try:
                os.chdir(os.path.dirname(thefile))
            except BaseException:
                os.chdir(rootdir)

            file_num += 1
            count = count + numpages
print('\n')



tableprint.banner('检查到 %s 个文件共 ' % file_num + str(count) + ' 页', style='grid')
header = ['幅面', '页数']
data = [["A4", a4], ["A3", a3], ["A2", a2], ["A1", a1], ["A0", a0]]
tableprint.table(data, header, style='grid')
input()
