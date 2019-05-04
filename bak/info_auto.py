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
from lxml import etree
import xlsxwriter
from prettytable import *
import prettytable
from PyPDF2 import PdfFileReader, PdfFileWriter
import traceback


def tb():
    # os.system('cls')
    print(colorama.Fore.LIGHTYELLOW_EX + (pyfiglet.figlet_format(
        "XinXinDangAn", font="small")))
    print(
        colorama.Fore.LIGHTYELLOW_EX +
        "城建档案XML目录录入系统\n\nCopyright 2017\n四川欣兴档案管理咨询有限公司\nAll rights reserved.")
    print(colorama.Back.RESET, end="")
    print(colorama.Fore.LIGHTWHITE_EX +
          "--------------------------------------------------------\n\n")


def xm(fn):
    try:
        name = os.path.splitext(fn)
        fn1 = name[0]
    except:
        fn1 = fn
    bz = ""
    key = str(uuid.uuid4()).upper()
    global xmmc, xmdd, xmid
    xmmc = fn1

    if os.path.exists(xmmc+'.xlsx'):
        try:
            os.system("xlsx2csv.py -c GBK %s.xlsx %s.csv " % (xmmc, xmmc))
        except:
            pass
    if not os.path.exists(xmmc+'.csv'):
        print('%s does not exist！'%(xmmc+'.xlsx'),end='')
        sys.exit()
    xmid = 0
    if not os.path.exists(xmmc):
        os.mkdir(xmmc)
    fo = codecs.open(xmmc + '\\' + xmmc + '.xml', "w+", "utf-8")
    fo.seek(0, 2)
    report = codecs.open(xmmc + '\\' + "report.html", "w+", "gb2312")
    report.seek(0, 2)
    fo.write("<?xml version=\"1.0\"  encoding=\"utf-8\"?>\n")
    fo.write("<电子文件信息>\n")
    type = "0"
    global xjdd, jsdw, djdw, jldw, kcdw, yjdw, lxpzdw, lxpzwh, sjdw
    global ghxkzh, ydghxkzh, ydxkzh, sgxkzh

    with open(xmmc + '.csv') as f:
        for i in f.readlines():
            line = i.strip()
            line = ''.join(line.split())
            a = line.split(',')
            try:
                if a[1] == ':':
                    if a[0] == '项目地点':
                        xmdd = a[2]
                    elif a[0] == '建设单位':
                        jsdw = a[2]
                    elif a[0] == '施工单位':
                        sgdw = a[2]
                    elif a[0] == '监理单位':
                        jldw = a[2]
                    elif a[0] == '勘察单位':
                        kcdw = a[2]
                    elif a[0] == '设计单位':
                        sjdw = a[2]
                    elif a[0] == '立项批准单位':
                        lxpzdw = a[2]
                    elif a[0] == '立项批准文号':
                        lxpzwh = a[2]
                    elif a[0] == '规划许可证号':
                        ghxkzh = a[2]
                    elif a[0] == '用地规划许可证号':
                        ydghxkzh = a[2]
                    elif a[0] == '施工许可证号':
                        sgxkzh = a[2]
                    elif a[0] == '单体序号':
                        dwgcid = a[2]
                    elif a[0] == '工程档号':
                        gcdh = a[2]
                    elif a[0] == '总登记号':
                        zdjh_ = a[2]
                    elif a[0] == '开工日期':
                        kgrq_ = a[2]
                    elif a[0] == '竣工日期':
                        jgrq_ = a[2]
                    else:
                        pass
                else:
                    pass
            except:
                pass

    djdw = ''
    yjdw = jsdw
    ydxkzh = ''
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
    colorama.init()
    # os.system('cls')
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

    with open(xmmc + '.csv') as f:
        for i in f.readlines():
            line = i.strip()
            line = ''.join(line.split())
            a = line.split(',')
            try:
                if a[1] == ':':
                    if a[0] == '项目地点':
                        xmdd = a[2]
                    elif a[0] == '建设单位':
                        jsdw = a[2]
                    elif a[0] == '施工单位':
                        sgdw = a[2]
                    elif a[0] == '监理单位':
                        jldw = a[2]
                    elif a[0] == '勘察单位':
                        kcdw = a[2]
                    elif a[0] == '设计单位':
                        sjdw = a[2]
                    elif a[0] == '立项批准单位':
                        lxpzdw = a[2]
                    elif a[0] == '立项批准文号':
                        lxpzwh = a[2]
                    elif a[0] == '规划许可证号':
                        ghxkzh = a[2]
                    elif a[0] == '用地规划许可证号':
                        ydghxkzh = a[2]
                    elif a[0] == '施工许可证号':
                        sgxkzh = a[2]
                    elif a[0] == '单体序号':
                        dwgcid = a[2]
                    elif a[0] == '工程档号':
                        gcdh = a[2]
                    elif a[0] == '总登记号':
                        zdjh_ = a[2]
                    elif a[0] == '开工日期':
                        kgrq_ = a[2]
                    elif a[0] == '竣工日期':
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
        kgrq = kgrq_[:4] + '/' + kgrq_[4:6] + '/' + kgrq_[6:8]
    try:
        t = time.strptime(kgrq, '%Y/%m/%d')
    except ValueError:
        kgrq = ""
    if not jgrq_.isdigit() or len(jgrq_) < 8:
        jgrq = ""
    else:
        jgrq = jgrq_[:4] + '/' + jgrq_[4:6] + '/' + jgrq_[6:8]
    try:
        t = time.strptime(jgrq, '%Y/%m/%d')
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
    
    # print('\n')
    print('      项目名称：' + xmmc)
    print('      项目地点:' + xmdd)
    print('      建设单位:' + jsdw)
    print('      施工单位:' + sgdw)
    print('      监理单位:' + jldw)
    print('      勘察单位:' + kcdw)
    print('      设计单位:' + sjdw)
    print('      立项批准单位:' + lxpzdw)
    print('      立项批准文号:' + lxpzwh)
    print('      规划许可证号:' + ghxkzh)
    print('      用地规划许可证号:' + ydghxkzh)
    print('      施工许可证号:' + sgxkzh)
    print('      单体序号:' + str(dwgcid))
    print('      工程档号:' + gcdh)
    print('      总登记号:' + str(zdjh_+1))
    print('      开工日期:' + kgrq)
    print('      竣工日期:' + jgrq)
    print('\n')
    
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
    
    fo.flush()
    report.flush()
    fo.close()


