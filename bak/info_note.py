# -*- coding: UTF-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import time
import datetime
import os
import codecs
import colorama
import pyfiglet
import uuid
import random
import shutil
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


def xm():
    print(colorama.Fore.LIGHTWHITE_EX + colorama.Back.LIGHTBLUE_EX +
          "请按条目输入项目概况的内容:")
    print(colorama.Back.RESET, end="")
    print(colorama.Fore.LIGHTRED_EX +
          "========================================================\n")
    print(colorama.Fore.RESET, end="")
    bz = ""
    key = str(uuid.uuid4()).upper()
    global xmmc, xmdd, xmid
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
    if not os.path.exists(xmmc):
        os.mkdir(xmmc)
    fo = codecs.open(xmmc + '\\' + xmmc + '.xml', "w+", "utf-8")
    fo.seek(0, 2)
    report = codecs.open(xmmc + '\\' + "report", "w+", "gb2312")
    report.seek(0, 2)
    fo.write("<?xml version=\"1.0\"  encoding=\"utf-8\"?>\n")
    fo.write("<电子文件信息>\n")
    type = "0"
    xmdd = input(colorama.Fore.LIGHTWHITE_EX + ("项目地点:"))
    global jsdw, djdw, jldw, kcdw, yjdw, lxpzdw, lxpzwh, sjdw
    global ghxkzh, ydghxkzh, ydxkzh, sgxkzh
    jsdw = input(colorama.Fore.LIGHTWHITE_EX + ("建设单位:"))
    djdw = ''
    jldw = input(colorama.Fore.LIGHTWHITE_EX + ("监理单位:"))
    kcdw = input(colorama.Fore.LIGHTWHITE_EX + ("勘察单位:"))
    sjdw = input(colorama.Fore.LIGHTWHITE_EX + ("设计单位:"))
    print('\n')
    yjdw = jsdw
    lxpzdw = ""
    lxpzwh = ghxkzh = ydghxkzh = ydxkzh = sgxkzh = ""
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
    '''
    print(colorama.Fore.LIGHTRED_EX +
          "--------------------------------------------------------\n\n")
    print(colorama.Fore.LIGHTGREEN_EX + "项目概况录入完毕，按回车继续录入单位工程的内容...")
    input(colorama.Fore.LIGHTWHITE_EX + (""))
    os.system('cls')
    '''


