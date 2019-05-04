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
from PyPDF2 import PdfFileReader, PdfFileWriter

# import traceback


class ProgressBar():
    def __init__(self, width=50):
        self.pointer = 0
        self.width = width

    def __call__(self, x):
        self.pointer = int(self.width * (x / 100.0))
        return "|" + "#" * self.pointer + "-" * (self.width - self.pointer) + \
               "|\n %d 生成目录\n\n" % int(x)


def tb():
    # 头部
    os.system('cls')
    print(colorama.Fore.LIGHTYELLOW_EX + (pyfiglet.figlet_format(
        "XinXinDangAn", font="small")))
    print(colorama.Fore.LIGHTYELLOW_EX + "城建档案XML目录录入系统\n\nCopyright 2017\n四川欣兴档案管理咨询有限公司\nAll rights reserved.")
    print(colorama.Back.RESET, end="")
    print(colorama.Fore.LIGHTWHITE_EX +
          "--------------------------------------------------------\n\n")


def xm():
    # 项目
    print(colorama.Fore.LIGHTWHITE_EX + colorama.Back.LIGHTBLUE_EX +
          "请按条目输入项目概况的内容:")
    print(colorama.Back.RESET, end="")
    print(colorama.Fore.LIGHTRED_EX +
          "========================================================\n")
    print(colorama.Fore.RESET, end="")
    bz = ""
    key = str(uuid.uuid4()).upper()
    global xmmc, xmdd, xmid
    xmid = "1"
    while True:
        xmmc = input(colorama.Fore.LIGHTWHITE_EX + ("项目名称:"))
        if xmmc:
            break
        else:
            print("项目名称可是必须填的！\n")
    if not os.path.exists(xmmc):
        os.mkdir(xmmc)
    fo = codecs.open(xmmc + '\\' + "info.xml", "w+", "utf-8")
    fo.seek(0, 2)
    report = codecs.open(xmmc + '\\' + "report", "w+", "gb2312")
    report.seek(0, 2)
    fo.write("<?xml version=\"1.0\"  encoding=\"utf-8\"?>\n")
    fo.write("<电子文件信息>\n")
    # type = input(colorama.Fore.LIGHTWHITE_EX+("项目类型:"))
    type = "0"
    xmdd = input(colorama.Fore.LIGHTWHITE_EX + ("项目地点:"))
    global jsdw, djdw, jldw, kcdw, yjdw, lxpzdw, lxpzwh, sjdw
    global ghxkzh, ydghxkzh, ydxkzh, sgxkzh
    jsdw = input(colorama.Fore.LIGHTWHITE_EX + ("建设单位:"))
    # djdw = input(colorama.Fore.LIGHTWHITE_EX + ("代建单位:"))
    djdw = ''
    jldw = input(colorama.Fore.LIGHTWHITE_EX + ("监理单位:"))
    kcdw = input(colorama.Fore.LIGHTWHITE_EX + ("勘察单位:"))
    # sjdw = input(colorama.Fore.LIGHTWHITE_EX+("设计单位:"))
    sjdw = ""
    # yjdw = input(colorama.Fore.LIGHTWHITE_EX + ("移交单位:"))
    yjdw = jsdw
    # lxpzdw = input(colorama.Fore.LIGHTWHITE_EX+("立项批准单位:"))
    lxpzdw = ""
    # lxpzwh = input(colorama.Fore.LIGHTWHITE_EX+("立项批准文号:"))
    # ghxkzh = input(colorama.Fore.LIGHTWHITE_EX+("规划许可证号:"))
    # ydghxkzh = input(colorama.Fore.LIGHTWHITE_EX+("用地规划许可证号:"))
    # ydxkzh = input(colorama.Fore.LIGHTWHITE_EX+("用地许可证号:"))
    # sgxkzh = input(colorama.Fore.LIGHTWHITE_EX+("施工许可证号:"))
    lxpzwh = ghxkzh = ydghxkzh = ydxkzh = sgxkzh = ""
    # bz = input(colorama.Fore.LIGHTWHITE_EX+("备注"))
    bz = ""
    fo.write(
        u"  <项目 Id=\"%s\" Type=\"%s\" Xmmc=\"%s\" Xmdd=\"%s\" Jsdw=\"%s\" Djdw=\"%s\" Lxpzdw=\"%s\" Sjdw=\"%s\" Jldw=\"%s\" Kcdw=\"%s\" Lxpzwh=\"%s\" Ghxkzh=\"%s\" Ydghxkzh=\"%s\" Ydxkzh=\"%s\" Sgxkzh=\"%s\" Yjdw=\"%s\" Bz=\"%s\" Key=\"%s\">\n"
        % (xmid, type, xmmc, xmdd, jsdw, djdw, lxpzdw, sjdw, jldw, kcdw,
           lxpzwh, ghxkzh, ydghxkzh, ydxkzh, sgxkzh, yjdw, bz, key))
    fo.flush()
    report.flush()
    fo.close()
    report.close()
    print(colorama.Fore.LIGHTRED_EX +
          "--------------------------------------------------------\n\n")
    print(colorama.Fore.LIGHTGREEN_EX + "项目概况录入完毕，按回车继续录入单位工程的内容...")
    input(colorama.Fore.LIGHTWHITE_EX + (""))
    os.system('cls')


