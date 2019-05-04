# -*- coding: UTF-8 -*-

import time
import datetime
import os
import sys
import codecs
import colorama
import uuid
import random
import shutil
import re
from lxml import etree
import xlsxwriter
from PyPDF2 import PdfFileReader, PdfFileWriter
import tkinter as tk
from tkinter import filedialog
import traceback
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def xm(fn):
    try:
        name = os.path.splitext(fn)
        fn1 = name[0]
    except:
        fn1 = fn
    bz = ""
    key = str(uuid.uuid4()).upper()
    key = ""
    global xmmc, xmdd, xmid
    xmmc = fn1
    if os.path.exists(xmmc + ".xlsx"):
        try:
            os.system("xlsx2csv.py -c GBK %s.xlsx %s.csv " % (xmmc, xmmc))
        except:
            pass
    if not os.path.exists(xmmc + ".csv"):
        print("%s does not exist！" % (xmmc + ".xlsx"), end="")
        sys.exit()
    xmid = 0
    if not os.path.exists(xmmc):
        os.mkdir(xmmc)
    fo = codecs.open(xmmc + "\\" + xmmc + ".xml", "w+", "utf-8")
    fo.seek(0, 2)
    fo.write('<?xml version="1.0"  encoding="utf-8"?>\n')
    fo.write("<电子文件信息>\n")
    type = "0"
    global xjdd, jsdw, djdw, jldw, kcdw, yjdw, lxpzdw, lxpzwh, sjdw
    global ghxkzh, ydghxkzh, ydxkzh, sgxkzh
    with open(xmmc + ".csv") as f:
        for i in f.readlines():
            line = i.strip()
            line = "".join(line.split())
            a = line.split(",")
            try:
                if a[1] == ":":
                    if a[0] == "项目地点":
                        xmdd = a[2]
                    elif a[0] == "建设单位":
                        jsdw = a[2]
                    elif a[0] == "施工单位":
                        sgdw = a[2]
                    elif a[0] == "监理单位":
                        jldw = a[2]
                    elif a[0] == "勘察单位":
                        kcdw = a[2]
                    elif a[0] == "设计单位":
                        sjdw = a[2]
                    elif a[0] == "立项批准单位":
                        lxpzdw = a[2]
                    elif a[0] == "立项批准文号":
                        lxpzwh = a[2]
                    elif a[0] == "规划许可证号":
                        ghxkzh = a[2]
                    elif a[0] == "用地规划许可证号":
                        ydghxkzh = a[2]
                    elif a[0] == "施工许可证号":
                        sgxkzh = a[2]
                    elif a[0] == "单体序号":
                        dwgcid = a[2]
                    elif a[0] == "工程档号":
                        gcdh = a[2]
                    elif a[0] == "总登记号":
                        zdjh_ = a[2]
                    elif a[0] == "开工日期":
                        kgrq_ = a[2]
                    elif a[0] == "竣工日期":
                        jgrq_ = a[2]
                    else:
                        pass
                else:
                    pass
            except:
                pass

    djdw = ""
    yjdw = jsdw
    ydxkzh = ""
    print("\n")
    bz = ""
    fo.write(
        u'  <项目 Id="%s" Type="%s" Xmmc="%s" Xmdd="%s" Jsdw="%s" Djdw="%s" Lxpzdw="%s" Sjdw="%s" Jldw="%s" Kcdw="%s" Lxpzwh="%s" Ghxkzh="%s" Ydghxkzh="%s" Ydxkzh="%s" Sgxkzh="%s" Yjdw="%s" Bz="%s" Key="%s">\n'
        % (
            xmid,
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
            key,
        )
    )
    fo.flush()
    fo.close()