def yjnr():
    fo = codecs.open(xmmc + '\\' + xmmc + '.xml', "r+", "utf-8")
    fo.seek(0, 2)
    fo.write("          <移交目录><!--\n")
    id = int((random.random() * 100000))
    id2 = 0
    onno = '''              <移交内容 Id="146" ReceiveListId="1" SingleProjectId="2" ParentId="0" SerialNumber="" Name="（一）工程准备阶段文件" Sequence="0" Key="" />
              <移交内容 Id="147" ReceiveListId="2" SingleProjectId="2" ParentId="146" SerialNumber="" Name="项目建议书及批复文件，有关立项的会议纪要、领导批示" Sequence="0" Key="" />
              <移交内容 Id="148" ReceiveListId="3" SingleProjectId="2" ParentId="146" SerialNumber="" Name="可行性研究报告、附件及批复文件" Sequence="0" Key="" />
              <移交内容 Id="149" ReceiveListId="4" SingleProjectId="2" ParentId="146" SerialNumber="" Name="专家论证意见、项目评估文件" Sequence="0" Key="" />
              <移交内容 Id="150" ReceiveListId="5" SingleProjectId="2" ParentId="146" SerialNumber="" Name="选址意见书（单）" Sequence="0" Key="" />
              <移交内容 Id="151" ReceiveListId="6" SingleProjectId="2" ParentId="146" SerialNumber="" Name="土地使用证明文件" Sequence="0" Key="" />
              <移交内容 Id="152" ReceiveListId="7" SingleProjectId="2" ParentId="146" SerialNumber="" Name="拆迁安置意见、协议、方案等" Sequence="0" Key="" />
              <移交内容 Id="153" ReceiveListId="8" SingleProjectId="2" ParentId="146" SerialNumber="" Name="建设用地规划许可证" Sequence="0" Key="" />
              <移交内容 Id="154" ReceiveListId="9" SingleProjectId="2" ParentId="146" SerialNumber="" Name="建设工程规划许可证、建设工程施工许可证" Sequence="0" Key="" />
              <移交内容 Id="155" ReceiveListId="10" SingleProjectId="2" ParentId="146" SerialNumber="" Name="工程、水文地质勘察报告" Sequence="0" Key="" />
              <移交内容 Id="156" ReceiveListId="11" SingleProjectId="2" ParentId="146" SerialNumber="" Name="有关行政主管部门审查、审批意见（环境影响评价、防空地下室建设意见书、消防设计审查意见书、白蚁防治意见书及防治合同、防雷设计审查意见书等工程涉及的专业）" Sequence="0" Key="" />
              <移交内容 Id="157" ReceiveListId="12" SingleProjectId="2" ParentId="146" SerialNumber="" Name="施工图设计文件审查合格书及审查报告、建筑节能施工图审查意见书" Sequence="0" Key="" />
              <移交内容 Id="158" ReceiveListId="13" SingleProjectId="2" ParentId="146" SerialNumber="" Name="工程合同（勘察、设计、施工、监理等合同）、中标通知书、质量监督申请表、安全监督申请表" Sequence="0" Key="" />
              <移交内容 Id="159" ReceiveListId="14" SingleProjectId="2" ParentId="146" SerialNumber="" Name="工程概括信息表、建设单位工程项目负责人及现场管理人员名册、监理单位工程项目总监及监理人员名册、施工单位工程项目经理及质量管理人员名册" Sequence="0" Key="" />
              <移交内容 Id="160" ReceiveListId="15" SingleProjectId="2" ParentId="0" SerialNumber="" Name="（二）监理文件" Sequence="0" Key="" />
              <移交内容 Id="161" ReceiveListId="16" SingleProjectId="2" ParentId="160" SerialNumber="" Name="监理规划及实施细则" Sequence="0" Key="" />
              <移交内容 Id="162" ReceiveListId="17" SingleProjectId="2" ParentId="160" SerialNumber="" Name="工程暂停令、复工报审表、延期申请表及审批表" Sequence="0" Key="" />
              <移交内容 Id="163" ReceiveListId="18" SingleProjectId="2" ParentId="160" SerialNumber="" Name="质量事故报告及处理意见" Sequence="0" Key="" />
              <移交内容 Id="164" ReceiveListId="19" SingleProjectId="2" ParentId="160" SerialNumber="" Name="监理工作总结及工程质量评估报告" Sequence="0" Key="" />
              <移交内容 Id="165" ReceiveListId="20" SingleProjectId="2" ParentId="0" SerialNumber="" Name="（三）施工文件" Sequence="0" Key="" />
              <移交内容 Id="166" ReceiveListId="21" SingleProjectId="2" ParentId="165" SerialNumber="" Name="桩基工程" Sequence="0" Key="" />
              <移交内容 Id="167" ReceiveListId="22" SingleProjectId="2" ParentId="166" SerialNumber="" Name="开工报告、图纸会审、设计变更" Sequence="0" Key="" />
              <移交内容 Id="168" ReceiveListId="23" SingleProjectId="2" ParentId="166" SerialNumber="" Name="桩位放线记录" Sequence="0" Key="" />
              <移交内容 Id="169" ReceiveListId="24" SingleProjectId="2" ParentId="166" SerialNumber="" Name="主要原材料出厂质量证明文件、进场复试报告及报验单" Sequence="0" Key="" />
              <移交内容 Id="170" ReceiveListId="25" SingleProjectId="2" ParentId="166" SerialNumber="" Name="砂浆、混凝土配合比及检验报告" Sequence="0" Key="" />
              <移交内容 Id="171" ReceiveListId="26" SingleProjectId="2" ParentId="166" SerialNumber="" Name="隐蔽工程检查（验收）记录及报验单" Sequence="0" Key="" />
              <移交内容 Id="172" ReceiveListId="27" SingleProjectId="2" ParentId="166" SerialNumber="" Name="工程质量事故处理记录" Sequence="0" Key="" />
              <移交内容 Id="173" ReceiveListId="28" SingleProjectId="2" ParentId="166" SerialNumber="" Name="桩基子分部工程质量验收记录" Sequence="0" Key="" />
              <移交内容 Id="174" ReceiveListId="29" SingleProjectId="2" ParentId="166" SerialNumber="" Name="桩基检测报告" Sequence="0" Key="" />
              <移交内容 Id="175" ReceiveListId="30" SingleProjectId="2" ParentId="166" SerialNumber="" Name="桩位竣工图" Sequence="0" Key="" />
              <移交内容 Id="176" ReceiveListId="31" SingleProjectId="2" ParentId="165" SerialNumber="" Name="建筑与结构工程" Sequence="0" Key="" />
              <移交内容 Id="177" ReceiveListId="32" SingleProjectId="2" ParentId="176" SerialNumber="" Name="开工报告及报审表" Sequence="0" Key="" />
              <移交内容 Id="178" ReceiveListId="33" SingleProjectId="2" ParentId="176" SerialNumber="" Name="图纸会审记录" Sequence="0" Key="" />
              <移交内容 Id="179" ReceiveListId="34" SingleProjectId="2" ParentId="176" SerialNumber="" Name="设计变更通知单、工程洽商记录（技术核定单）" Sequence="0" Key="" />
              <移交内容 Id="180" ReceiveListId="35" SingleProjectId="2" ParentId="176" SerialNumber="" Name="施工组织设计及报验单、施工方案、危险性较大分部分项工程施工方案" Sequence="0" Key="" />
              <移交内容 Id="181" ReceiveListId="36" SingleProjectId="2" ParentId="176" SerialNumber="" Name="主要原材料出厂质量证明文件、进场复试试验报告（砂、碎石、卵石、水泥、砖、钢材、商品混凝土、预应力筋、预应力锚具、夹具和连接器等）及报验单" Sequence="0" Key="" />
              <移交内容 Id="182" ReceiveListId="37" SingleProjectId="2" ParentId="176" SerialNumber="" Name="工程定位测量记录及报验单" Sequence="0" Key="" />
              <移交内容 Id="183" ReceiveListId="38" SingleProjectId="2" ParentId="176" SerialNumber="" Name="基槽验线记录、地基验槽记录、地基钎探记录" Sequence="0" Key="" />
              <移交内容 Id="184" ReceiveListId="39" SingleProjectId="2" ParentId="176" SerialNumber="" Name="地基承载力检验报告" Sequence="0" Key="" />
              <移交内容 Id="185" ReceiveListId="40" SingleProjectId="2" ParentId="176" SerialNumber="" Name="土壤密度及击实试验报告" Sequence="0" Key="" />
              <移交内容 Id="186" ReceiveListId="41" SingleProjectId="2" ParentId="176" SerialNumber="" Name="回填土试验报告（应附图）" Sequence="0" Key="" />
              <移交内容 Id="187" ReceiveListId="42" SingleProjectId="2" ParentId="176" SerialNumber="" Name="砂浆配合比及砂浆抗压强度试验报告" Sequence="0" Key="" />
              <移交内容 Id="188" ReceiveListId="43" SingleProjectId="2" ParentId="176" SerialNumber="" Name="混凝土配合比及混凝土抗压（抗渗）强度试验报告、回弹法检测混凝土抗压强度报告" Sequence="0" Key="" />
              <移交内容 Id="189" ReceiveListId="44" SingleProjectId="2" ParentId="176" SerialNumber="" Name="钢筋焊接连接接头检测报告、钢筋机械连接接头检测报告" Sequence="0" Key="" />
              <移交内容 Id="190" ReceiveListId="45" SingleProjectId="2" ParentId="176" SerialNumber="" Name="化学植筋承载力检验报告" Sequence="0" Key="" />
              <移交内容 Id="191" ReceiveListId="46" SingleProjectId="2" ParentId="176" SerialNumber="" Name="钢筋保护层厚度检测报告、钢筋间距及楼板厚度检测报告" Sequence="0" Key="" />
              <移交内容 Id="192" ReceiveListId="47" SingleProjectId="2" ParentId="176" SerialNumber="" Name="外墙饰面砖样板粘接强度检测报告" Sequence="0" Key="" />
              <移交内容 Id="193" ReceiveListId="48" SingleProjectId="2" ParentId="176" SerialNumber="" Name="预应力筋张拉、有粘结预应力结构灌浆记录" Sequence="0" Key="" />
              <移交内容 Id="194" ReceiveListId="49" SingleProjectId="2" ParentId="176" SerialNumber="" Name="网架（索膜）施工记录、网架节点承载力试验报告" Sequence="0" Key="" />
              <移交内容 Id="195" ReceiveListId="50" SingleProjectId="2" ParentId="176" SerialNumber="" Name="木结构构件力学性能试验报告、木结构防护剂试验报告" Sequence="0" Key="" />
              <移交内容 Id="196" ReceiveListId="51" SingleProjectId="2" ParentId="176" SerialNumber="" Name="钢结构工程" Sequence="0" Key="" />
              <移交内容 Id="197" ReceiveListId="52" SingleProjectId="2" ParentId="196" SerialNumber="" Name="图纸会审记录、设计变更通知单、工程洽商记录" Sequence="0" Key="" />
              <移交内容 Id="198" ReceiveListId="53" SingleProjectId="2" ParentId="196" SerialNumber="" Name="钢结构材料出厂质量证明文件、进场复试报告（钢材、防火涂料、焊接材料、高强度大六角头螺栓连接副、扭剪型高强螺栓连接副等）及报验单" Sequence="0" Key="" />
              <移交内容 Id="199" ReceiveListId="54" SingleProjectId="2" ParentId="196" SerialNumber="" Name="超声波、磁粉、射线探伤报告" Sequence="0" Key="" />
              <移交内容 Id="200" ReceiveListId="55" SingleProjectId="2" ParentId="196" SerialNumber="" Name="高强度螺栓抗滑移系数、抗扭矩试验、拉拔试验报告" Sequence="0" Key="" />
              <移交内容 Id="201" ReceiveListId="56" SingleProjectId="2" ParentId="196" SerialNumber="" Name="防腐、防火涂料厚度检测报告" Sequence="0" Key="" />
              <移交内容 Id="202" ReceiveListId="57" SingleProjectId="2" ParentId="196" SerialNumber="" Name="构件吊装记录" Sequence="0" Key="" />
              <移交内容 Id="203" ReceiveListId="58" SingleProjectId="2" ParentId="196" SerialNumber="" Name="隐蔽工程检查（验收）记录及报验单" Sequence="0" Key="" />
              <移交内容 Id="204" ReceiveListId="59" SingleProjectId="2" ParentId="196" SerialNumber="" Name="钢结构子分部工程质量验收记录" Sequence="0" Key="" />
              <移交内容 Id="205" ReceiveListId="60" SingleProjectId="2" ParentId="176" SerialNumber="" Name="防水工程试水检查记录" Sequence="0" Key="" />
              <移交内容 Id="206" ReceiveListId="61" SingleProjectId="2" ParentId="176" SerialNumber="" Name="沉降观测记录及报验单" Sequence="0" Key="" />
              <移交内容 Id="207" ReceiveListId="62" SingleProjectId="2" ParentId="176" SerialNumber="" Name="工程竣工测量（建筑物垂直度、全高测量记录等）" Sequence="0" Key="" />
              <移交内容 Id="208" ReceiveListId="63" SingleProjectId="2" ParentId="176" SerialNumber="" Name="分户验收汇总表、室内环境检测报告" Sequence="0" Key="" />
              <移交内容 Id="209" ReceiveListId="64" SingleProjectId="2" ParentId="176" SerialNumber="" Name="隐蔽工程检查（验收）记录及报验单" Sequence="0" Key="" />
              <移交内容 Id="210" ReceiveListId="65" SingleProjectId="2" ParentId="176" SerialNumber="" Name="工程质量事故处理记录" Sequence="0" Key="" />
              <移交内容 Id="211" ReceiveListId="66" SingleProjectId="2" ParentId="176" SerialNumber="" Name="分部（子分部）工程质量验收记录" Sequence="0" Key="" />
              <移交内容 Id="212" ReceiveListId="67" SingleProjectId="2" ParentId="165" SerialNumber="" Name="节能保温工程" Sequence="0" Key="" />
              <移交内容 Id="213" ReceiveListId="68" SingleProjectId="2" ParentId="212" SerialNumber="" Name="节能工程材料出厂质量证明文件、进场复试报告及报验单" Sequence="0" Key="" />
              <移交内容 Id="214" ReceiveListId="69" SingleProjectId="2" ParentId="212" SerialNumber="" Name="门窗物理性能检测报告" Sequence="0" Key="" />
              <移交内容 Id="215" ReceiveListId="70" SingleProjectId="2" ParentId="212" SerialNumber="" Name="节能性能检测报告" Sequence="0" Key="" />
              <移交内容 Id="216" ReceiveListId="71" SingleProjectId="2" ParentId="212" SerialNumber="" Name="隐蔽工程检查（验收）记录及报验单" Sequence="0" Key="" />
              <移交内容 Id="217" ReceiveListId="72" SingleProjectId="2" ParentId="212" SerialNumber="" Name="节能分部工程质量验收记录" Sequence="0" Key="" />
              <移交内容 Id="218" ReceiveListId="73" SingleProjectId="2" ParentId="165" SerialNumber="" Name="幕墙工程" Sequence="0" Key="" />
              <移交内容 Id="219" ReceiveListId="74" SingleProjectId="2" ParentId="218" SerialNumber="" Name="图纸会审记录、设计变更通知单、工程洽商记录" Sequence="0" Key="" />
              <移交内容 Id="220" ReceiveListId="75" SingleProjectId="2" ParentId="218" SerialNumber="" Name="幕墙材料出厂质量证明文件、进场复试报告（铝塑板、石材、玻璃、结构胶等）及报验单" Sequence="0" Key="" />
              <移交内容 Id="221" ReceiveListId="76" SingleProjectId="2" ParentId="218" SerialNumber="" Name="后置埋件的现场拉拔强度检测报告" Sequence="0" Key="" />
              <移交内容 Id="222" ReceiveListId="77" SingleProjectId="2" ParentId="218" SerialNumber="" Name="幕墙的抗风压性能、空气渗透性能、雨水渗透性能及平面内变形性能检测报告" Sequence="0" Key="" />
              <移交内容 Id="223" ReceiveListId="78" SingleProjectId="2" ParentId="218" SerialNumber="" Name="隐蔽工程检查（验收）记录（预埋件或后置埋件、龙骨隐蔽、幕墙防火构造、幕墙防雷装置等）及报验单" Sequence="0" Key="" />
              <移交内容 Id="224" ReceiveListId="79" SingleProjectId="2" ParentId="218" SerialNumber="" Name="幕墙子分部工程质量验收记录" Sequence="0" Key="" />
              <移交内容 Id="225" ReceiveListId="80" SingleProjectId="2" ParentId="165" SerialNumber="" Name="给排水及采暖工程" Sequence="0" Key="" />
              <移交内容 Id="226" ReceiveListId="81" SingleProjectId="2" ParentId="225" SerialNumber="" Name="图纸会审记录、设计变更通知单、工程洽商记录" Sequence="0" Key="" />
              <移交内容 Id="227" ReceiveListId="82" SingleProjectId="2" ParentId="225" SerialNumber="" Name="材料、构配件出厂质量证明文件及进场复试试验报告" Sequence="0" Key="" />
              <移交内容 Id="228" ReceiveListId="83" SingleProjectId="2" ParentId="225" SerialNumber="" Name="隐蔽工程检查（验收）记录及报验单" Sequence="0" Key="" />
              <移交内容 Id="229" ReceiveListId="84" SingleProjectId="2" ParentId="225" SerialNumber="" Name="施工试验记录、设备试运行记录（系统清洗、灌水、通水、通球试验记录）及报验单" Sequence="0" Key="" />
              <移交内容 Id="230" ReceiveListId="85" SingleProjectId="2" ParentId="225" SerialNumber="" Name="分部（子分部）工程质量验收记录" Sequence="0" Key="" />
              <移交内容 Id="231" ReceiveListId="86" SingleProjectId="2" ParentId="165" SerialNumber="" Name="建筑电气工程" Sequence="0" Key="" />
              <移交内容 Id="232" ReceiveListId="87" SingleProjectId="2" ParentId="231" SerialNumber="" Name="图纸会审记录、设计变更通知单、工程洽商记录" Sequence="0" Key="" />
              <移交内容 Id="233" ReceiveListId="88" SingleProjectId="2" ParentId="231" SerialNumber="" Name="材料、设备出厂质量证明文件及进场复试试验报告" Sequence="0" Key="" />
              <移交内容 Id="234" ReceiveListId="89" SingleProjectId="2" ParentId="231" SerialNumber="" Name="隐蔽工程检查（验收）记录及报验单" Sequence="0" Key="" />
              <移交内容 Id="235" ReceiveListId="90" SingleProjectId="2" ParentId="231" SerialNumber="" Name="接地、绝缘电阻测试记录及报验单" Sequence="0" Key="" />
              <移交内容 Id="236" ReceiveListId="91" SingleProjectId="2" ParentId="231" SerialNumber="" Name="电气设备空载试运行记录、建筑物照明通电试运行记录及报验单" Sequence="0" Key="" />
              <移交内容 Id="237" ReceiveListId="92" SingleProjectId="2" ParentId="231" SerialNumber="" Name="分部（子分部）工程质量验收记录" Sequence="0" Key="" />
              <移交内容 Id="238" ReceiveListId="93" SingleProjectId="2" ParentId="165" SerialNumber="" Name="通风与空调工程" Sequence="0" Key="" />
              <移交内容 Id="239" ReceiveListId="94" SingleProjectId="2" ParentId="238" SerialNumber="" Name="图纸会审记录、设计变更通知单、工程洽商记录" Sequence="0" Key="" />
              <移交内容 Id="240" ReceiveListId="95" SingleProjectId="2" ParentId="238" SerialNumber="" Name="材料、设备出厂质量证明文件及进场复试试验报告" Sequence="0" Key="" />
              <移交内容 Id="241" ReceiveListId="96" SingleProjectId="2" ParentId="238" SerialNumber="" Name="隐蔽工程检查（验收）记录及报验单" Sequence="0" Key="" />
              <移交内容 Id="242" ReceiveListId="97" SingleProjectId="2" ParentId="238" SerialNumber="" Name="空调系统试运转调试记录、空调水系统试运转调试记录、防排烟系统联合试运行记录及报验单" Sequence="0" Key="" />
              <移交内容 Id="243" ReceiveListId="98" SingleProjectId="2" ParentId="238" SerialNumber="" Name="制冷系统气密性试验记录及报验单" Sequence="0" Key="" />
              <移交内容 Id="244" ReceiveListId="99" SingleProjectId="2" ParentId="238" SerialNumber="" Name="净化空调系统检测记录及报验单" Sequence="0" Key="" />
              <移交内容 Id="245" ReceiveListId="100" SingleProjectId="2" ParentId="238" SerialNumber="" Name="分部（子分部）工程质量验收记录" Sequence="0" Key="" />
              <移交内容 Id="246" ReceiveListId="101" SingleProjectId="2" ParentId="165" SerialNumber="" Name="智能建筑工程" Sequence="0" Key="" />
              <移交内容 Id="247" ReceiveListId="102" SingleProjectId="2" ParentId="246" SerialNumber="" Name="图纸会审记录、设计变更通知单、工程洽商记录" Sequence="0" Key="" />
              <移交内容 Id="248" ReceiveListId="103" SingleProjectId="2" ParentId="246" SerialNumber="" Name="材料、设备出厂质量证明文件及进场复试试验报告" Sequence="0" Key="" />
              <移交内容 Id="249" ReceiveListId="104" SingleProjectId="2" ParentId="246" SerialNumber="" Name="隐蔽工程检查（验收）记录及报验单" Sequence="0" Key="" />
              <移交内容 Id="250" ReceiveListId="105" SingleProjectId="2" ParentId="246" SerialNumber="" Name="施工试验记录、智能设备试运行记录及报验单" Sequence="0" Key="" />
              <移交内容 Id="251" ReceiveListId="106" SingleProjectId="2" ParentId="246" SerialNumber="" Name="分部（子分部）工程质量验收记录" Sequence="0" Key="" />
              <移交内容 Id="252" ReceiveListId="107" SingleProjectId="2" ParentId="165" SerialNumber="" Name="电梯工程" Sequence="0" Key="" />
              <移交内容 Id="253" ReceiveListId="108" SingleProjectId="2" ParentId="252" SerialNumber="" Name="电梯出厂合格证书、安全部件型式试验证书及开箱检验记录" Sequence="0" Key="" />
              <移交内容 Id="254" ReceiveListId="109" SingleProjectId="2" ParentId="252" SerialNumber="" Name="隐蔽工程检查（验收）记录及报验单" Sequence="0" Key="" />
              <移交内容 Id="255" ReceiveListId="110" SingleProjectId="2" ParentId="252" SerialNumber="" Name="电梯负荷运行试验记录及报验单" Sequence="0" Key="" />
              <移交内容 Id="256" ReceiveListId="111" SingleProjectId="2" ParentId="252" SerialNumber="" Name="自动扶梯、自动人行道整机性能、运行试验记录及报验单" Sequence="0" Key="" />
              <移交内容 Id="257" ReceiveListId="112" SingleProjectId="2" ParentId="252" SerialNumber="" Name="电梯安装自检报告" Sequence="0" Key="" />
              <移交内容 Id="258" ReceiveListId="113" SingleProjectId="2" ParentId="252" SerialNumber="" Name="电梯检测报告" Sequence="0" Key="" />
              <移交内容 Id="259" ReceiveListId="114" SingleProjectId="2" ParentId="252" SerialNumber="" Name="分部（子分部）工程质量验收记录" Sequence="0" Key="" />
              <移交内容 Id="260" ReceiveListId="115" SingleProjectId="2" ParentId="252" SerialNumber="" Name="土建布置图" Sequence="0" Key="" />
              <移交内容 Id="261" ReceiveListId="116" SingleProjectId="2" ParentId="165" SerialNumber="" Name="建筑消防工程（参照水、电、智能等分部工程文件材料）" Sequence="0" Key="" />
              <移交内容 Id="262" ReceiveListId="117" SingleProjectId="2" ParentId="165" SerialNumber="" Name="建筑内、外装饰工程（参照土建、水、电分部工程文件材料）" Sequence="0" Key="" />
              <移交内容 Id="263" ReceiveListId="118" SingleProjectId="2" ParentId="165" SerialNumber="" Name="室外工程" Sequence="0" Key="" />
              <移交内容 Id="264" ReceiveListId="119" SingleProjectId="2" ParentId="263" SerialNumber="" Name="室外安装施工文件（给水、雨水、污水、燃气、电讯、电力照明、电视、消防等）" Sequence="0" Key="" />
              <移交内容 Id="265" ReceiveListId="120" SingleProjectId="2" ParentId="263" SerialNumber="" Name="室外建筑环境施工文件（建筑小品、水景、道路、园林绿化等）" Sequence="0" Key="" />
              <移交内容 Id="266" ReceiveListId="121" SingleProjectId="2" ParentId="0" SerialNumber="" Name="（四）竣工图" Sequence="0" Key="" />
              <移交内容 Id="267" ReceiveListId="122" SingleProjectId="2" ParentId="266" SerialNumber="" Name="建筑竣工图" Sequence="0" Key="" />
              <移交内容 Id="268" ReceiveListId="123" SingleProjectId="2" ParentId="266" SerialNumber="" Name="结构竣工图" Sequence="0" Key="" />
              <移交内容 Id="269" ReceiveListId="124" SingleProjectId="2" ParentId="266" SerialNumber="" Name="钢结构竣工图" Sequence="0" Key="" />
              <移交内容 Id="270" ReceiveListId="125" SingleProjectId="2" ParentId="266" SerialNumber="" Name="幕墙竣工图" Sequence="0" Key="" />
              <移交内容 Id="271" ReceiveListId="126" SingleProjectId="2" ParentId="266" SerialNumber="" Name="建筑给排水及供暖竣工图" Sequence="0" Key="" />
              <移交内容 Id="272" ReceiveListId="127" SingleProjectId="2" ParentId="266" SerialNumber="" Name="建筑电气竣工图" Sequence="0" Key="" />
              <移交内容 Id="273" ReceiveListId="128" SingleProjectId="2" ParentId="266" SerialNumber="" Name="智能化竣工图" Sequence="0" Key="" />
              <移交内容 Id="274" ReceiveListId="129" SingleProjectId="2" ParentId="266" SerialNumber="" Name="通风与空调竣工图" Sequence="0" Key="" />
              <移交内容 Id="275" ReceiveListId="130" SingleProjectId="2" ParentId="266" SerialNumber="" Name="室外工程竣工图" Sequence="0" Key="" />
              <移交内容 Id="276" ReceiveListId="131" SingleProjectId="2" ParentId="266" SerialNumber="" Name="规划红线内的室外给水、排水、供热、供电、燃气、照明管线等竣工图" Sequence="0" Key="" />
              <移交内容 Id="277" ReceiveListId="132" SingleProjectId="2" ParentId="266" SerialNumber="" Name="规划红线内的道路、园林绿化、喷灌设施等竣工图" Sequence="0" Key="" />
              <移交内容 Id="278" ReceiveListId="133" SingleProjectId="2" ParentId="0" SerialNumber="" Name="（五）竣工验收文件" Sequence="0" Key="" />
              <移交内容 Id="279" ReceiveListId="134" SingleProjectId="2" ParentId="278" SerialNumber="" Name="规划、消防、环保、民防、防雷等部门出具的认可文件或准许使用文件" Sequence="0" Key="" />
              <移交内容 Id="280" ReceiveListId="135" SingleProjectId="2" ParentId="278" SerialNumber="" Name="专家组竣工验收意见及会议纪要" Sequence="0" Key="" />
              <移交内容 Id="281" ReceiveListId="136" SingleProjectId="2" ParentId="278" SerialNumber="" Name="竣工验收报告" Sequence="0" Key="" />
              <移交内容 Id="282" ReceiveListId="137" SingleProjectId="2" ParentId="278" SerialNumber="" Name="房屋建筑工程质量保修书" Sequence="0" Key="" />
              <移交内容 Id="283" ReceiveListId="138" SingleProjectId="2" ParentId="278" SerialNumber="" Name="住宅质量保证书、住宅使用说明书" Sequence="0" Key="" />
              <移交内容 Id="284" ReceiveListId="139" SingleProjectId="2" ParentId="278" SerialNumber="" Name="建设工程竣工验收备案表" Sequence="0" Key="" />
              <移交内容 Id="285" ReceiveListId="140" SingleProjectId="2" ParentId="278" SerialNumber="" Name="五方责任主体工程质量终身责任承诺书" Sequence="0" Key="" />
              <移交内容 Id="286" ReceiveListId="141" SingleProjectId="2" ParentId="278" SerialNumber="" Name="建设工程档案移交书" Sequence="0" Key="" />
              <移交内容 Id="287" ReceiveListId="142" SingleProjectId="2" ParentId="0" SerialNumber="" Name="（六）工程声像、电子档案" Sequence="0" Key="" />
              <移交内容 Id="288" ReceiveListId="143" SingleProjectId="2" ParentId="287" SerialNumber="" Name="声像档案。按《德阳市建设工程声像档案管理规定》执行。" Sequence="0" Key="" />
              <移交内容 Id="289" ReceiveListId="144" SingleProjectId="2" ParentId="287" SerialNumber="" Name="电子档案。按《关于开展建设工程电子档案收集工作的通知》执行。" Sequence="0" Key="" />-->
    '''
    line1 = '          <移交内容 Id="%s" ReceiveListId="1" SingleProjectId="%s" ParentId="%s" SerialNumber="" Name="%s" Sequence="0" Key="%s" />\n'
    line2 = '              <移交内容 Id="%s" ReceiveListId="2" SingleProjectId="%s" ParentId="%s" SerialNumber="" Name="%s" Sequence="0" Key="%s" />'
    fo.write(onno)
    fo.write(line1 % (str(id), dwgcid, id2, gcmc, str(uuid.uuid4()).upper()))
    id2 = id
    id += 1
    fo.write(line2 % (str(id), dwgcid, id2, gcmc, str(uuid.uuid4()).upper()))
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
    global table, wjyc
    wjyc = ''
    table = PrettyTable(["文件名", "起始页码", "终止页码", "页数", "PDF状态", "形成时间", "文图号"])
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
    ljr = '陈宏'
    zrz=jsdw
    ajzrz=jsdw
    jnwjqssj = jnwjzzsj = datenow_
    jnwjqssj = jnwjzzsj = ""
    bgqx = "0"
    mj = "0"
    tmp1=1
    
    try:
        with open(xmmc+'.csv') as f:
            newcsv=''
            for i in f.readlines():
                line=i.strip()
                line=''.join(line.split())
                a=line.split(',')
                if a[1] != '':
                    a=','.join(a)+'\n'
                    newcsv+=a
        with open(xmmc+'.csv','w+',encoding='gbk') as f:
            f.write(newcsv)
    except:
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
            test_zzy = 0
            test_zzy1 = 0
            try:
                shutil.rmtree(xmmc + '\\' + xmmc)
            except:
                pass
            for i in f.readlines():
                line = i.strip()
                line = ''.join(line.split())
                dt = re.compile(r',,,,,+')
                k = re.search(dt, line)
                if k:
                    line = dt.sub('', line)
                if ',' in line:
                    a = line.split(',')
                    try:
                        try:
                            int(a[1])
                        except:
                            continue
                        if a[1] == '0':
                            ajtm_ = a[0]
                            print('  '+str(tmp1).zfill(2)+'  '+a[0])
                            tmp1+=1
                            wjyc += '***' + a[0] + '***</b><br>'
                        else:
                            count += 1
                        if a[1] == '1':
                            if not no1st == 0:
                                fo.write("          </案卷>\n")
                            zdjh += 1
                            no1st += 1
                            ajtm = gcmc + ajtm_
                            fo.write(
                                "          <案卷 Id=\"%s\" SingleProjectId=\"%s\" Ajh=\"%s\" Zdjh=\"%s\" Ajtm=\"%s\" Bzdw=\"%s\" Bzrq=\"%s\" Zrz=\"%s\" Gg=\"%s\" JnwjQssj=\"%s\" JnwjZzsj=\"%s\" Bgqx=\"%s\" Mj=\"%s\" Ljr=\"%s\" Ljsj=\"%s\" Ztc=\"%s\" Fz=\"%s\" Key=\"%s\">\n" %
                                (count_aj, singleprojectid, ajh, zdjh, ajtm, bzdw, bzrq, ajzrz, gg, jnwjqssj, jnwjzzsj, bgqx, mj, ljr, ljsj, ztc, fz, str(
                                    uuid.uuid4()).upper()))
                            ajtm_ = ''
                            test_zzy = 0
                    except BaseException:
                        pass
                    try:
                        if a[1] == '0':
                            count_aj += 1
                            table.add_row(['', '', '', '', '', '', ''])
                            table.add_row(
                                ['第' + str(count_aj) + '卷', '', '', '', '', '', ''])
                            table.add_row(['-----', '', '', '', '', '', ''])
                            continue
                    except BaseException:
                        pass
                    try:
                        qsy = str(int(a[1]))
                    except BaseException:
                        qsy = '错误'
                        isok = '错误'
                    try:
                        zzy = str(int(a[2]))
                        if int(zzy) - int(qsy) < 0:
                            zzy = '错误'
                    except BaseException:
                        zzy = '错误'
                        isok = '错误'
                    if not int(a[1]) - 1 == int(test_zzy):
                        print(colorama.Fore.LIGHTRED_EX +"      终止页 " + str(test_zzy) + " 错误!")
                    test_zzy = a[2]

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
                            isok = '错误'
                    except BaseException:
                        ab = '错误'
                        isok = '错误'
                    try:
                        wth = a[4]
                    except BaseException:
                        wth = sgdw
                    try:
                        zrz = a[5]
                        if zrz=='':
                            zrz=jsdw
                    except BaseException:
                        zrz = jsdw
                    try:
                        ajzrz = a[5]
                        if ajzrz=='':
                            ajzrz=jsdw
                    except BaseException:
                        ajzrz = jsdw
                    try:
                        wjyc += line + '<br>'
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
                            isok = ''
                    except BaseException:
                        # print(colorama.Fore.LIGHTRED_EX +'%s错误，%s第%s至第%s页\n'%(a[0],str(count_aj) + '.pdf',qsy,zzy))
                        #print(colorama.Fore.LIGHTGREEN_EX + '      %s错误，第%s%s至%s页\n' %
                        #      (str(count) + '.pdf', str(count_aj) + '卷', qsy, zzy))
                        isok = '错误'

                    isok = ''
                    table.add_row([str(count) + '.pdf', qsy,
                                   zzy, ab, isok, xcsj, wth])
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
    s = table.get_html_string()
    report.write(s)
    print(colorama.Back.RESET, end="")
    fo.flush()
    report.flush()
    fo.close()
    report.close()