def dwgc():
    # 单位工程
    fo = codecs.open(xmmc + '\\' + "info.xml", "r+", "utf-8")
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
    global gcdh, dscs, dxcs, jclx, jglx, dwgcid,zdjh_
    dwgcid = "1"
    print(colorama.Fore.RESET, end="")
    # gcmc = input(colorama.Fore.LIGHTWHITE_EX + ("工程名称:"))
    gcmc = xmmc
    gcdh = input(colorama.Fore.LIGHTWHITE_EX + ("工程档号:"))
    zdjh_ = input(colorama.Fore.LIGHTWHITE_EX + ("总登记号:"))
    if not zdjh_.isdigit():
        zdjh_=0
    zdjh_=int(zdjh_)
    zdjh_-=1
    # gcdd = input(colorama.Fore.LIGHTWHITE_EX + ("工程地点:"))
    gcdd = xmdd
    sgdw = input(colorama.Fore.LIGHTWHITE_EX + ("施工单位:"))
    kgrq_ = input(colorama.Fore.LIGHTWHITE_EX + ("开工日期(YYYYMMDD):"))
    if not kgrq_.isdigit() or len(kgrq_)<8:
        kgrq = ""
    else:
        kgrq = kgrq_[:4] + '/' + kgrq_[4:6] + '/' + kgrq_[6:8]
    jgrq_ = input(colorama.Fore.LIGHTWHITE_EX + ("竣工日期(YYYYMMDD):"))
    if not jgrq_.isdigit() or len(jgrq_)<8:
        jgrq = ""
    else:
        jgrq = jgrq_[:4] + '/' + jgrq_[4:6] + '/' + jgrq_[6:8]
    gcys = input(colorama.Fore.LIGHTWHITE_EX + ("工程预算:"))
    if not gcys.isdigit():
        gcys = 0
    gcjs = input(colorama.Fore.LIGHTWHITE_EX + ("工程决算:"))
    if not gcjs.isdigit():
        gcjs = 0
    # jzmj = input(colorama.Fore.LIGHTWHITE_EX+("建筑面积:"))
    # ydmj = input(colorama.Fore.LIGHTWHITE_EX+("用地面积:"))
    jzmj = ydmj = "0"
    # gd = input(colorama.Fore.LIGHTWHITE_EX+("高度:"))
    # zs=input(colorama.Fore.LIGHTWHITE_EX+("幢数"))
    gd = zs = "0"
    # dscs = input(colorama.Fore.LIGHTWHITE_EX+("地上层数:"))
    # dxcs = input(colorama.Fore.LIGHTWHITE_EX+("地下层数:"))
    dscs = dxcs = "0"
    # type = input(colorama.Fore.LIGHTWHITE_EX+("工程类型:"))
    # jclx = input(colorama.Fore.LIGHTWHITE_EX+("基础类型:"))
    # jglx = input(colorama.Fore.LIGHTWHITE_EX+("结构类型:"))
    type = "0"
    jclx = jglx = ""
    fo.write(
        "      <单位工程 Jb=\"\" Hz=\"\" Cd=\"0\" Kd=\"0\" Kj=\"0\" Ks=\"0\" Jk=\"\" Gd=\"%s\" Jzmj=\"%s\" Ydmj=\"%s\" Dscs=\"%s\" Dxcs=\"%s\" Jclx=\"%s\" Jglx=\"%s\" Kgrq=\"%s\" Jgrq=\"%s\" Zs=\"%s\" Gcys=\"%s\" Gcjs=\"%s\" Id=\"%s\" ProjectId=\"%s\" Type=\"%s\" Gcmc=\"%s\" Gcdd=\"%s\" Gcdh=\"%s\" Bgqx=\"%s\" Mj=\"%s\" Jsdw=\"%s\" Djdw=\"%s\" Sgdw=\"%s\" Lxpzdw=\"%s\" Sjdw=\"%s\" Jldw=\"%s\" Kcdw=\"%s\" Lxpzwh=\"%s\" Ghxkzh=\"%s\" Ydghxkzh=\"%s\" Ydxkzh=\"%s\" Sgxkzh=\"%s\" Yjdw=\"%s\" Bz=\"%s\" Key=\"%s\" >\n"
        % (gd, jzmj, ydmj, dscs, dxcs, jclx, jglx, kgrq, jgrq, zs, gcys, gcjs,
           dwgcid, projectid, type, gcmc, gcdd, gcdh, bgqx, mj, jsdw, djdw,
           sgdw, lxpzdw, sjdw, jldw, kcdw, lxpzwh, ghxkzh, ydghxkzh, ydxkzh,
           sgxkzh, yjdw, bz, key))
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
        "--------------------------------------------------------\n\n\n")
    report.write("移交内容流水:\n")
    report.write("========================================================\n")
    fo.flush()
    report.flush()
    fo.close()
    report.close()
    print(colorama.Fore.LIGHTRED_EX +
          "--------------------------------------------------------\n\n")
    print(colorama.Fore.LIGHTGREEN_EX + "单位工程录入完毕，按回车继续录入移交项目的流水内容...")
    input(colorama.Fore.LIGHTWHITE_EX + (""))
    os.system('cls')


