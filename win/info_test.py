# -*- coding: UTF-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import time
import datetime
import os
import sys
import codecs
import colorama
import pyfiglet
import uuid
import random
import shutil
import re
from prettytable import *
import webbrowser
from PyPDF2 import PdfFileReader, PdfFileWriter
# import traceback

def tb():
    os.system('cls')
    print(colorama.Fore.LIGHTYELLOW_EX + (pyfiglet.figlet_format(
        "XinXinDangAn", font="small")))
    print(
        colorama.Fore.LIGHTYELLOW_EX +
        "城建档案XML目录录入系统\n\nCopyright 2017\n四川欣兴档案管理咨询有限公司\nAll rights reserved.")
    print(colorama.Back.RESET, end="")
    print(colorama.Fore.LIGHTWHITE_EX +
          "--------------------------------------------------------\n\n")


def xm(fn):
    print(fn)
    if not os.path.exists(fn):
        print("File not exist:"+fn)
        return
    name=os.path.splitext(fn)
    fn1=name[0]
    print(fn)
    print(colorama.Fore.LIGHTWHITE_EX + colorama.Back.LIGHTBLUE_EX +
          "请按条目输入项目概况的内容:")
    print(colorama.Back.RESET, end="")
    print(colorama.Fore.LIGHTRED_EX +
          "========================================================\n")
    print(colorama.Fore.RESET, end="")
    bz = ""
    key = str(uuid.uuid4()).upper()
    global xmmc, xmdd, xmid
    '''
    while True:
        xmmc = input(colorama.Fore.LIGHTWHITE_EX + ("项目名称:"))
        if xmmc:
            break
        else:
            print("项目名称是必须填的！\n")
    while True:
        xmid = input(colorama.Fore.LIGHTWHITE_EX + ("项目类型:"))
        if xmid:
            break
        else:
            print("项目类型是必须填的！\n")
    '''
    xmmc=fn1
    xmid=0
    if not os.path.exists(xmmc):
        os.mkdir(xmmc)
    fo = codecs.open(xmmc + '\\' + xmmc + '.xml', "w+", "utf-8")
    fo.seek(0, 2)
    report = codecs.open(xmmc + '\\' + "report.html", "w+", "gb2312")
    report.seek(0, 2)
    fo.write("<?xml version=\"1.0\"  encoding=\"utf-8\"?>\n")
    fo.write("<电子文件信息>\n")
    type = "0"
    xmdd=''#xmdd = input(colorama.Fore.LIGHTWHITE_EX + ("项目地点:"))
    global jsdw, djdw, jldw, kcdw, yjdw, lxpzdw, lxpzwh, sjdw
    global ghxkzh, ydghxkzh, ydxkzh, sgxkzh
    jsdw=''#jsdw = input(colorama.Fore.LIGHTWHITE_EX + ("建设单位:"))
    djdw = ''
    jldw=''#jldw = input(colorama.Fore.LIGHTWHITE_EX + ("监理单位:"))
    kcdw=''#kcdw = input(colorama.Fore.LIGHTWHITE_EX + ("勘察单位:"))
    sjdw=''#sjdw = input(colorama.Fore.LIGHTWHITE_EX + ("设计单位:"))
    yjdw = jsdw
    lxpzdw=''#lxpzdw = input(colorama.Fore.LIGHTWHITE_EX + ("立项批准单位:"))
    ydxkzh =  ""
    lxpzwh=''#lxpzwh = input(colorama.Fore.LIGHTWHITE_EX + ("立项批准文号:"))
    ghxkzh=''#ghxkzh = input(colorama.Fore.LIGHTWHITE_EX + ("规划许可证号:"))
    ydghxkzh=''#ydghxkzh = input(colorama.Fore.LIGHTWHITE_EX + ("用地规划许可证号:"))
    sgxkzh=''#sgxkzh = input(colorama.Fore.LIGHTWHITE_EX + ("施工许可证号:"))
    print('\n')
    bz = ""
    fo.write(
        u"  <项目 Id=\"%s\" Type=\"%s\" Xmmc=\"%s\" Xmdd=\"%s\" Jsdw=\"%s\" Djdw=\"%s\" Lxpzdw=\"%s\" Sjdw=\"%s\" Jldw=\"%s\" Kcdw=\"%s\" Lxpzwh=\"%s\" Ghxkzh=\"%s\" Ydghxkzh=\"%s\" Ydxkzh=\"%s\" Sgxkzh=\"%s\" Yjdw=\"%s\" Bz=\"%s\" Key=\"%s\">\n" %
        (xmid,
         type,
         xmmc,
         xmdd,
         jsdw,
         djdw,
         lxpzdw,
         sjdw,
         jldw,
         kcdw,
         lxpzwh,
         ghxkzh,
         ydghxkzh,
         ydxkzh,
         sgxkzh,
         yjdw,
         bz,
         key))
    fo.flush()
    report.flush()
    fo.close()
    report.close()