def dwgc():
    fo = codecs.open(xmmc + '\\' + xmmc + '.xml', "r+", "utf-8")
    fo.seek(0, 2)
    report = codecs.open(xmmc + '\\' + "report", "r+", "gb2312")
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
    mj = ""
    bz = ""
    key = str(uuid.uuid4()).upper()
    global gcmc, gcdd, sgdw, kgrq, jgrq, gcys, gcjs, gd, jzmj, ydmj, dscs, dzcs
    global gcdh, dscs, dxcs, jclx, jglx, dwgcid, zdjh_
    # dwgcid = xmid
    print(colorama.Fore.RESET, end="")
    # gcmc = input(colorama.Fore.LIGHTWHITE_EX + ("工程名称:"))
    gcmc = xmmc
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
    kgrq_ = input(colorama.Fore.LIGHTWHITE_EX + ("开工日期(YYYYMMDD):"))
    if not kgrq_.isdigit() or len(kgrq_) < 8:
        kgrq = ""
    else:
        kgrq = kgrq_[:4] + '/' + kgrq_[4:6] + '/' + kgrq_[6:8]
    try:
        t = time.strptime(kgrq, '%Y/%m/%d')
    except ValueError:
        kgrq = ""
    jgrq_ = input(colorama.Fore.LIGHTWHITE_EX + ("竣工日期(YYYYMMDD):"))
    if not jgrq_.isdigit() or len(jgrq_) < 8:
        jgrq = ""
    else:
        jgrq = jgrq_[:4] + '/' + jgrq_[4:6] + '/' + jgrq_[6:8]
    try:
        t = time.strptime(jgrq, '%Y/%m/%d')
    except ValueError:
        jgrq = ""
    '''
    gcys = input(colorama.Fore.LIGHTWHITE_EX + ("工程预算:"))
    if not gcys.isdigit():
        gcys = 0
    gcjs = input(colorama.Fore.LIGHTWHITE_EX + ("工程决算:"))
    if not gcjs.isdigit():
        gcjs = 0
    '''
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
    report.write("工程录入基本信息:\n")
    report.write("========================================================\n")
    report.write("项目名称:%s\n" % xmmc)
    report.write("项目地点:%s\n" % xmdd)
    report.write("建设单位:%s\n" % jsdw)
    report.write("地基单位:%s\n" % djdw)
    report.write("监理单位:%s\n" % jldw)
    report.write("勘察单位:%s\n" % kcdw)
    report.write("设计单位:%s\n" % sjdw)
    report.write("移交单位:%s\n" % yjdw)
    report.write("立项批准单位:%s\n" % lxpzdw)
    report.write("立项批准文号:%s\n" % lxpzwh)
    report.write("规划许可证号:%s\n" % ghxkzh)
    report.write("用地规划许可证号:%s\n" % ydghxkzh)
    report.write("用地许可证号:%s\n" % ydxkzh)
    report.write("施工许可证号:%s\n" % sgxkzh)
    report.write("工程名称:%s\n" % gcmc)
    report.write("工程地点:%s\n" % gcdd)
    report.write("工程档号:%s\n" % gcdh)
    report.write("施工单位:%s\n" % sgdw)
    report.write("开工日期:%s\n" % kgrq)
    report.write("竣工日期:%s\n" % jgrq)
    report.write("工程预算:%s\n" % gcys)
    report.write("工程决算:%s\n" % gcjs)
    report.write("高度:%s\n" % gd)
    report.write("建筑面积:%s\n" % jzmj)
    report.write("用地面积:%s\n" % ydmj)
    report.write("地上层数:%s\n" % dscs)
    report.write("地下层数:%s\n" % dxcs)
    report.write("基础类型:%s\n" % jclx)
    report.write("结构类型:%s\n" % jglx)
    report.write(
        "--------------------------------------------------------\n\n")
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
    nr = ''
    with open("yjnr.txt", 'r', encoding='utf-8') as f:
        for line in f:
            id += 1
            nr += "              " + line % (str(id), dwgcid, id2, gcmc,
                                             str(uuid.uuid4()).upper())
            id2 = id
    fo.write(nr)
    global sid
    sid = id
    fo.write("\n          </移交目录>\n")
    fo.flush()
    fo.close()