def yjnr():
    # 移交目录
    fo = codecs.open(xmmc + '\\' + "info.xml", "r+", "utf-8")
    fo.seek(0, 2)
    fo.write("          <移交目录>\n")
    # 移交内容
    id = int((random.random() * 100000))
    id2 = 0
    for line in codecs.open("yjnr.txt", "r", "utf-8"):
        id += 1
        fo.write("              " + line % (str(id), id2,
                                            str(uuid.uuid4()).upper()))
        id2 = id
    # /移交目录
    global sid
    sid = id
    fo.write("\n")
    fo.write("          </移交目录>\n")
    fo.flush()
    fo.close()


def aj():
    # 案卷
    fo = codecs.open(xmmc + '\\' + "info.xml", "r+", "utf-8")
    fo.seek(0, 2)
    report = codecs.open(xmmc + '\\' + "report", "r+", "gb2312")
    report.seek(0, 2)
    report.write("文件分段列表:\n")
    report.write("========================================================\n")
    report.write("文件名:		起始页码:		结束页码:\n")
    report.write("--------------------------------------------------------\n")
    id_wj = 1
    id_aj = 1
    # print(colorama.Fore.RESET, end="")
    # print(colorama.Fore.LIGHTWHITE_EX + colorama.Back.LIGHTBLUE_EX +
    #       "请输入所有案卷的通用数据:")
    # print(colorama.Back.RESET, end="")
    # print(colorama.Fore.LIGHTRED_EX +
    #       "========================================================\n")
    # colorama.init()
    singleprojectid = dwgcid
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
    # ljsj = input(colorama.Fore.LIGHTWHITE_EX+("案卷立卷时间:"))
    # bzrq = input(colorama.Fore.LIGHTWHITE_EX+("案卷编制日期:"))
    # ljr = input(colorama.Fore.LIGHTWHITE_EX + ("案卷立卷人:"))
    # zrz = input(colorama.Fore.LIGHTWHITE_EX + ("案卷责任人:"))
    ljr = '杨颂'
    zrz = jsdw
    # jnwjqssj = input(colorama.Fore.LIGHTWHITE_EX+("卷内文件起始时间:"))
    # jnwjzzsj = input(colorama.Fore.LIGHTWHITE_EX+("卷内文件终止时间:"))
    jnwjqssj = jnwjzzsj = datenow_
    jnwjqssj = jnwjzzsj = ""
    # jnwjzzsj=""
    # bgqx = input(colorama.Fore.LIGHTWHITE_EX+("保管期限:"))
    bgqx = "0"
    # mj = input(colorama.Fore.LIGHTWHITE_EX+("密级:"))
    mj = "1"
    fo.flush()
    report.flush()
    fo.close()
    report.close()
    os.system("cls")
    goon = "y"
    while goon != "n":
        colorama.init(autoreset=True)
        fo = codecs.open(xmmc + '\\' + "info.xml", "r+", "utf-8")
        fo.seek(0, 2)
        report = codecs.open(xmmc + '\\' + "report", "r+", "gb2312")
        report.seek(0, 2)
        print(colorama.Fore.LIGHTWHITE_EX + colorama.Back.LIGHTBLUE_EX +
              "请按卷分别输入案卷内容")
        print(colorama.Back.RESET)
        print(colorama.Fore.LIGHTRED_EX +
              "========================================================\n")
        ajh = id_aj
        ajtm_ = input(colorama.Fore.LIGHTWHITE_EX + ("案卷名称:"))
        ajtm = gcmc + ajtm_
        zdjh+=1
        fo.write(
            "          <案卷 Id=\"%s\" SingleProjectId=\"%s\" Ajh=\"%s\" Zdjh=\"%s\" Ajtm=\"%s\" Bzdw=\"%s\" Bzrq=\"%s\" Zrz=\"%s\" Gg=\"%s\" JnwjQssj=\"%s\" JnwjZzsj=\"%s\" Bgqx=\"%s\" Mj=\"%s\" Ljr=\"%s\" Ljsj=\"%s\" Ztc=\"%s\" Fz=\"%s\" Key=\"%s\">\n"
            % (id_aj, singleprojectid, ajh, zdjh, ajtm, bzdw, bzrq, zrz, gg,
               jnwjqssj, jnwjzzsj, bgqx, mj, ljr, ljsj, ztc, fz,
               str(uuid.uuid4()).upper()))
        report.write("%s中的PDF文件列表:\n" % (ajtm))
        report.write(
            "--------------------------------------------------------\n")
        # 文件
        pdfcut = ''
        print("\n")
        print(colorama.Fore.LIGHTWHITE_EX + colorama.Back.LIGHTBLUE_EX +
              (ajtm + "内包含的文件内容"))
        print(colorama.Back.RESET, end="")
        print(colorama.Fore.LIGHTRED_EX +
              "========================================================\n")
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
        wjtm = input(colorama.Fore.LIGHTWHITE_EX + ("文件名称:"))
        print("\n")
        while True:
            try:
                qsy = input(colorama.Fore.LIGHTWHITE_EX + ("开始页码:"))
                print("\n")
                y = int(qsy)
                break
            except ValueError:
                print(colorama.Fore.LIGHTYELLOW_EX + colorama.Back.LIGHTRED_EX
                      + "页码只能是整数！！请重新输入\n")
                print(colorama.Back.RESET, end="")
        while True:
            try:
                zzy = input(colorama.Fore.LIGHTWHITE_EX + ("结束页码:"))
                print("\n")
                y = int(zzy)
                break
            except ValueError:
                print(colorama.Fore.LIGHTYELLOW_EX + colorama.Back.LIGHTRED_EX
                      + "页码只能是整数！！请重新输入")
                print("\n")
                print(colorama.Back.RESET, end="")
        xcsj_ = input(colorama.Fore.LIGHTWHITE_EX + ("文件形成时间(YYYYMMDD):"))
        if xcsj_.isdigit() and len(xcsj_)>7:
            xcsj = xcsj_[:4] + '-' + xcsj_[4:6] + '-' + xcsj_[6:8]
        else:
            xcsj = ""
        # singleprojectrevceivelistid=input(colorama.Fore.LIGHTWHITE_EX+("文件所属内容编号："))
        print(colorama.Fore.LIGHTBLUE_EX +
              "--------------------------------------------------------\n")
        sl = int(zzy) - int(qsy) + 1
        pdfcut += str(zzy) + ','
        while wjtm != "n":
            fo.write(
                "              <文件 Id=\"%s\" FileId=\"%s\" SingleProjectId=\"%s\" SingleProjectRevceiveListId=\"%s\" Dh=\"%s\" Wjtm=\"%s\" Wth=\"%s\" Zrz=\"%s\" Bgqx=\"%s\" Mj=\"%s\" Xcsj=\"%s\" Ztlx=\"%s\" Qsy=\"%s\" Zzy=\"%s\" Sl=\"%s\" Wb=\"%s\" Gg=\"%s\" Ty=\"%s\" Ztc=\"%s\" Fz=\"%s\" ERecordPath=\"%s\" ERecordSize=\"%s\" Md5=\"%s\" CceptStatus=\"%s\" Key=\"%s\" />\n"
                % (id_wj, fileid, singleprojectid, singleprojectrevceivelistid,
                   dh, wjtm, wth, zrz, bgqx, mj, xcsj, ztlx, qsy, zzy, sl, wb,
                   gg, ty, ztc, fz, gcmc + '\\' + str(id_wj) + '.pdf',
                   erecordsize, md5, cceptstatus, str(uuid.uuid4()).upper()))
            report.write("%s		%s 			%s\n" % (str(id_wj) + '.pdf', qsy, zzy))
            # 从id_aj.pdf抽取id_wj.pdf到gcmc\目录里
            try:
                reader = PdfFileReader(str(id_aj) + '.pdf')
                writer = PdfFileWriter()
                with open(xmmc + '\\' + str(id_wj) + '.pdf', 'wb') as wstream:
                    for page in range(int(qsy) - 1, int(zzy)):
                        temp = reader.getPage(page)
                        writer.addPage(temp)
                    writer.write(wstream)
            except:
                # print(traceback.format_exc())
                pass

            id_wj += 1
            wjtm = input(colorama.Fore.LIGHTWHITE_EX + ("文件名称:"))
            print("\n")
            if wjtm != "n":
                while True:
                    try:
                        qsy = input(colorama.Fore.LIGHTWHITE_EX + ("开始页码:"))
                        print("\n")
                        y = int(qsy)
                        break
                    except ValueError:
                        print(colorama.Fore.LIGHTYELLOW_EX +
                              colorama.Back.LIGHTRED_EX + "页码只能是整数！！请重新输入\n")
                        print(colorama.Back.RESET, end="")
                while True:
                    try:
                        zzy = input(colorama.Fore.LIGHTWHITE_EX + ("结束页码:"))
                        print("\n")
                        y = int(zzy)
                        break
                    except ValueError:
                        print(colorama.Fore.LIGHTYELLOW_EX +
                              colorama.Back.LIGHTRED_EX + "页码只能是整数！！请重新输入\n")
                        print(colorama.Back.RESET, end="")
                xcsj_ = input(colorama.Fore.LIGHTWHITE_EX +
                              ("文件形成时间(YYYYMMDD):"))
                if xcsj_.isdigit() and len(xcsj_)>7:
                    xcsj = xcsj_[:4] + '-' + xcsj_[4:6] + '-' + xcsj_[6:8]
                else:
                    xcsj = ""
                # print("\n")
                # singleprojectrevceivelistid=input(colorama.Fore.LIGHTWHITE_EX+("文件所属内容编号："))
                # print("\n")
                print(
                    colorama.Fore.LIGHTBLUE_EX +
                    "--------------------------------------------------------\n"
                )
                sl = int(zzy) - int(qsy) + 1
                pdfcut += str(zzy) + ','
        report.write("\npdf截断序列:\n" + pdfcut + '\n')
        report.write(
            "--------------------------------------------------------\n")
        id_aj += 1
        fo.write("          </案卷>\n")
        fo.flush()
        report.flush()
        fo.close()
        report.close()
        print(colorama.Fore.LIGHTRED_EX +
              "--------------------------------------------------------\n\n")
        goon = input(colorama.Fore.LIGHTGREEN_EX + ("还有其他案卷输入吗？"))
        print(colorama.Fore.LIGHTRED_EX +
              "--------------------------------------------------------\n")
        print(colorama.Fore.LIGHTWHITE_EX + colorama.Back.LIGHTBLUE_EX +
              "本案卷文件信息输入完毕\n\n")
        print(colorama.Back.RESET, end="")
        os.system('cls')