def dwgc():
    fo = codecs.open(xmmc + '\\' + xmmc + '.xml', "r+", "utf-8")
    fo.seek(0, 2)
    report = codecs.open(xmmc + '\\' + "report.html", "r+", "gb2312")
    report.seek(0, 2)
    print(colorama.Fore.LIGHTWHITE_EX + colorama.Back.LIGHTBLUE_EX +
          "请按条目输入单位工程的内容:")
    print(colorama.Back.RESET, end="")
    print(colorama.Fore.LIGHTRED_EX +
          "========================================================\n")
    colorama.init()
    zs = ""
    projectid = xmid
    bgqx = ""
    mj = "0"
    bz = ""
    key = str(uuid.uuid4()).upper()
    global gcmc, gcdd, sgdw, kgrq, jgrq, gcys, gcjs, gd, jzmj, ydmj, dscs, dzcs
    global gcdh, dscs, dxcs, jclx, jglx, dwgcid, zdjh_
    print(colorama.Fore.RESET, end="")
    gcmc = xmmc
    '''
    dwgcid = input(colorama.Fore.LIGHTWHITE_EX + ("单体序号:"))
    if not dwgcid.isdigit():
        dwgcid = 1
    gcdh = input(colorama.Fore.LIGHTWHITE_EX + ("工程档号:"))
    zdjh_ = input(colorama.Fore.LIGHTWHITE_EX + ("总登记号:"))
    if not zdjh_.isdigit():
        zdjh_ = 0
    zdjh_ = int(zdjh_)
    zdjh_ -= 1
    gcdd = xmdd
    sgdw = input(colorama.Fore.LIGHTWHITE_EX + ("施工单位:"))
    kgrq_ = input(colorama.Fore.LIGHTWHITE_EX + ("开工日期:"))
    if not kgrq_.isdigit() or len(kgrq_) < 8:
        kgrq = ""
    else:
        kgrq = kgrq_[:4] + '/' + kgrq_[4:6] + '/' + kgrq_[6:8]
    try:
        t = time.strptime(kgrq, '%Y/%m/%d')
    except ValueError:
        kgrq = ""
    jgrq_ = input(colorama.Fore.LIGHTWHITE_EX + ("竣工日期:"))
    if not jgrq_.isdigit() or len(jgrq_) < 8:
        jgrq = ""
    else:
        jgrq = jgrq_[:4] + '/' + jgrq_[4:6] + '/' + jgrq_[6:8]
    try:
        t = time.strptime(jgrq, '%Y/%m/%d')
    except ValueError:
        jgrq = ""
    '''
    zdjh_=0
    gcdd = xmdd
    dwgcid=''
    gcdh=''
    zdjh=''
    sgdw=''
    kgrq=''
    jgrq=''
    gcys = 0
    gcjs = 0
    jzmj = ydmj = "0"
    gd = zs = "0"
    dscs = dxcs = "0"
    type = "0"
    jclx = jglx = ""
    fo.write(
        "      <单位工程 Jb=\"\" Hz=\"\" Cd=\"0\" Kd=\"0\" Kj=\"0\" Ks=\"0\" Jk=\"\" Gd=\"%s\" Jzmj=\"%s\" Ydmj=\"%s\" Dscs=\"%s\" Dxcs=\"%s\" Jclx=\"%s\" Jglx=\"%s\" Kgrq=\"%s\" Jgrq=\"%s\" Zs=\"%s\" Gcys=\"%s\" Gcjs=\"%s\" Id=\"%s\" ProjectId=\"%s\" Type=\"%s\" Gcmc=\"%s\" Gcdd=\"%s\" Gcdh=\"%s\" Bgqx=\"%s\" Mj=\"%s\" Jsdw=\"%s\" Djdw=\"%s\" Sgdw=\"%s\" Lxpzdw=\"%s\" Sjdw=\"%s\" Jldw=\"%s\" Kcdw=\"%s\" Lxpzwh=\"%s\" Ghxkzh=\"%s\" Ydghxkzh=\"%s\" Ydxkzh=\"%s\" Sgxkzh=\"%s\" Yjdw=\"%s\" Bz=\"%s\" Key=\"%s\" >\n" %
        (gd,
         jzmj,
         ydmj,
         dscs,
         dxcs,
         jclx,
         jglx,
         kgrq,
         jgrq,
         zs,
         gcys,
         gcjs,
         dwgcid,
         projectid,
         type,
         gcmc,
         gcdd,
         gcdh,
         bgqx,
         mj,
         jsdw,
         djdw,
         sgdw,
         lxpzdw,
         sjdw,
         jldw,
         kcdw,
         lxpzwh,
         ghxkzh,
         ydghxkzh,
         ydxkzh,
         sgxkzh,
         yjdw,
         bz,
         key))
    report.write("<h1>%s报告:</h1><br>"%xmmc)
    report.write("<hr><br>")
    report.write("项目名称:%s<br>" % xmmc)
    report.write("项目地点:%s<br>" % xmdd)
    report.write("建设单位:%s<br>" % jsdw)
    report.write("地基单位:%s<br>" % djdw)
    report.write("监理单位:%s<br>" % jldw)
    report.write("勘察单位:%s<br>" % kcdw)
    report.write("设计单位:%s<br>" % sjdw)
    report.write("移交单位:%s<br>" % yjdw)
    report.write("立项批准单位:%s<br>" % lxpzdw)
    report.write("立项批准文号:%s<br>" % lxpzwh)
    report.write("规划许可证号:%s<br>" % ghxkzh)
    report.write("用地规划许可证号:%s<br>" % ydghxkzh)
    report.write("施工许可证号:%s<br>" % sgxkzh)
    report.write("工程名称:%s<br>" % gcmc)
    report.write("工程地点:%s<br>" % gcdd)
    report.write("工程档号:%s<br>" % gcdh)
    report.write("施工单位:%s<br>" % sgdw)
    report.write("开工日期:%s<br>" % kgrq)
    report.write("竣工日期:%s<br><br>" % jgrq)
    report.write("<hr><br>")
    fo.flush()
    report.flush()
    fo.close()
    os.system('cls')

