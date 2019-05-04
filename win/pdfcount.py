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


def CompressImage(image_name):
    os.system("magick -resize \"3000x4000\" %s %s" % (image_name, image_name))


def CompressAll():
    ext_names = ['.JPG', '.jpg', '.jepg']
    for each_image in os.listdir('./'):
        for ext_name in ext_names:
            if each_image.endswith(ext_name):
                CompressImage(each_image)
                break


# CompressAll()
'''
rootdir = ".\\"
for parent,dirnames,filenames in os.walk(rootdir):
    for dirname in dirnames:
        thedir = parent+'\\'+dirname
        print(thedir)
        os.system("magick %s\\*.jpg %s\\%s.pdf" %(thedir,thedir,thedir))


# PdfLinearize()
rootdir = ".\\"
for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        if filename.endswith('.pdf'):
            for dirname in dirnames:
                thedir=parent+'\\'+dirname
                print(thedir)
                thefilename = thedir+'\\'+filename
                print(thefilename)
                print("qpdf --linearize %s %s.1" %(thefilename,thefilename))
                os.system("qpdf --linearize %s %s.1" %(thefilename,thefilename))

'''

uid=int(uuid.uuid4())
pw=uid//111111//999999//888888//222222//333333//666666
key=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'\n\n'+str(uid)+'\n'+str(pw)

my_sender='22622211@qq.com'    # 发件人邮箱账号
my_pass = 'asimaumtnvzzbgeg'              # 发件人邮箱密码
my_user='22622211@qq.com'      # 收件人邮箱账号，我这边发送给自己
def mail():
    ret=True
    try:
        msg=MIMEText(key,'plain','utf-8')
        msg['From']=formataddr(["FromRunoob",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["FK",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="PDFcount key"                # 邮件的主题，也可以说是标题
 
        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret
 
ret=mail()
if ret:
    #print("PDF页面统计")
    pass
else:
    print("请联网!")

print('\n运行码:'+str(uid))
test=0
test1=0
while test==0:
    if test1 > 2:
        sys.exit()
    pws=input('\n请输入密码:')
    try:
        if int(pws)==uid//111111//999999//888888//222222//333333//666666:
            test=1
        else:
            print('密码错!\n')
            test1+=1
    except:
        print('密码错!\n')
        test1+=1
# PdfLinearize()
#rootdir = ".\\"
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
            numpages = reader.getNumPages()
            print(parent + '\\' + filename + '   共' + str(numpages) + '页')
            for i in range(reader.numPages):
                dic = dict(reader.pages[i])
                # print(dic)
                for (k, v) in dic.items():
                    if k == '/MediaBox':

                        sot = sorted(v)
                        print("第%s页 : %s x %s" % (i + 1, sot[2] // 72 * 300, sot[3] // 72 * 300))
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
                # print('\n')

            #print (os.path.dirname(thefile))
            try:
                os.chdir(os.path.dirname(thefile))
            except BaseException:
                os.chdir(rootdir)

            file_num += 1
            count = count + numpages
            print('\n')

'''
print('='*50)
print('检查到 %s个文件共 '%file_num + str(count) + ' 页,其中:')
#print('-'*50)
print("\n")
print(tabulate([["A4",a4,"--->",a4],["A3",a3,"--->",a3*2],["A2",a2,"--->",a2*4],["A1",a1,"--->",a1*8],["A0",a0,"--->",a0*16]],headers=["幅面","页数","","折合A4"],tablefmt='orgtbl'))
#print('其中A4 %s页，A3 %s页, A2 %s页, A1 %s页, A0 %s页' % (a4, a3, a2, a1, a0))
#print('-'*50)
print("\n")
print('折算后总计： %s 页'%(a4+a3*2+a2*4+a1*8+a0*16))
print('-'*50)
'''

tableprint.banner('检查到 %s 个文件共 ' % file_num + str(count) + ' 页', style='clean')
header = ['幅面', '页数', '', '折合A4']
data = [["A4", a4, "--->", a4], ["A3", a3, "--->", a3 * 2], ["A2", a2, "--->", a2 * 4], ["A1", a1, "--->", a1 * 8], ["A0", a0, "--->", a0 * 16]]
tableprint.table(data, header)
tableprint.banner('图纸折算A4后总计 %s 页' % (a4 + a3 * 2 + a2 * 4 + a1 * 8 + a0 * 16), style='clean')
input()