def dwgc():
    fo = codecs.open(xmmc + "\\" + xmmc + ".xml", "r+", "utf-8")
    fo.seek(0, 2)
    colorama.init()
    zs = ""
    projectid = xmid
    bgqx = ""
    mj = "0"
    bz = ""
    key = str(uuid.uuid4()).upper()
    key = ""
    global gcmc, gcdd, sgdw, kgrq, jgrq, gcys, gcjs, gd, jzmj, ydmj, dscs, dzcs
    global gcdh, dscs, dxcs, jclx, jglx, dwgcid, zdjh_
    print(colorama.Fore.RESET, end="")
    gcmc = xmmc
    with open(xmmc + ".csv") as f:
        for i in f.readlines():
            line = i.strip()
            line = "".join(line.split())
            a = line.split(",")
            try:
                if a[1] == ":":
                    if a[0] == "项目地点":
                        xmdd = a[2]
                    elif a[0] == "建设单位":
                        jsdw = a[2]
                    elif a[0] == "施工单位":
                        sgdw = a[2]
                    elif a[0] == "监理单位":
                        jldw = a[2]
                    elif a[0] == "勘察单位":
                        kcdw = a[2]
                    elif a[0] == "设计单位":
                        sjdw = a[2]
                    elif a[0] == "立项批准单位":
                        lxpzdw = a[2]
                    elif a[0] == "立项批准文号":
                        lxpzwh = a[2]
                    elif a[0] == "规划许可证号":
                        ghxkzh = a[2]
                    elif a[0] == "用地规划许可证号":
                        ydghxkzh = a[2]
                    elif a[0] == "施工许可证号":
                        sgxkzh = a[2]
                    elif a[0] == "单体序号":
                        dwgcid = a[2]
                    elif a[0] == "工程档号":
                        gcdh = a[2]
                    elif a[0] == "总登记号":
                        zdjh_ = a[2]
                    elif a[0] == "开工日期":
                        kgrq_ = a[2]
                    elif a[0] == "竣工日期":
                        jgrq_ = a[2]
                    else:
                        pass
                else:
                    pass
            except:
                pass

    if not dwgcid.isdigit():
        dwgcid = 1
    if not zdjh_.isdigit():
        zdjh_ = 0
    zdjh_ = int(zdjh_)
    zdjh_ -= 1
    gcdd = xmdd
    if not kgrq_.isdigit() or len(kgrq_) < 8:
        kgrq = ""
    else:
        kgrq = kgrq_[:4] + "/" + kgrq_[4:6] + "/" + kgrq_[6:8]
    try:
        t = time.strptime(kgrq, "%Y/%m/%d")
    except ValueError:
        kgrq = ""
    if not jgrq_.isdigit() or len(jgrq_) < 8:
        jgrq = ""
    else:
        jgrq = jgrq_[:4] + "/" + jgrq_[4:6] + "/" + jgrq_[6:8]
    try:
        t = time.strptime(jgrq, "%Y/%m/%d")
    except ValueError:
        jgrq = ""
    gcdd = xmdd
    gcys = 0
    gcjs = 0
    jzmj = ydmj = "0"
    gd = zs = "0"
    dscs = dxcs = "0"
    type = "0"
    jclx = jglx = ""
    print("      项目名称         ：" + xmmc + "\n")
    print("      项目地点         : " + xmdd + "\n")
    print("      建设单位         : " + jsdw + "\n")
    print("      施工单位         : " + sgdw + "\n")
    print("      监理单位         : " + jldw + "\n")
    print("      勘察单位         : " + kcdw + "\n")
    print("      设计单位         : " + sjdw + "\n")
    print("      立项批准单位     : " + lxpzdw + "\n")
    print("      立项批准文号     : " + lxpzwh + "\n")
    print("      规划许可证号     : " + ghxkzh + "\n")
    print("      用地规划许可证号 : " + ydghxkzh + "\n")
    print("      施工许可证号     : " + sgxkzh + "\n")
    print("      单体序号         : " + str(dwgcid) + "\n")
    print("      工程档号         : " + gcdh + "\n")
    # print('      总登记号         : ' + str(zdjh_+1)+'\n')
    print("      开工日期         : " + kgrq + "\n")
    print("      竣工日期         : " + jgrq + "\n")
    print("=" * 100 + "\n")
    fo.write(
        '      <单位工程 Jb="" Hz="" Cd="0" Kd="0" Kj="0" Ks="0" Jk="" Gd="%s" Jzmj="%s" Ydmj="%s" Dscs="%s" Dxcs="%s" Jclx="%s" Jglx="%s" Kgrq="%s" Jgrq="%s" Zs="%s" Gcys="%s" Gcjs="%s" Id="%s" ProjectId="%s" Type="%s" Gcmc="%s" Gcdd="%s" Gcdh="%s" Bgqx="%s" Mj="%s" Jsdw="%s" Djdw="%s" Sgdw="%s" Lxpzdw="%s" Sjdw="%s" Jldw="%s" Kcdw="%s" Lxpzwh="%s" Ghxkzh="%s" Ydghxkzh="%s" Ydxkzh="%s" Sgxkzh="%s" Yjdw="%s" Bz="%s" Key="%s" >\n'
        % (
            gd,
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
            key,
        )
    )

    fo.flush()

    fo.close()