def wb():
    fo = codecs.open(xmmc + '\\' + "info.xml", "r+", "utf-8")
    fo.seek(0, 2)
    report = codecs.open(xmmc + '\\' + "report", "r+", "gb2312")
    report.seek(0, 2)
    # 尾部
    fo.write("      </单位工程>\n")
    fo.write("  </项目>\n")
    fo.write("</电子文件信息>")
    print(colorama.Fore.LIGHTWHITE_EX + colorama.Back.LIGHTBLUE_EX +
          (gcmc + "信息已经录入完成了，正在生成目录..."))
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
    i = 1
    j = 1
    while os.path.isfile("%s" % (xmmc + '\\' + xmmc + ".xml")):
        while os.path.isfile("%s" % (xmmc + '\\' + xmmc + str(i) + ".xml")):
            i += 1
        else:
            j = i
            os.system("copy %s %s" % (xmmc + '\\' + "info.xml",
                                      xmmc + '\\' + xmmc + str(j) + ".xml"))
            os.system("copy %s %s" % (xmmc + '\\' + "report",
                                      xmmc + '\\' + xmmc + str(j) + ".report"))
            break
    else:
        os.system("copy %s %s" % (xmmc + '\\' + "info.xml",
                                  xmmc + '\\' + xmmc + ".xml"))
        os.system("copy %s %s" % (xmmc + '\\' + "report",
                                  xmmc + '\\' + xmmc + ".report"))
    os.system("cls")
    pb = ProgressBar()
    for i in range(101):
        os.system('cls')
        print(pb(i))
        time.sleep(0.0001)
    print(colorama.Fore.LIGHTGREEN_EX + "正在生成报告，请稍候...")
    time.sleep(1)
    os.system("cls")
    print(colorama.Fore.LIGHTGREEN_EX + (pyfiglet.figlet_format(
        "Report", font="train")))
    print(colorama.Fore.RESET)
    os.system("type %s" % (xmmc + '\\' + "report"))
    print("\n\n")
    input(colorama.Fore.LIGHTWHITE_EX + ("完成！回车退出..."))
