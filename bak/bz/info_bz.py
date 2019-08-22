import uuid
import os
import xlsx2csv
import random
import datetime
import shutil
import tkinter as tk
from tkinter import filedialog
import lxml
from bs4 import BeautifulSoup
from PyPDF2 import PdfFileReader, PdfFileWriter
import traceback
import re
from icecream import ic
import pysnooper


def 打开文件():
    root = tk.Tk()
    root.withdraw()
    fn = filedialog.askopenfilename(
        filetypes=(("xlsx", "*.xlsx"), ("*.*", "*.*")))
    oschdir = os.path.dirname(fn)
    os.chdir(oschdir)
    fn = fn.split("/")[-1]
    return fn


def 转换csv(fn):
    if os.path.exists(fn):
        文件名 = fn.split(".")[0] + ".csv"
        try:
            os.system("xlsx2csv.py %s %s " % (fn, 文件名))
        except BaseException:
            traceback.print_exc()

        try:
            with open(文件名, encoding="utf-8") as f:
                newcsv = ""
                for i in f.readlines():
                    line = i.strip()
                    line = "".join(line.split())
                    列 = line.split(",")

                    dt = re.compile(r",,+")
                    k = re.search(dt, line)
                    if k:
                        line = dt.sub("", line)

                    if 列[1] != "":
                        列 = ",".join(列) + "\n"
                        newcsv += 列
            with open(文件名, "w+", encoding="utf-8") as f:
                f.write(newcsv)
        except BaseException:
            traceback.print_exc()

# @pysnooper.snoop()
def 切割pdf(起始页, 终止页, 文件存储路径, 打开文件号, 生成文件号):
    try:
        起始页 = int(起始页)
        终止页 = int(终止页)
    except BaseException:
        traceback.print_exc()

    页数 = 终止页 - 起始页 + 1

    try:
        if int(页数) > 0:
            reader = PdfFileReader(str(打开文件号) + ".pdf")
            writer = PdfFileWriter()
            with open(文件存储路径 + str(生成文件号) + ".pdf", "wb") as wstream:
                for page in range(起始页 - 1, 终止页):
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
                except BaseException:
                    pass

            if not isdouble:
                print('非双层PDF')

    except BaseException:
        traceback.print_exc()


def 现在时间():
    now_ = datetime.datetime.now()
    datenow_ = "%s/%s/%s" % (now_.year, now_.month, now_.day)
    return datenow_ + " 0:00:00"


def 处理日期(fn):
    处理完成的日期 = ''
    if not fn.isdigit() or len(fn) < 8:
        处理完成的日期 = ""
    else:
        处理完成的日期 = fn[:4] + "-" + fn[4:6] + "-" + fn[6:8] + ' 0:00:00'
    return 处理完成的日期


def 审核时间():
    两天后 = datetime.datetime.now() + datetime.timedelta(1)
    week = 两天后.weekday()
    if week == 6:
        审核时间 = 两天后 + datetime.timedelta(2)
    elif week == 0:
        审核时间 = 两天后 + datetime.timedelta(1)
    else:
        审核时间 = 两天后
    datenow_ = "%s/%s/%s" % (审核时间.year, 审核时间.month, 审核时间.day)
    return datenow_ + " 0:00:00"


def 遍历csv(fn):
    fn = fn.split(".")[0] + ".csv"
    列 = []
    with open(fn, encoding="utf-8") as f:
        for i in f.readlines():
            line = i.strip()
            line = "".join(line.split())
            列.append(line.split(","))
            # print(列)
        return 列