def yjnr():
    fo = codecs.open(xmmc + "\\" + xmmc + ".xml", "r+", "utf-8")
    fo.seek(0, 2)
    fo.write("          <移交目录>\n")
    id = int((random.random() * 100000))
    id2 = 1
    global parentid
    parentid = 0
    line1 = (
        '              <移交内容 Id="%s" ReceiveListId="%s" SingleProjectId="%s" ParentId="0" SerialNumber="" Name="%s" Sequence="0" Key="%s" />\n'
    )
    line2 = (
        '              <移交内容 Id="%s" ReceiveListId="%s" SingleProjectId="%s" ParentId="%s" SerialNumber="" Name="%s" Sequence="0" Key="%s" />'
    )
    try:
        with open(xmmc + ".csv") as f:
            newcsv = ""
            for i in f.readlines():
                line = i.strip()
                line = "".join(line.split())
                a = line.split(",")
                if a[1] != "":
                    a = ",".join(a) + "\n"
                    newcsv += a
        with open(xmmc + ".csv", "w+", encoding="gbk") as f:
            f.write(newcsv)
    except:
        pass
    try:
        with open(xmmc + ".csv") as f:
            colorama.init(autoreset=True)
            fo = codecs.open(xmmc + "\\" + xmmc + ".xml", "r+", "utf-8")
            fo.seek(0, 2)
            try:
                shutil.rmtree(xmmc + "\\" + xmmc)
            except:
                pass

            for i in f.readlines():
                line = i.strip()
                line = "".join(line.split())
                dt = re.compile(r",,,,,+")
                k = re.search(dt, line)
                name = ""
                if k:
                    line = dt.sub("", line)
                if "," in line:
                    a = line.split(",")
                    try:
                        try:
                            int(a[1])
                            name = a[0]
                        except:
                            continue
                        if a[1] == "0":
                            fo.write(
                                line1
                                % (str(id), str(id2), dwgcid, name, str(uuid.uuid4()))
                            )
                            parentid = id
                            id += 1
                            id2 += 1
                        else:
                            fo.write(
                                line2
                                % (
                                    str(id),
                                    str(id2),
                                    dwgcid,
                                    parentid,
                                    name,
                                    str(uuid.uuid4()),
                                )
                            )
                            id += 1
                            id2 += 1
                            if not a[6] == "over":
                                fo.write("\n")
                    except BaseException:
                        pass
    except:
        pass
    global sid
    sid = id
    fo.write("\n          </移交目录>\n")
    fo.flush()
    fo.close()
    shutil.copy(xmmc + "\\" + xmmc + ".xml", xmmc + "\\" + xmmc + "1.xml")