def yjnr():
    fo = codecs.open(xmmc + '\\' + xmmc + '.xml', "r+", "utf-8")
    fo.seek(0, 2)
    fo.write("          <移交目录>\n")
    id = int((random.random() * 100000))
    id2 = 0
    line1 = '              <移交内容 Id="%s" ReceiveListId="1" SingleProjectId="%s" ParentId="%s" SerialNumber="" Name="%s" Sequence="0" Key="%s" />\n'
    line2 = '              <移交内容 Id="%s" ReceiveListId="2" SingleProjectId="%s" ParentId="%s" SerialNumber="" Name="%s" Sequence="0" Key="%s" />'
    fo.write(line1 % (str(id), dwgcid, id2, gcmc,str(uuid.uuid4()).upper()))
    id2 = id
    id+=1
    fo.write(line2 % (str(id), dwgcid, id2, gcmc,str(uuid.uuid4()).upper()))
    global sid
    sid = id
    fo.write("\n          </移交目录>\n")
    fo.flush()
    fo.close()

def aj():
    fo = codecs.open(xmmc + '\\' + xmmc + '.xml', "r+", "utf-8")
    fo.seek(0, 2)
    report = codecs.open(xmmc + '\\' + "report.html", "r+", "gb2312")
    report.seek(0, 2)
    global table,wjyc
    wjyc=''
    table = PrettyTable(["文件名","起始页码","终止页码","页数","PDF状态","形成时间","文图号"])
    table.align["文件名"] = "l"
    table.padding_witdth = 1
    id_wj = 1
    id_aj = 1
    fileid = id_aj
    singleprojectid = dwgcid
    singleprojectrevceivelistid = sid
    dh = ""
    wth = ""
    bgqx = "1"
    ztlx = "0"
    wb = ""
    gg = "4"
    ty = ""
    ztc = ""
    fz = ""
    erecordsize = "0"
    md5 = ""
    cceptstatus = "0"
    ajh = ""
    zdjh = zdjh_
    ajtm = ""
    bzdw = ""
    gg = "0"
    bgqx = "0"
    ljsj = ""
    ztc = ""
    fz = ""
    bzdw = jsdw
    now_ = datetime.datetime.now()
    datenow_ = "%s-%s-%s" % (now_.year, now_.month, now_.day)
    ljsj = bzrq = datenow_
    print(colorama.Fore.RESET, end="")
    ljr = '杨颂'
    zrz = jsdw
    jnwjqssj = jnwjzzsj = datenow_
    jnwjqssj = jnwjzzsj = ""
    bgqx = "0"
    mj = "0"
    os.system("cls")
    try:
        os.system("xlsx2csv.py -c GBK %s.xlsx %s.csv "%(xmmc,xmmc))
    except:
        print ("没有可测试的文件")
        pass
    try:
        with open(xmmc + '.csv') as f:
            colorama.init(autoreset=True)
            fo = codecs.open(xmmc + '\\' + xmmc + '.xml', "r+", "utf-8")
            fo.seek(0, 2)
            report = codecs.open(xmmc + '\\' + "report.html", "r+", "gb2312")
            report.seek(0, 2)
            ajh = id_aj
            count = 0
            count_aj = 0
            no1st = 0
            ajtm_ = ''
            test_zzy=0
            test_zzy1=0
            try:
                shutil.rmtree(xmmc + '\\' + xmmc)
            except:
                pass
            for i in f.readlines():
                line = i.strip()
                line = ''.join(line.split())
                dt = re.compile(r',,,+')
                k=re.search(dt,line)
                if k:
                    line=dt.sub('',line)
                if ',' in line:
                    a = line.split(',')
                    try:
                        try:
                            int(a[1])
                        except:
                            continue
                        if a[1] == '0':
                            ajtm_ = a[0]
                            print(a[0])
                            wjyc+='***'+a[0]+'***</b><br>'
                        else:
                            count += 1
                        if a[1] == '1':
                            if not no1st == 0:
                                fo.write("          </案卷>\n")
                            zdjh += 1
                            no1st += 1
                            ajtm = gcmc + ajtm_
                            '''
                            print(
                                colorama.Fore.LIGHTYELLOW_EX +"          <案卷 Id=\"%s\" SingleProjectId=\"%s\" Ajh=\"%s\" Zdjh=\"%s\" Ajtm=\"%s\" Bzdw=\"%s\" Bzrq=\"%s\" Zrz=\"%s\" Gg=\"%s\" JnwjQssj=\"%s\" JnwjZzsj=\"%s\" Bgqx=\"%s\" Mj=\"%s\" Ljr=\"%s\" Ljsj=\"%s\" Ztc=\"%s\" Fz=\"%s\" Key=\"%s\">\n" %
                                (count_aj, singleprojectid, ajh, zdjh, ajtm, bzdw, bzrq, zrz, gg, jnwjqssj, jnwjzzsj, bgqx, mj, ljr, ljsj, ztc, fz, str(
                                    uuid.uuid4()).upper()))
                            '''
                            fo.write(
                                "          <案卷 Id=\"%s\" SingleProjectId=\"%s\" Ajh=\"%s\" Zdjh=\"%s\" Ajtm=\"%s\" Bzdw=\"%s\" Bzrq=\"%s\" Zrz=\"%s\" Gg=\"%s\" JnwjQssj=\"%s\" JnwjZzsj=\"%s\" Bgqx=\"%s\" Mj=\"%s\" Ljr=\"%s\" Ljsj=\"%s\" Ztc=\"%s\" Fz=\"%s\" Key=\"%s\">\n" %
                                (count_aj, singleprojectid, ajh, zdjh, ajtm, bzdw, bzrq, zrz, gg, jnwjqssj, jnwjzzsj, bgqx, mj, ljr, ljsj, ztc, fz, str(
                                    uuid.uuid4()).upper()))
                            ajtm_ = ''
                            test_zzy=0
                    except BaseException:
                        pass
                    try:
                        if a[1] == '0':
                            count_aj += 1
                            table.add_row(['','','','','','',''])
                            table.add_row(['第'+str(count_aj)+'卷','','','','','',''])
                            table.add_row(['-----','','','','','',''])
                            continue
                    except BaseException:
                        pass
                    try:
                        qsy = str(int(a[1]))
                    except BaseException:
                        qsy = '错误'
                        isok='错误'
                    try:
                        zzy = str(int(a[2]))
                        if int(zzy)-int(qsy)<0:
                            zzy='错误'
                    except BaseException:
                        zzy = '错误'
                        isok='错误'
                    if not int(a[1])-1 == int(test_zzy):
                        print ("*终止页 "+str(test_zzy)+" 错误!*\n")
                    test_zzy=a[2]

                    pdfcut = ''.join(zzy) + ','
                    try:
                        xcsj_ = str(a[3])
                        if xcsj_.isdigit() and len(xcsj_) > 7:
                            xcsj = xcsj_[:4] + '/' + \
                                xcsj_[4:6] + '/' + xcsj_[6:8]
                    except BaseException:
                        xcsj = ''
                    try:
                        t = time.strptime(xcsj, '%Y/%m/%d')
                    except ValueError:
                        xcsj = ""
                    try:
                        ab = str(int(a[2]) - int(a[1]) + 1)
                        if int(ab) > 0:
                            ab = ab
                        else:
                            ab = '错误'
                            isok='错误'
                    except BaseException:
                        ab = '错误'
                        isok='错误'
                    try:
                        wth = a[4]
                    except BaseException:
                        wth = ''
                    try:
                        # print(line)
                        wjyc+=line+'<br>'
                        '''
                        print(colorama.Fore.LIGHTCYAN_EX +"              <文件 Id=\"%s\" FileId=\"%s\" SingleProjectId=\"%s\" SingleProjectRevceiveListId=\"%s\" Dh=\"%s\" Wjtm=\"%s\" Wth=\"%s\" Zrz=\"%s\" Bgqx=\"%s\" Mj=\"%s\" Xcsj=\"%s\" Ztlx=\"%s\" Qsy=\"%s\" Zzy=\"%s\" Sl=\"%s\" Wb=\"%s\" Gg=\"%s\" Ty=\"%s\" Ztc=\"%s\" Fz=\"%s\" ERecordPath=\"%s\" ERecordSize=\"%s\" Md5=\"%s\" CceptStatus=\"%s\" Key=\"%s\" />" %
                            (count,
                             count_aj,
                             singleprojectid,
                             singleprojectrevceivelistid,
                             dh,
                             a[0],
                                wth,
                                zrz,
                                bgqx,
                                mj,
                                xcsj,
                                ztlx,
                                qsy,
                                zzy,
                                ab,
                                wb,
                                gg,
                                ty,
                                ztc,
                                fz,
                                gcmc +
                                '\\' +
                                str(count) +
                                '.pdf',
                                erecordsize,
                                md5,
                                cceptstatus,
                                str(
                                 uuid.uuid4()).upper()))
                        '''
                        fo.write(
                            "              <文件 Id=\"%s\" FileId=\"%s\" SingleProjectId=\"%s\" SingleProjectRevceiveListId=\"%s\" Dh=\"%s\" Wjtm=\"%s\" Wth=\"%s\" Zrz=\"%s\" Bgqx=\"%s\" Mj=\"%s\" Xcsj=\"%s\" Ztlx=\"%s\" Qsy=\"%s\" Zzy=\"%s\" Sl=\"%s\" Wb=\"%s\" Gg=\"%s\" Ty=\"%s\" Ztc=\"%s\" Fz=\"%s\" ERecordPath=\"%s\" ERecordSize=\"%s\" Md5=\"%s\" CceptStatus=\"%s\" Key=\"%s\" />\n" %
                            (count,
                             count_aj,
                             singleprojectid,
                             singleprojectrevceivelistid,
                             dh,
                             a[0],
                                wth,
                                zrz,
                                bgqx,
                                mj,
                                xcsj,
                                ztlx,
                                qsy,
                                zzy,
                                ab,
                                wb,
                                gg,
                                ty,
                                ztc,
                                fz,
                                gcmc +
                                '\\' +
                                str(count) +
                                '.pdf',
                                erecordsize,
                                md5,
                                cceptstatus,
                                str(
                                 uuid.uuid4()).upper()))
                    except BaseException:
                        pass
                    try:
                        os.mkdir(xmmc + '\\' + xmmc)
                    except BaseException:
                        pass
                    '''
                    try:
                        if int(ab) > 0:
                            reader = PdfFileReader(str(count_aj) + '.pdf')
                            writer = PdfFileWriter()
                            with open(xmmc + '\\' + str(count) + '.pdf', 'wb') as wstream:
                                for page in range(int(qsy) - 1, int(zzy)):
                                    temp = reader.getPage(page)
                                    writer.addPage(temp)
                                writer.write(wstream)
                            # print(colorama.Fore.LIGHTGREEN_EX +'PDF正常\n')
                            shutil.move(wstream.name, xmmc + '\\' + xmmc)
                            isok = ''
                    except BaseException:
                        print(colorama.Fore.LIGHTRED_EX +'%sPDF错误，对应文件%s第%s至第%s页\n'%(a[0],str(count_aj) + '.pdf',qsy,zzy))
                        isok='错误'
                    '''
                    isok=''
                    table.add_row([str(count) + '.pdf', qsy, zzy,ab,isok,xcsj,wth])
                    xcsj = ''
    except BaseException:
        pass
    try:
        if count > 1:
            fo.write("          </案卷>\n")
    except BaseException:
        pass
    fo.flush()
    report.flush()
    fo.close()
    report.close()


def wb():
    fo = codecs.open(xmmc + '\\' + xmmc + '.xml', "r+", "utf-8")
    fo.seek(0, 2)
    report = codecs.open(xmmc + '\\' + "report.html", "r+", "gb2312")
    report.seek(0, 2)
    fo.write("      </单位工程>\n")
    fo.write("  </项目>\n")
    fo.write("</电子文件信息>")
    # report.write(wjyc)
    # report.write('<br><hr><br>')
    s=table.get_html_string()
    report.write(s)
    print(colorama.Back.RESET, end="")
    fo.flush()
    report.flush()
    fo.close()
    report.close()


if __name__ == "__main__":
    os.system('cls')
    colorama.init()
    tb()
    xm(sys.argv[1])
    dwgc()
    yjnr()
    aj()
    wb()
    os.remove(xmmc + '\\report.html')
    print ("\n测试情况：")
    print (table)
    print('\n测试完成!\n')
