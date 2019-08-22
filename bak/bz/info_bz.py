import uuid
import os
import datetime
import shutil
import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup
from PyPDF2 import PdfFileReader, PdfFileWriter
import traceback
import re
from icecream import ic


def 打开文件():
    root = tk.Tk()
    root.withdraw()
    fn = filedialog.askopenfilename(filetypes=(("xlsx", "*.xlsx"), ("*.*", "*.*")))
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
                pass
                # ic("非双层PDF")

    except BaseException:
        pass
        # traceback.print_exc()
        #ic("文件不存在")


def 现在时间():
    now_ = datetime.datetime.now()
    datenow_ = "%s/%s/%s" % (now_.year, now_.month, now_.day)
    return datenow_ + " 0:00:00"


def 处理日期(fn):
    处理完成的日期 = ""
    if not fn.isdigit() or len(fn) < 8:
        处理完成的日期 = ""
    else:
        处理完成的日期 = fn[:4] + "-" + fn[4:6] + "-" + fn[6:8] + " 0:00:00"
    return 处理完成的日期


def 处理日期无后缀(fn):
    处理完成的日期 = ""
    if not fn.isdigit() or len(fn) < 8:
        处理完成的日期 = ""
    else:
        处理完成的日期 = fn[:4] + "-" + fn[4:6] + "-" + fn[6:8]
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


def 提交变量值(fn):
    global 项目地点, 建设单位, 设计单位, 监理单位, 勘察单位, 立项批准单位, 立项批准文号, 规划许可证号, 施工许可证号, 国有土地使用证号, 高度, 基础类型, 结构类型, 地上层数, 地下层数, 建筑面积, 用地面积, 单体Key, 施工单位, 开工日期, 竣工日期, 项目名称, 项目类型, 项目Key, 工程档号

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
            # elif i[0] == "总登记号":
            #    总登记号 = i[2]
    # os.system("cls")


def 创建文件项(名称):
    Key = str(uuid.uuid4())
    案卷档号 = (工程档号 + "-" + str(axml.案卷序号).zfill(3),)
    axml.临时文件 += r'<File ArchivesId="001" ProjectId="{项目Key}" SingleProjectId="{单体Key}" OldNumber="" Name="{案卷名称}" Num="{总登记号}" RetentionPeriod="1" SecretLevel="1" FilingBy="孙胜锴" Filinged="{立卷时间}" AuditorBy="" AuditorDate="" Remark="" Number="{案卷档号}" PreparedBy="{编制单位}" OrderNumber="{案卷序号}" Prepared="{编制时间}" StartTime="{卷内文件起始时间}" EndTime="{卷内文件终止时间}" PersonLiable="{责任者}" KeyWord="" Specifications="3" Id="{Key}">'.format(
        案卷序号=axml.案卷序号,
        单体序号=单体序号,
        总登记号=axml.总登记号,
        案卷档号=案卷档号[0],
        案卷名称=名称,
        编制单位=建设单位,
        移交单位=建设单位,
        立卷时间=现在时间(),
        编制时间=现在时间(),
        审核时间=审核时间(),
        卷内文件起始时间="",
        卷内文件终止时间="",
        责任者=建设单位,
        项目Key=项目Key,
        单体Key=单体Key,
        Key=Key,
    )
    return Key, 案卷档号


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
    文件名称 = 1
    项目Key = ""

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

        总登记号 = input("总登记号:")
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

        self.项目名称 = 项目名称
        self.项目类型 = 项目类型
        self.总登记号 = 总登记号
        self.项目Key = 项目Key

        if os.path.exists("项目名称"):
            shutil.rmtree(项目名称, True)
            os.mkdir(项目名称)
        else:
            os.mkdir(项目名称)

        self.临时文件 += r'<?xml version="1.0" encoding="utf-8"?>'
        self.临时文件 += r"<ElectronicFileInformation>"
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

    def 创建案卷(self, fn, 案卷序号=1, 文件序号=1):
        判定1 = 0
        self.案卷序号 = 案卷序号

        for i in fn:
            try:
                int(i[1])
            except ValueError:
                pass
            else:
                if i[1] == "0":
                    单卷序号 = 0
                    if 判定1 != 0:
                        self.临时文件 += r"</File>"
                        名称 = i[0]
                        案卷Key, 案卷档号 = 创建文件项(名称)

                        os.mkdir(i[0])
                        shutil.move(i[0], 项目名称 + "\\" + 单体Key)
                        文件存储路径 = 项目名称 + "\\" + 单体Key + "\\" + i[0] + "\\"

                        self.案卷序号递增 += 1
                        self.案卷序号 += 1
                        self.总登记号 += 1
                        判定1 += 1
                    else:
                        名称 = i[0]
                        案卷Key, 案卷档号 = 创建文件项(名称)

                        os.mkdir(i[0])
                        shutil.move(i[0], 项目名称 + "\\" + 单体Key)
                        文件存储路径 = 项目名称 + "\\" + 单体Key + "\\" + i[0] + "\\"

                        self.案卷序号递增 += 1
                        self.案卷序号 += 1
                        self.总登记号 += 1
                        判定1 += 1
                else:
                    单卷序号 += 1
                    文件Key = str(uuid.uuid4())
                    self.临时文件 += r'<RecordPaper Number="{文件档号}" Name="{文件名称}" PersonLiable="{责任者}" RetentionPeriod="1" SecretLevel="0" StartTime="{起始时间}" EndTime="{终止时间}" Amount="{页数}" Specifications="" Tabloid="" KeyWord="" Remark="" Qsy="{起始页}" Zzy="{终止页}" CarrierType="0" DrawingNumber="" Text="" RecordType="" Manuscript="" ArchivesId="001" FilesId="{所属案卷Key}" SingleProjectId="{所属单体Key}" ProjectId="{所属项目Key}" TransferContentId="" Type="0" SortNum="{文件序号}" OrderNumber="{文件序号}" FileUrl="{单张文件路径}" Id="{Key}"/>'.format(
                        文件名称=i[0],
                        文件档号=案卷档号[0] + "-" + str(单卷序号).zfill(3),
                        责任者=建设单位,
                        起始时间=处理日期无后缀(i[3]),
                        终止时间=处理日期无后缀(i[3]),
                        页数=str(int(i[2]) - int(i[1]) + 1),
                        所属案卷=str(int(axml.案卷序号) - 1),
                        文件序号=文件序号,
                        Key=文件Key,
                        单张文件路径=文件存储路径 + 文件Key + ".pdf",
                        起始页=str(int(i[1])),
                        终止页=str(int(i[2])),
                        所属项目Key=项目Key,
                        所属单体Key=单体Key,
                        所属案卷Key=案卷Key,
                    )
                    # ic(axml.案卷序号-1)
                    切割pdf(i[1], i[2], 文件存储路径, str(axml.案卷序号 - 1), 文件Key)

                    self.文件序号递增 += 1
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
    global 文件名称, 总登记号
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
        axml.创建案卷(csv列表, 案卷序号, 文件序号)
        os.remove(文件名.split(".")[0] + ".csv")

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

    文件名 = 项目名称 + ".xml"
    soup = BeautifulSoup(临时文件, "xml")
    # print(soup.prettify())
    with open(文件名, "w+", encoding="utf-8") as f:
        f.write(soup.prettify())