def jxxml(file):
    try:
        tree = etree.parse(file)
        treeview = etree.tounicode(tree, pretty_print=True)
    except BaseException:
        print('文件不存在！')

    dtsl = len(tree.xpath('//单位工程'))
    for i in range(dtsl):
        j = i + 1
        #print('\n'+str(j), end=':')
        #print(tree.xpath('//单位工程[%s]/@Gcmc' % j)[0]+'目录生成成功！')
        wjm = tree.xpath('//单位工程[%s]/@Gcmc' % j)[0]

        workbook = xlsxwriter.Workbook('目录-' + wjm + '.xlsx')
        worksheet = workbook.add_worksheet()

        table = prettytable.PrettyTable(
            ["序号", "文件编号", "责任者", "文件题名", "日期", "页次", "备注"])

        table.padding_witdth = 1

        xmmc = tree.xpath('//项目/@Xmmc')
        xmdd = tree.xpath('//项目/@Xmdd')
        jsdw = tree.xpath('//单位工程[%s]/@Jsdw' % j)
        sgdw = tree.xpath('//单位工程[%s]/@Sgdw' % j)
        jldw = tree.xpath('//单位工程[%s]/@Jldw' % j)
        kcdw = tree.xpath('//单位工程[%s]/@Kcdw' % j)
        sjdw = tree.xpath('//单位工程[%s]/@Sjdw' % j)
        lxpzdw = tree.xpath('//单位工程[%s]/@Lxpzdw' % j)
        lxpzwh = tree.xpath('//单位工程[%s]/@Lxpzwh' % j)
        ghxkzh = tree.xpath('//单位工程[%s]/@Ghxkzh' % j)
        ydghxkzh = tree.xpath('//单位工程[%s]/@Ydghxkzh' % j)
        sgxkzh = tree.xpath('//单位工程[%s]/@Sgxkzh' % j)
        gcdh = tree.xpath('//单位工程[%s]/@Gcdh' % j)
        kgrq = tree.xpath('//单位工程[%s]/@Kgrq' % j)
        
        try:
            kgrq = kgrq[0].rsplit('/')
            kgrq = kgrq[0] + kgrq[1].zfill(2) + kgrq[2].zfill(2)
        except BaseException:
            kgrq = ''
        jgrq = tree.xpath('//单位工程[%s]/@Jgrq' % j)
        try:
            jgrq = jgrq[0].rsplit('/')
            jgrq = jgrq[0] + jgrq[1].zfill(2) + jgrq[2].zfill(2)
        except BaseException:
            jgrq = ''

        ajsl = len(tree.xpath('//单位工程[%s]/案卷' % j))
        xrh = 0
        test1 = 0
        for aj_i in range(ajsl):
            aj_j = aj_i + 1

            zdjh = tree.xpath('//单位工程[%s]/案卷[%s]/@Zdjh' % (j, aj_j))
            table.add_row(['', '', '', '', '', '', ''])

            wjsl = len(tree.xpath('//单位工程[%s]/案卷[%s]/文件' % (j, aj_j)))

            if test1 > 0:
                xrh += 1
            xh = 1
            for wj_i in range(wjsl):
                wj_j = wj_i + 1
                wjtm = tree.xpath(
                    '//单位工程[%s]/案卷[%s]/文件[%s]/@Wjtm' %
                    (j, aj_j, wj_j))
                qsy = tree.xpath(
                    '//单位工程[%s]/案卷[%s]/文件[%s]/@Qsy' %
                    (j, aj_j, wj_j))
                zzy = tree.xpath(
                    '//单位工程[%s]/案卷[%s]/文件[%s]/@Zzy' %
                    (j, aj_j, wj_j))
                xcsj = tree.xpath(
                    '//单位工程[%s]/案卷[%s]/文件[%s]/@Xcsj' %
                    (j, aj_j, wj_j))
                yc = str(qsy[0]) + '-' + str(zzy[0])
                zrz = tree.xpath('//单位工程[%s]/案卷[%s]/文件[%s]/@Zrz' %
                    (j, aj_j, wj_j))
                try:
                    xcsj = xcsj[0].rsplit('/')
                    xcsj = xcsj[0] + '-' + \
                        xcsj[1].zfill(2) + '-' + xcsj[2].zfill(2)
                except BaseException:
                    xcsj = ''
                wth = tree.xpath(
                    '//单位工程[%s]/案卷[%s]/文件[%s]/@Wth' %
                    (j, aj_j, wj_j))
                row = [str(xh), '', zrz[0], wjtm[0], xcsj, yc, '']
                table.add_row(row)

                worksheet.write(xrh, 0, str(xh))
                worksheet.write(xrh, 1, '')
                worksheet.write(xrh, 2, zrz[0])
                worksheet.write(xrh, 3, wjtm[0])
                worksheet.write(xrh, 4, xcsj)
                worksheet.write(xrh, 5, yc)
                worksheet.write(xrh, 6, '')
                xh += 1
                xrh += 1
                test1 += 1

        workbook.close()

if __name__ == "__main__":
    # os.system('cls')
    colorama.init()
    # tb()
    try:
        xm(sys.argv[1])
    except:
        print ("Parameter error!")
        #sys.exit()
    dwgc()
    yjnr()
    aj()
    wb()
    os.remove(xmmc + '\\report.html')
    jxxml(xmmc + '\\' + xmmc + '.xml')
    # print ("\n\n")
    # print (table)
    # print('\n测试完成!\n')