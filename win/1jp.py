# -*-coding:utf-8 -*-

from lxml import etree
import time
import prettytable
import sys
import os
import xlsxwriter
import tkinter as tk
from tkinter import filedialog

def jxxml(file):
    try:
        tree = etree.parse(file)
        treeview = etree.tounicode(tree, pretty_print=True)
    except BaseException:
        print('文件不存在！')

    dtsl = len(tree.xpath('//单位工程'))
    global zdjh
    zdjh=input('起始总登记号:')
    try:
        zdjh=int(zdjh)
    except:
        try:
            zdjh=int(input('\n总登记号必须为数字!!!请输入正确的总登记号：'))
        except:
            print('\n不跟你玩了！！！')
            sys.exit()
    #bzdw=input('编制单位:')
    #bzrq=input('编制日期(YYYY-MM-DD):')
    bzdw = tree.xpath('//项目/@Jsdw')[0]
    #bzrq = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    bzrq = tree.xpath('//单位工程[1]//案卷[1]/@Bzrq')[0]
    #print(bzrq)

    
    for i in range(dtsl):
        count=1
        j = i + 1
        print(j, end=':')
        print(tree.xpath('//单位工程[%s]/@Gcmc' % j)[0])
        wjm = tree.xpath('//单位工程[%s]/@Gcmc' % j)[0]

        workbook = xlsxwriter.Workbook(wjm + '.xlsx')
        worksheet = workbook.add_worksheet()

        table = prettytable.PrettyTable(
            ["序号", "文件编号", "责任者", "文件题名", "日期", "页次", "备注"])

        table.padding_witdth = 1

        gcdh = tree.xpath('//单位工程[%s]/@Gcdh' % j)
        ajsl = len(tree.xpath('//单位工程[%s]/案卷' % j))
        xrh=0
        
        for oo in range(ajsl):
            #print(tree.xpath('//单位工程[%s]//案卷[%s]//文件[last()]/@Zzy' % (j, str(oo + 1)))[0])  #确定终止页
            zzy = tree.xpath('//单位工程[%s]//案卷[%s]//文件[last()]/@Zzy' % (j, str(oo + 1)))[0]
            worksheet.write(xrh, 7, zzy)
            ajtm = tree.xpath('//单位工程[%s]//案卷[%s]/@Ajtm' % (j, str(oo + 1)))
            #if not '图' in ajtm[0]:
            if not ajtm[0].endswith('图'):
                worksheet.write(xrh, 0, gcdh[0]+'-'+str(count).zfill(3))
                worksheet.write(xrh, 1, ajtm[0])
                #zdjh = tree.xpath('//单位工程[%s]//案卷[%s]/@Zdjh' % (j,str(oo+1)))
                worksheet.write(xrh, 2, str(zdjh))
                worksheet.write(xrh, 3, str(ajsl))
                worksheet.write(xrh, 4, str(oo+1))
                worksheet.write(xrh, 5, bzdw)
                worksheet.write(xrh, 6, bzrq)
                xrh+=1
            else:
                xrh+=1
            
            count+=1
            zdjh+=1
        workbook.close()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    fn = filedialog.askopenfilename(filetypes=(('xml源', '*.xml'), ('csv源', '*.csv')))
    oschdir = os.path.dirname(fn)
    os.chdir(oschdir)
    fn = fn.split('/')[-1]
    #print(fn)
    fn1 = fn.split('.')[0]
    #print(fn1)
    jxxml(fn)
    print("End of ",end='')
    print(zdjh-1)