def aj():
    fo = codecs.open(xmmc + '\\' + xmmc + '.xml', "r+", "utf-8")
    fo.seek(0, 2)
    report = codecs.open(xmmc + '\\' + "report", "r+", "gb2312")
    report.seek(0, 2)
    report.write("文件分段列表:\n")
    report.write("========================================================\n")
    report.write("文件名:		起始页码:		结束页码:\n")
    report.write("--------------------------------------------------------\n")
    global table
    table = PrettyTable(["文件名","起始页码","终止页码","PDF状态","形成时间","文图号"])
    # table.set_style(pt.PLAIN_COLUMNS)
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
    mj = "1"
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
    mj = "1"
    os.system("cls")
    try:
        with open(xmmc + '.csv') as f:
            colorama.init(autoreset=True)
            fo = codecs.open(xmmc + '\\' + xmmc + '.xml', "r+", "utf-8")
            fo.seek(0, 2)
            report = codecs.open(xmmc + '\\' + "report", "r+", "gb2312")
            report.seek(0, 2)
            ajh = id_aj
            count = 0
            count_aj = 0
            no1st = 0
            ajtm_ = ''
            try:
                shutil.rmtree(xmmc + '\\' + xmmc)
            except:
                pass
            for i in f.readlines():
                line = i.strip()
                line = ''.join(line.split())
                line = line.replace(',,,', '')
                if ',' in line:
                    a = line.split(',')
                    try:
                        if a[1] == '0':
                            ajtm_ = a[0]
                        else:
                            count += 1
                        if a[1] == '1':
                            if not no1st == 0:
                                fo.write("          </案卷>\n")
                            zdjh += 1
                            no1st += 1
                            ajtm = gcmc + ajtm_
                            print(
                                colorama.Fore.LIGHTYELLOW_EX +"          <案卷 Id=\"%s\" SingleProjectId=\"%s\" Ajh=\"%s\" Zdjh=\"%s\" Ajtm=\"%s\" Bzdw=\"%s\" Bzrq=\"%s\" Zrz=\"%s\" Gg=\"%s\" JnwjQssj=\"%s\" JnwjZzsj=\"%s\" Bgqx=\"%s\" Mj=\"%s\" Ljr=\"%s\" Ljsj=\"%s\" Ztc=\"%s\" Fz=\"%s\" Key=\"%s\">\n" %
                                (count_aj, singleprojectid, ajh, zdjh, ajtm, bzdw, bzrq, zrz, gg, jnwjqssj, jnwjzzsj, bgqx, mj, ljr, ljsj, ztc, fz, str(
                                    uuid.uuid4()).upper()))
                            fo.write(
                                "          <案卷 Id=\"%s\" SingleProjectId=\"%s\" Ajh=\"%s\" Zdjh=\"%s\" Ajtm=\"%s\" Bzdw=\"%s\" Bzrq=\"%s\" Zrz=\"%s\" Gg=\"%s\" JnwjQssj=\"%s\" JnwjZzsj=\"%s\" Bgqx=\"%s\" Mj=\"%s\" Ljr=\"%s\" Ljsj=\"%s\" Ztc=\"%s\" Fz=\"%s\" Key=\"%s\">\n" %
                                (count_aj, singleprojectid, ajh, zdjh, ajtm, bzdw, bzrq, zrz, gg, jnwjqssj, jnwjzzsj, bgqx, mj, ljr, ljsj, ztc, fz, str(
                                    uuid.uuid4()).upper()))
                            ajtm_ = ''
                            # time.sleep(2)
                    except BaseException:
                        pass
                    try:
                        if a[1] == '0':
                            count_aj += 1
                            table.add_row(['','','','','',''])
                            table.add_row(['第'+str(count_aj)+'卷','','','','',''])
                            table.add_row(['-----','','','','',''])
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
                    report.write(
                        "%s		%s 			%s\n" %
                        (str(count) + '.pdf', qsy, zzy))
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
                        print(colorama.Fore.LIGHTCYAN_EX +"              <文件 Id=\"%s\" FileId=\"%s\" SingleProjectId=\"%s\" SingleProjectRevceiveListId=\"%s\" Dh=\"%s\" Wjtm=\"%s\" Wth=\"%s\" Zrz=\"%s\" Bgqx=\"%s\" Mj=\"%s\" Xcsj=\"%s\" Ztlx=\"%s\" Qsy=\"%s\" Zzy=\"%s\" Sl=\"%s\" Wb=\"%s\" Gg=\"%s\" Ty=\"%s\" Ztc=\"%s\" Fz=\"%s\" ERecordPath=\"%s\" ERecordSize=\"%s\" Md5=\"%s\" CceptStatus=\"%s\" Key=\"%s\" />\n" %
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
                        # time.sleep(1)
                    except BaseException:
                        pass
                    report.write(
                        "--------------------------------------------------------\n")
                    try:
                        os.mkdir(xmmc + '\\' + xmmc)
                    except BaseException:
                        pass
                    try:
                        if int(ab) > 0:
                            reader = PdfFileReader(str(count_aj) + '.pdf')
                            writer = PdfFileWriter()
                            with open(xmmc + '\\' + str(count) + '.pdf', 'wb') as wstream:
                                for page in range(int(qsy) - 1, int(zzy)):
                                    temp = reader.getPage(page)
                                    writer.addPage(temp)
                                writer.write(wstream)
                            shutil.move(wstream.name, xmmc + '\\' + xmmc)
                            isok = '正常'
                            # print ("pdf done")
                    except BaseException:
                        # print ("%s.pdf error!\n"%str(count))
                        isok='错误'
                        # pass
                    table.add_row([str(count) + '.pdf', qsy, zzy,isok,xcsj,wth])
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
    report = codecs.open(xmmc + '\\' + "report", "r+", "gb2312")
    report.seek(0, 2)
    fo.write("      </单位工程>\n")
    fo.write("  </项目>\n")
    fo.write("</电子文件信息>")
    print(colorama.Back.RESET, end="")
    fo.flush()
    report.flush()
    fo.close()
    report.close()

    
if __name__ == "__main__":
    colorama.init()
    tb()
    xm()
    dwgc()
    yjnr()
    aj()
    wb()
    os.remove(xmmc + '\\report')
    # time.sleep(1)
    # os.system('cls')
    print ("文件分段列表")
    # result = table.get_string(hrules=ALL)
    print (table)
    # print (result)
    '''
    html_table = table.get_html_string()
    print (html_table)
    with open(r'a.html','w+') as f:
        print(html_table, file=f)
        webbrowser.open('a.html')
    time.sleep(1)
    os.remove('a.html')
    '''
    print('\nOkey!')