# @pysnooper.snoop()
def 提交变量值(fn):
    global 项目地点, 建设单位, 设计单位, 监理单位, 勘察单位, 立项批准单位, 立项批准文号, 规划许可证号, 施工许可证号, 国有土地使用证号, 高度, 基础类型, 结构类型, 地上层数, 地下层数, 建筑面积, 用地面积, 单体Key, 施工单位, 开工日期, 竣工日期, 项目名称, 项目类型, 项目Key, 工程档号, 总登记号

    for i in fn:
        if i[1] == ":":
            if i[0] == "项目地点":
                项目地点 = i[2]
            elif i[0] == "建设单位":
                建设单位 = i[2]
            elif i[0] == "设计单位":
                设计单位 = i[2]
            elif i[0] == "监理单位":
                监理单位 = i[2]
            elif i[0] == "勘察单位":
                勘察单位 = i[2]
            elif i[0] == "立项批准单位":
                立项批准单位 = i[2]
            elif i[0] == "立项批准文号":
                立项批准文号 = i[2]
            elif i[0] == "规划许可证号":
                规划许可证号 = i[2]
            elif i[0] == "施工许可证号":
                施工许可证号 = i[2]
            elif i[0] == "国有土地使用证号":
                国有土地使用证号 = i[2]
            elif i[0] == "高度":
                高度 = i[2]
            elif i[0] == "基础类型":
                基础类型 = i[2]
            elif i[0] == "结构类型":
                结构类型 = i[2]
            elif i[0] == "地上层数":
                地上层数 = i[2]
            elif i[0] == "地下层数":
                地下层数 = i[2]
            elif i[0] == "建筑面积":
                建筑面积 = i[2]
            elif i[0] == "用地面积":
                用地面积 = i[2]
            elif i[0] == "单体Key":
                单体Key = i[2]
            elif i[0] == "项目Key":
                项目Key = i[2]
            elif i[0] == "施工单位":
                施工单位 = i[2]
            elif i[0] == "开工日期":
                开工日期 = i[2]
            elif i[0] == "竣工日期":
                竣工日期 = i[2]
            elif i[0] == "工程档号":
                工程档号 = i[2]
            elif i[0] == "总登记号":
                总登记号 = i[2]
    #os.system("cls")


def 创建文件项(名称):
    axml.临时文件 += r'<File Id="{案卷序号}" SingleProjectId="{单体序号}" Zdjh="{总登记号}" Ajdh="{案卷档号}" Ajtm="{案卷名称}" Bzdw="{编制单位}" Yjdw="{移交单位}四川筑鼎投资有限公司" Ztlx="1" Mj="1" Bgqx="1" Ajsx="1" Ljr="立卷人" Ljrq="{立卷时间}" Bzsj="{编制时间}" Shr="审核人" Shrq="{审核时间}" Fz="" JnwjQssj="{卷内文件起始时间}" JnwjZzsj="{卷内文件终止时间}" Zrz="{责任者}" Ztc="" Key="{Key}">'.format(
        案卷序号=axml.案卷序号,
        单体序号=单体序号,
        总登记号=axml.总登记号,
        案卷档号=工程档号 + '-' + str(axml.案卷序号).zfill(3),
        案卷名称=名称,
        编制单位=建设单位,
        移交单位=建设单位,
        立卷时间=现在时间(),
        编制时间=现在时间(),
        审核时间=审核时间(),
        卷内文件起始时间="",
        卷内文件终止时间="",
        责任者=建设单位,
        Key=str(uuid.uuid4()),
    )