def aj():
    fo = codecs.open(xmmc + "\\" + xmmc + ".xml", "r+", "utf-8")
    fo.seek(0, 2)
    global wjyc
    wjyc = ""
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
    ljr = "李佳靖"
    zrz = jsdw
    ajzrz = jsdw
    jnwjqssj = jnwjzzsj = datenow_
    jnwjqssj = jnwjzzsj = ""
    bgqx = "0"
    mj = "0"
    tmp1 = 1
    try:
        with open(xmmc + ".csv") as f:
            colorama.init(autoreset=True)
            fo = codecs.open(xmmc + "\\" + xmmc + ".xml", "r+", "utf-8")
            fo.seek(0, 2)
            count = 0
            count_aj = 0
            no1st = 0
            ajtm_ = ""
            test_zzy = 0
            test_zzy1 = 0
            name_1 = ""
            try:
                shutil.rmtree(xmmc + "\\" + xmmc)
            except:
                pass
            for i in f.readlines():
                line = i.strip()
                line = "".join(line.split())
                dt = re.compile(r",,,,,+")
                k = re.search(dt, line)
                if k:
                    line = dt.sub("", line)
                if "," in line:
                    a = line.split(",")
                    try:
                        try:
                            int(a[1])
                        except:
                            continue
                        if a[1] == "0":
                            ajtm_ = a[0]
                            print(
                                colorama.Fore.LIGHTBLUE_EX
                                + "  \n"
                                + str(tmp1).zfill(2)
                                + "  "
                                + a[0]
                                + "\n"
                            )
                            tmp1 += 1
                            wjyc += "***" + a[0] + "***</b><br>"
                        else:
                            count += 1
                        if a[1] == "1":
                            if not no1st == 0:
                                fo.write("          </案卷>\n")
                            zdjh += 1
                            zdjh__ = ""
                            no1st += 1
                            ajtm = gcmc + ajtm_

                            fo.write(
                                '          <案卷 Id="%s" SingleProjectId="%s" Ajh="%s" Zdjh="%s" Ajtm="%s" Bzdw="%s" Bzrq="%s" Zrz="%s" Gg="%s" JnwjQssj="%s" JnwjZzsj="%s" Bgqx="%s" Mj="%s" Ljr="%s" Ljsj="%s" Ztc="%s" Fz="%s" Key="%s">\n'
                                % (
                                    count_aj,
                                    singleprojectid,
                                    count_aj,
                                    zdjh__,
                                    ajtm,
                                    bzdw,
                                    bzrq,
                                    ajzrz,
                                    gg,
                                    jnwjqssj,
                                    jnwjzzsj,
                                    bgqx,
                                    mj,
                                    ljr,
                                    ljsj,
                                    ztc,
                                    fz,
                                    str(uuid.uuid4()),
                                )
                            )
                            ajtm_ = ""
                            test_zzy = 0
                    except BaseException:
                        pass
                    try:
                        if a[1] == "0":
                            count_aj += 1
                            continue
                    except BaseException:
                        pass
                    try:
                        qsy = str(int(a[1]))
                    except BaseException:
                        qsy = "错误"
                        isok = "错误"
                    try:
                        zzy = str(int(a[2]))
                        if int(zzy) - int(qsy) < 0:
                            zzy = "错误"
                    except BaseException:
                        zzy = "错误"
                        isok = "错误"
                    if not int(a[1]) - 1 == int(test_zzy):
                        print(
                            colorama.Fore.LIGHTRED_EX
                            + " " * 42
                            + "终止页 {:<} 错误".format(str(test_zzy))
                        )
                    test_zzy = a[2]
                    pdfcut = "".join(zzy) + ","
                    try:
                        xcsj_ = str(a[3])
                        if xcsj_.isdigit() and len(xcsj_) > 7:
                            xcsj = xcsj_[:4] + "/" + xcsj_[4:6] + "/" + xcsj_[6:8]
                        else:
                            xcsj = ""
                    except:
                        pass
                    try:
                        t = time.strptime(xcsj, "%Y/%m/%d")
                    except ValueError:
                        xcsj = ""
                    try:
                        ab = str(int(a[2]) - int(a[1]) + 1)
                        if int(ab) > 0:
                            ab = ab
                        else:
                            ab = "错误"
                            isok = "错误"
                    except BaseException:
                        ab = "错误"
                        isok = "错误"
                    try:
                        wth = a[4]
                    except BaseException:
                        wth = sgdw
                    try:
                        zrz = a[5]
                        if zrz == "":
                            zrz = jsdw
                    except BaseException:
                        zrz = jsdw
                    try:
                        ajzrz = a[5]
                        if ajzrz == "":
                            ajzrz = jsdw
                    except BaseException:
                        ajzrz = jsdw
                    try:
                        with open(
                            xmmc + "\\" + xmmc + "1.xml", "r", encoding="utf-8"
                        ) as f1:
                            searchName = 'Name="' + a[0] + '"'
                            searchName = 'Name="' + a[0]
                            cp = re.compile(searchName)
                            cp1 = re.compile(r'\bId="([0-9]*)"')
                            for line in f1:
                                k = re.search(cp, line)
                                if k:
                                    l = re.search(cp1, line)
                                    singleprojectrevceivelistid = l.group(1)
                    except:
                        pass
                    try:
                        wjyc += line + "<br>"
                        fo.write(
                            '              <文件 Id="%s" FileId="%s" SingleProjectId="%s" SingleProjectRevceiveListId="%s" Dh="%s" Wjtm="%s" Wth="%s" Zrz="%s" Bgqx="%s" Mj="%s" Xcsj="%s" Ztlx="%s" Qsy="%s" Zzy="%s" Sl="%s" Wb="%s" Gg="%s" Ty="%s" Ztc="%s" Fz="%s" ERecordPath="%s" ERecordSize="%s" Md5="%s" CceptStatus="%s" Key="%s" />\n'
                            % (
                                count,
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
                                gcmc + "\\" + str(count) + ".pdf",
                                erecordsize,
                                md5,
                                cceptstatus,
                                str(uuid.uuid4()),
                            )
                        )
                    except BaseException:
                        pass
                    try:
                        os.mkdir(xmmc + "\\" + xmmc)
                    except BaseException:
                        pass

                    try:
                        if int(ab) > 0:
                            reader = PdfFileReader(str(count_aj) + ".pdf")
                            writer = PdfFileWriter()
                            with open(
                                xmmc + "\\" + str(count) + ".pdf", "wb"
                            ) as wstream:
                                for page in range(int(qsy) - 1, int(zzy)):
                                    temp = reader.getPage(page)
                                    writer.addPage(temp)
                                writer.write(wstream)
                            x = PdfFileReader(wstream.name)
                            isdouble = False
                            for i in range(len(x.pages)):
                                try:
                                    x.pages[i]["/Resources"]["/Font"]
                                    isdouble = True
                                    break
                                except:
                                    pass

                            if not isdouble:
                                print(
                                    colorama.Fore.LIGHTGREEN_EX
                                    + " " * 10
                                    + "非双层PDF   : "
                                    + "{:\u3000<30} {:>10}".format(
                                        a[0], str(count) + ".pdf"
                                    )
                                )

                            shutil.move(wstream.name, xmmc + "\\" + xmmc)
                            isok = ""
                    except BaseException:
                        isok = "错误"
                        logger.error(
                            "PDF文件错误 : "
                            + "{:<10}|{:\u3000<30} ".format(str(count) + ".pdf", a[0])
                        )
                    xcsj = ""
    except BaseException:
        pass
    try:
        if count > 1:
            fo.write("          </案卷>\n")
    except BaseException:
        pass
    fo.flush()
    fo.close()


def wb():
    fo = codecs.open(xmmc + "\\" + xmmc + ".xml", "r+", "utf-8")
    fo.seek(0, 2)
    fo.write("      </单位工程>\n")
    fo.write("  </项目>\n")
    fo.write("</电子文件信息>")
    print(colorama.Back.RESET, end="")
    fo.flush()
    fo.close()


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.CRITICAL)
    os.system("cls")
    colorama.init()
    root = tk.Tk()
    root.withdraw()
    fn = filedialog.askopenfilename(filetypes=(("Excel源", "*.xlsx"), ("csv源", "*.csv")))
    oschdir = os.path.dirname(fn)
    os.chdir(oschdir)
    fn = fn.split("/")[-1]
    try:
        xm(fn)
    except:
        print("Parameter error!")
        traceback.print_exec()
        sys.exit()
    dwgc()
    yjnr()
    aj()
    wb()
    os.remove(xmmc + "\\" + xmmc + "1.xml")