class 项目xml:
    临时文件 = ""
    单体序号递增 = 1
    文件名称递增 = 1
    文件序号递增 = 1
    案卷序号递增 = 1
    项目名称 = ""
    项目类型 = ""
    总登记号 = 1
    案卷序号 = 1
    文件名称=1
    项目Key = ""
    细类Key字典 = {}

    def 创建项目(self):
        项目名称 = input("项目名称：")
        if 项目名称 == "":
            项目名称 = "项目名称"

        try:
            shutil.rmtree(项目名称, True)
        except BaseException:
            pass

        项目类型 = input("项目类型（0、1、2）：")
        if 项目类型 == "":
            项目类型 = "1"

        总登记号 = input("总登记号")
        if 总登记号 == "":
            总登记号 = 1
        else:
            try:
                总登记号 = int(总登记号)
            except BaseException:
                总登记号 = 1

        项目Key = input("项目Key:")
        if 项目Key == "":
            项目Key = "项目Key未填"

        单体Key = input("单体Key:")
        if 单体Key == "":
            单体Key = "单体Key未填"

        self.项目名称 = 项目名称
        self.项目类型 = 项目类型
        self.总登记号 = 总登记号
        self.项目Key = 项目Key
        self.单体Key = 单体Key

        if os.path.exists('项目名称'):
            shutil.rmtree(项目名称, True)
            os.mkdir(项目名称)
        else:
            os.mkdir(项目名称)

        self.临时文件 += r'<?xml version="1.0" encoding="utf-8"?>'
        self.临时文件 += r"<ElectronicFileInformation>"
        '''
        self.临时文件 += r'<Project Id="1" Xmlx="{项目类型}" Xmmc="{项目名称}" Xmdd="{项目地点}" Jsdw="{建设单位}" Djdw="" Lxpzdw="{立项批准单位}" Sjdw="{设计单位}" Jldw="{监理单位}" Kcdw="{勘察单位}" Lxpzwh="{立项批准文号}" Ghxkzh="{规划许可证号}" Ydghxkzh="" Gytdsyzh="{国有土地使用证号}" Sgxkzh="{施工许可证号}" Yjdw="{移交单位}" Bz="" Key="{项目Key}">'.format(
            项目类型=项目类型,
            项目名称=项目名称,
            项目地点=项目地点,
            建设单位=建设单位,
            立项批准单位=立项批准单位,
            设计单位=设计单位,
            监理单位=监理单位,
            勘察单位=勘察单位,
            立项批准文号=立项批准文号,
            规划许可证号=规划许可证号,
            国有土地使用证号=国有土地使用证号,
            施工许可证号=施工许可证号,
            移交单位=建设单位,
            项目Key=项目Key,
        )
        '''
        self.临时文件 += r'<Project ArchivesId="001" Type="{项目类型}" Name="{项目名称}" Address="{项目地点}" ConstructorUnit="{建设单位}" RepConstructionUnit="" ApprovalUnit="" DesignUnit="{设计单位}" SupervisorUnit="{监理单位}" SurveyUnit="{勘察单位}" Longitude="0.0" Latitude="0.0" Remark="" Id="{项目Key}">'.format(
            项目类型=项目类型,
            项目名称=项目名称,
            项目地点=项目地点,
            建设单位=建设单位,
            立项批准单位=立项批准单位,
            设计单位=设计单位,
            监理单位=监理单位,
            勘察单位=勘察单位,
            立项批准文号=立项批准文号,
            规划许可证号=规划许可证号,
            国有土地使用证号=国有土地使用证号,
            施工许可证号=施工许可证号,
            移交单位=建设单位,
            项目Key=项目Key,
        )

    def 创建单位工程(self, 单体序号, 工程名称):
        '''
        self.临时文件 += r'<Sproject Jsdw="{建设单位}" Djdw="" Sgdw="{施工单位}" Sjdw="{设计单位}" Jldw="{监理单位}" Kcdw="{勘察单位}" Lxpzwh="{立项批准文号}" Ghxkzh="{规划许可证号}" Ydghxkzh="" Sgxkzh="{施工许可证号}" Gd="{高度}" Jclx="{基础类型}" Jglx="{结构类型}" Dscs="{地上层数}" Dxcs="{地下层数}" Jzmj="{建筑面积}" Kgrq="{开工日期}" Jgrq="{竣工日期}" Ydmj="{用地面积}" Zs="0" Gcys="0" Gcjs="0" Id="{单体序号}" ProjectId="1" Dwgclx="{单位工程类型}" Gcmc="{工程名称}" Gcdd="{工程地点}" Yjdw="{移交单位}" Bz="" Gcdh="{工程档号}" Key="{单体Key}">'.format(
            建设单位=建设单位,
            施工单位=施工单位,
            设计单位=设计单位,
            监理单位=监理单位,
            勘察单位=勘察单位,
            立项批准文号=立项批准文号,
            规划许可证号=规划许可证号,
            施工许可证号=施工许可证号,
            高度=高度,
            基础类型=基础类型,
            结构类型=结构类型,
            地上层数=地上层数,
            地下层数=地下层数,
            建筑面积=建筑面积,
            开工日期=开工日期,
            竣工日期=竣工日期,
            用地面积=用地面积,
            单体序号=单体序号,
            单位工程类型=项目类型,
            工程名称=工程名称[0],
            工程地点=项目地点,
            移交单位=建设单位,
            工程档号=工程档号,
            单体Key=单体Key,
        )
        '''
        self.临时文件 += r'<SingleProject ArchivesId="001" ProjectId="{项目Key}" Type="1" Number="{工程档号}" Name="{工程名称}" Address="{工程地点}" FilingPerson="" RetentionPeriod="1" SecretLevel="1" OrderNumber="{单体序号}" ClassificationNumber="" FilingDate="" TransferingUnit="" ConstructorUnit="{建设单位}" Remark="" Id="{单体Key}" RepConstructionUnit="" BuildUnit="{施工单位}" DesignUnit="{设计单位}" SurveyUnit="{勘察单位}" SupervisorUnit="{监理单位}" ApprovalUnit="" ApprovalNumber="" PlanningPermit="{规划许可证号}" LandPlanningPermit="" BuildNumber="{施工许可证号}" OwnedLandNumber="" Height="{高度}" BasicType="" StructureType="" UpFloor="{地上层数}" DownFloor="{地下层数}" FloorArea="{建筑面积}" StartDate="{开工日期}" CompletionDate="{竣工日期}" LandArea="{用地面积}" BuildinNumber="1" Budget="0" FinalAccounts="0">'.format(
            建设单位=建设单位,
            施工单位=施工单位,
            设计单位=设计单位,
            监理单位=监理单位,
            勘察单位=勘察单位,
            立项批准文号=立项批准文号,
            规划许可证号=规划许可证号,
            施工许可证号=施工许可证号,
            高度=高度,
            基础类型=基础类型,
            结构类型=结构类型,
            地上层数=地上层数,
            地下层数=地下层数,
            建筑面积=建筑面积,
            开工日期=开工日期,
            竣工日期=竣工日期,
            用地面积=用地面积,
            单体序号=单体序号,
            单位工程类型=项目类型,
            工程名称=工程名称[0],
            工程地点=项目地点,
            移交单位=建设单位,
            工程档号=工程档号,
            单体Key=单体Key,
            项目Key=项目Key,
        )
        os.mkdir(单体Key)
        shutil.move(单体Key, 项目名称)
        self.单体序号递增 += 1

    def 创建移交内容(self, fn):
        csv列表 = fn
        biguid = ""
        smalluid = ""
        大类uuid = []
        小类uuid = []
        小类父亲uuid递增 = 0
        细类父亲uuid递增 = 0
        sequence = 1

        self.临时文件 += r"<ReceiveList>"
        for i in csv列表:
            if i[1] == "x":
                biguid = str(uuid.uuid4())
                大类uuid.append(biguid)
                self.临时文件 += r'<ListItem Name="{}" Sequence="{}" ParentKey="00000000-0000-0000-0000-000000000000" Key="{}" />'.format(
                    i[0], sequence, biguid
                )
                sequence += 1

        sequence = 1
        for i in csv列表:
            if i[1] == "x":
                小类父亲uuid = 大类uuid[小类父亲uuid递增]
                小类父亲uuid递增 += 1
            if i[1] == "0":
                smalluid = str(uuid.uuid4())
                小类uuid.append(smalluid)
                self.临时文件 += r'<ListItem Name="{}" Sequence="{}" ParentKey="{}" Key="{}" />'.format(
                    i[0], sequence, 小类父亲uuid, smalluid
                )
                sequence += 1

        sequence = 1
        for i in csv列表:
            if i[1] == "0":
                细类父亲uuid = 小类uuid[细类父亲uuid递增]
                细类父亲uuid递增 += 1
                sequence = 1
            if i[1] != "0" and i[1] != "x" and i[1] != "开始页" and i[1] != ":":
                细类Key = str(uuid.uuid4())
                self.临时文件 += r'<ListItem Name="{}" Sequence="{}" ParentKey="{}" Key="{}" />'.format(
                    i[0], sequence, 细类父亲uuid, 细类Key
                )

                self.细类Key字典[i[0]] = 细类Key
                sequence += 1

        self.临时文件 += r"</ReceiveList>"

    def 创建案卷(self, fn, 案卷序号=1, 文件名称=1,文件序号=1):
        判定1 = 0
        self.案卷序号 = 案卷序号
        for i in fn:
            try:
                int(i[1])
            except ValueError:
                pass
            else:
                if i[1] == "0":
                    if 判定1 != 0:
                        self.临时文件 += r"</File>"
                        名称 = i[0]
                        创建文件项(名称)

                        os.mkdir(i[0])
                        shutil.move(i[0], 项目名称 + '\\' + 单体Key)
                        文件存储路径 = 项目名称 + '\\' + 单体Key + '\\' + i[0] + '\\'

                        self.案卷序号递增 += 1
                        self.案卷序号 += 1
                        self.总登记号 += 1
                        判定1 += 1
                    else:
                        名称 = i[0]
                        创建文件项(名称)

                        os.mkdir(i[0])
                        shutil.move(i[0], 项目名称 + '\\' + 单体Key)
                        文件存储路径 = 项目名称 + '\\' + 单体Key + '\\' + i[0] + '\\'

                        self.案卷序号递增 += 1
                        self.案卷序号 += 1
                        self.总登记号 += 1
                        判定1 += 1
                else:
                    self.临时文件 += r'<Record Wjtm="{文件名称}" Zrz="{责任者}" Bgqx="1" Mj="1" Qssj="{起始时间}" Zzsj="{终止时间}" Sl="{页数}" Gg="" Ty="" Ztc="" Fz="" Ztlx="0" Wth="" Wz="" Id="{文件ID}" FileId="{所属案卷}" Wjxh="{文件序号}" Dzwjlj="{单张文件路径}" SingleProjectReceivelistKey="{对应移交内容Key}" Key="{Key}"><MetaData><![CDATA[]]></MetaData></Record>'.format(
                        文件名称=i[0],
                        责任者=建设单位,
                        起始时间=处理日期(i[3]),
                        终止时间=处理日期(i[3]),
                        页数=str(int(i[2]) - int(i[1]) + 1),
                        文件ID=文件名称,
                        所属案卷=str(int(axml.案卷序号)-1),
                        文件序号=文件序号,
                        单张文件路径=文件存储路径 + str(文件名称) + ".pdf",
                        对应移交内容Key=self.细类Key字典[i[0]],
                        Key=str(uuid.uuid4()),
                    )

                    # 切割pdf(i[1],i[2],文件存储路径,str(案卷序号-1),str(文件名称))

                    self.文件名称递增 += 1
                    self.文件序号递增 += 1
                    self.文件名称 += 1
                    文件名称+=1
                    文件序号 += 1

    def 项目结尾(self):
        self.临时文件 += r"</File></Sproject></Project></ElectronicFileInformation>"

    def 单体结尾(self):
        self.临时文件 += r"</File></Sproject>"


if __name__ == "__main__":
    临时文件 = ""
    单体序号 = 1
    案卷序号 = 1
    文件序号 = 1
    global 文件名称,总登记号
    文件名称=1
    是否继续 = True
    while 是否继续:
        os.system("cls")
        文件名 = 打开文件()
        转换csv(文件名)
        csv列表 = 遍历csv(文件名)

        提交变量值(csv列表)

        axml = 项目xml()
        if 单体序号 == 1:
            axml.创建项目()
            项目名称 = axml.项目名称
            项目类型 = axml.项目类型
            总登记号 = axml.总登记号
            项目Key = axml.项目Key
        axml.总登记号 = 总登记号
        axml.案卷序号 = 案卷序号
        axml.创建单位工程(单体序号, 文件名.split("."[0]))
        # axml.创建移交内容(csv列表)
        axml.创建案卷(csv列表, 案卷序号, 文件名称,文件序号)
        os.remove(文件名.split(".")[0] + '.csv')

        是否继续 = input("是否继续?y/n  ")
        if 是否继续 == "y":
            axml.单体结尾()
            临时文件 += axml.临时文件
            是否继续 = True
            单体序号 += 1
            案卷序号 = axml.案卷序号
            总登记号 = axml.总登记号
            文件名称 = axml.文件名称
        else:
            axml.项目结尾()
            临时文件 += axml.临时文件
            是否继续 = False

    文件名 = 项目名称 + "_目录.xml"
    soup = BeautifulSoup(临时文件, 'xml')
    print(soup.prettify())
    with open(文件名, "w+", encoding="utf-8") as f:
        f.write(soup.prettify())
