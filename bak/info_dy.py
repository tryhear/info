# -*- coding: utf-8 -*-

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

# import pysnooper


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
                    # traceback.print_exc()

            if not isdouble:
                pass
                # ic("非双层PDF")

    except BaseException:
        # pass
        traceback.print_exc()
        # ic("文件不存在")


def 现在时间():
    now_ = datetime.datetime.now()
    datenow_ = "%s-%s-%s" % (now_.year, now_.month, now_.day)
    return datenow_


def 大后天():
    theday = datetime.date.today() + datetime.datedelta(day=2)
    return "%s-%s-%s" % (theday.year, theday.month, theday.day)


def 处理日期(fn):
    处理完成的日期 = ""
    if not fn.isdigit() or len(fn) < 8:
        处理完成的日期 = ""
    else:
        处理完成的日期 = fn[:4] + "-" + fn[4:6] + "-" + fn[6:8]
    return 处理完成的日期


def 处理日期无后缀(fn):
    处理完成的日期 = 现在时间()
    if not fn.isdigit() or len(fn) < 8:
        处理完成的日期 = 现在时间()
    else:
        try:
            处理完成的日期 = "%s-%s-%s" % (datetime.date(fn[:4], fn[4:6], fn[6:8]))
        except:
            处理完成的日期 = 现在时间()
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
    datenow_ = "%s-%s-%s" % (审核时间.year, 审核时间.month, 审核时间.day)
    return datenow_


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
    global 项目地点, 建设单位, 设计单位, 监理单位, 勘察单位, 立项批准单位, 立项批准文号, 规划许可证号, 施工许可证号, 国有土地使用证号, 高度, 基础类型, 结构类型, 地上层数, 地下层数, 建筑面积, 用地面积, 单体Key, 施工单位, 开工日期, 竣工日期, 项目名称, 项目类型, 项目Key, 工程档号, 档案馆号, 项目编号, 工程预算, 工程结算, 用地规划许可证号, 合同价, 资金来源, 设备用房建筑面积, 居住建筑面积, 公建建筑面积, 配套设施建筑面积, 工业建筑面积, 车位建筑面积, 其他建筑面积, 总设容建筑面积, 地下总建筑面积, 地上总建筑面积, 住宅面积, 地上公建面积, 地下公建面积, 主要用途, 建筑物功能分类_数字, 建筑状态_数字, 外墙形式, 地上车位数, 地下车位数, 户数, 施工图审查单位, 工程主要检测单位, 安全监督单位, 质量监督单位, 合同工期, 实际工期, 环保验收日期, 防雷验收日期, 规划验收日期, 竣工验收日期, 园林验收日期, 绿色建筑评测日期, 联合验收日期, 消防验收日期, 施工专业分包单位, 商砼预拌单位, 绿地率, 建筑密度, 总停车位数, 经度, 纬度, 栋数, 总长度, 总投资金额, 立卷人, 审核人, 分类大纲代码, 砂浆预拌单位

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
            elif i[0] == "档案馆号":
                档案馆号 = i[2]
            elif i[0] == "项目编号":
                项目编号 = i[2]
            elif i[0] == "工程档号":
                工程档号 = i[2]
            elif i[0] == "开工日期":
                try:
                    开工日期 = 处理日期无后缀(i[2])
                except:
                    开工日期 = ""
            elif i[0] == "竣工日期":
                try:
                    竣工日期 = 处理日期无后缀(i[2])
                except:
                    竣工日期 = ""
            elif i[0] == "工程预算":
                工程预算 = i[2]
            elif i[0] == "工程结算":
                工程结算 = i[2]
            elif i[0] == "用地规划许可证号":
                用地规划许可证号 = i[2]
            elif i[0] == "施工专业分包单位":
                施工专业分包单位 = i[2]
            elif i[0] == "合同价":
                合同价 = i[2]
            elif i[0] == "总投资金额":
                总投资金额 = i[2]
            elif i[0] == "资金来源":
                资金来源 = i[2]
            elif i[0] == "设备用房建筑面积":
                设备用房建筑面积 = i[2]
            elif i[0] == "居住建筑面积":
                居住建筑面积 = i[2]
            elif i[0] == "公建建筑面积":
                公建建筑面积 = i[2]
            elif i[0] == "配套设施建筑面积":
                配套设施建筑面积 = i[2]
            elif i[0] == "工业建筑面积":
                工业建筑面积 = i[2]
            elif i[0] == "车位建筑面积":
                车位建筑面积 = i[2]
            elif i[0] == "其他建筑面积":
                其他建筑面积 = i[2]
            elif i[0] == "总设容建筑面积":
                总设容建筑面积 = i[2]
            elif i[0] == "地下总建筑面积":
                地下总建筑面积 = i[2]
            elif i[0] == "地上总建筑面积":
                地上总建筑面积 = i[2]
            elif i[0] == "住宅面积":
                住宅面积 = i[2]
            elif i[0] == "地上公建面积":
                地上公建面积 = i[2]
            elif i[0] == "地下公建面积":
                地下公建面积 = i[2]
            elif i[0] == "主要用途":
                主要用途 = i[2]
            elif i[0] == "建筑物功能分类_数字":
                建筑物功能分类_数字 = i[2]
            elif i[0] == "建筑状态_数字":
                建筑状态_数字 = i[2]
            elif i[0] == "外墙形式":
                外墙形式 = i[2]
            elif i[0] == "总停车位数":
                总停车位数 = i[2]
            elif i[0] == "地上车位数":
                地上车位数 = i[2]
            elif i[0] == "地下车位数":
                地下车位数 = i[2]
            elif i[0] == "户数":
                户数 = i[2]
            elif i[0] == "商砼预拌单位":
                商砼预拌单位 = i[2]
            elif i[0] == "绿地率":
                绿地率 = i[2]
            elif i[0] == "建筑密度":
                建筑密度 = i[2]
            elif i[0] == "经度":
                经度 = i[2]
            elif i[0] == "纬度":
                纬度 = i[2]
            elif i[0] == "栋数":
                栋数 = i[2]
            elif i[0] == "总长度":
                总长度 = i[2]
            elif i[0] == "施工图审查单位":
                施工图审查单位 = i[2]
            elif i[0] == "工程主要检测单位":
                工程主要检测单位 = i[2]
            elif i[0] == "安全监督单位":
                安全监督单位 = i[2]
            elif i[0] == "质量监督单位":
                质量监督单位 = i[2]
            elif i[0] == "合同工期":
                合同工期 = i[2]
            elif i[0] == "实际工期":
                实际工期 = i[2]
            elif i[0] == "环保验收日期":
                try:
                    环保验收日期 = 处理日期无后缀(i[2])
                except:
                    环保验收日期 = 现在时间()
            elif i[0] == "防雷验收日期":
                try:
                    防雷验收日期 = 处理日期无后缀(i[2])
                except:
                    防雷验收日期 = 现在时间()
            elif i[0] == "规划验收日期":
                try:
                    规划验收日期 = 处理日期无后缀(i[2])
                except:
                    规划验收日期 = 现在时间()
            elif i[0] == "竣工验收日期":
                try:
                    竣工验收日期 = 处理日期无后缀(i[2])
                except:
                    竣工验收日期 = 现在时间()
            elif i[0] == "园林验收日期":
                try:
                    园林验收日期 = 处理日期无后缀(i[2])
                except:
                    园林验收日期 = 现在时间()
            elif i[0] == "绿色建筑评测日期":
                try:
                    绿色建筑评测日期 = 处理日期无后缀(i[2])
                except:
                    绿色建筑评测日期 = 现在时间()
            elif i[0] == "联合验收日期":
                try:
                    联合验收日期 = 处理日期无后缀(i[2])
                except:
                    联合验收日期 = 现在时间()
            elif i[0] == "消防验收日期":
                try:
                    消防验收日期 = 处理日期无后缀(i[2])
                except:
                    消防验收日期 = 现在时间()
            elif i[0] == "立卷人":
                立卷人 = i[2]
            elif i[0] == "审核人":
                审核人 = i[2]
            elif i[0] == "分类大纲代码":
                分类大纲代码 = i[2]
            elif i[0] == "砂浆预拌单位":
                砂浆预拌单位 = i[2]

            # elif i[0] == "总登记号":
            #    总登记号 = i[2]
    # os.system("cls")


def 创建文件项(名称):
    Key = str(uuid.uuid4())
    案卷档号 = (工程档号 + "-" + str(axml.案卷序号).zfill(3),)
    axml.临时文件 += r'<File ArchivesId="{档案馆号}" ProjectId="{项目Key}" SingleProjectId="{单体Key}" OldNumber="" Name="{案卷名称}" Num="{总登记号}" RetentionPeriod="2" SecretLevel="1" FilingBy="{立卷人}" Filinged="{立卷时间}" Auditored="{审核时间}" AuditorBy="{审核人}" Remark="" Number="{案卷档号}" PreparedBy="{编制单位}" OrderNumber="{案卷序号}" Prepared="{编制时间}" StartTime="{卷内文件起始时间}" EndTime="{卷内文件终止时间}" PersonLiable="{责任者}" KeyWord="无" Specifications="3" Id="{Key}" Classification="{分类大纲代码}">'.format(
        案卷序号=axml.案卷序号,
        单体序号=单体序号,
        档案馆号=档案馆号,
        # 总登记号=axml.总登记号,
        总登记号="0",
        案卷档号=案卷档号[0],
        案卷名称=名称,
        编制单位=建设单位,
        移交单位=建设单位,
        立卷时间=现在时间(),
        编制时间=现在时间(),
        审核时间=审核时间(),
        卷内文件起始时间=现在时间(),
        卷内文件终止时间=现在时间(),
        责任者=建设单位,
        项目Key=项目Key,
        单体Key=单体Key,
        Key=Key,
        立卷人=立卷人,
        审核人=审核人,
        分类大纲代码=分类大纲代码,
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
        # 项目名称 = 文件名.split(".")[0]
        if 项目名称 == "":
            项目名称 = "项目名称"

        try:
            shutil.rmtree(项目名称, True)
        except BaseException:
            traceback.print_exc()

        # 项目类型 = input("项目类型（0、1、2）：")
        项目类型 = "1"
        # if 项目类型 == "":
        #    项目类型 = "1"

        # 总登记号 = input("总登记号:")
        总登记号 = 1
        # if 总登记号 == "":
        #    总登记号 = 1
        # else:
        #    try:
        #        总登记号 = int(总登记号)
        #    except BaseException:
        #        总登记号 = 1

        # 项目Key = input("项目Key:")
        # if 项目Key == "":
        #    项目Key = "项目Key未填"
        # 档案馆号="618100"
        # 项目编号="000003"

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
        self.临时文件 += r'<Project ArchivesId="{档案馆号}" Type="{项目类型}" Number="{项目编号}" Name="{项目名称}" Address="{项目地点}" ConstructorUnit="{建设单位}" RepConstructionUnit="无" ApprovalUnit="{立项批准单位}" DesignUnit="{设计单位}" SupervisorUnit="{监理单位}" SurveyUnit="{勘察单位}" Longitude="{经度}" Latitude="{纬度}" Remark="" Id="{项目Key}" projectUse="1" keyProject="0" buildNature="1" greenSpaceRate="{绿地率}" buildDensity="{建筑密度}" totalParkSpace="{总停车位数}" upperParkSpace="{地上车位数}" lowerParkSpace="{地下车位数}" households="{栋数}" totalLength="{总长度}" totalInvestmentAmount="{总投资金额}" budget="{工程预算}" finalAccounts="{工程结算}" contractPrice="{合同价}" funded="{资金来源}" deviceBuildArea="{设备用房建筑面积}" liveBuildArea="{居住建筑面积}" publicBuildArea="{公建建筑面积}" supporteFacilityBuildArea="{配套设施建筑面积}" industryBuildArea="{工业建筑面积}" parkingBuildArea="{车位建筑面积}" otherBuildArea="{其他建筑面积}" totleDesignBuildArea="{总设容建筑面积}" lowerTotalBuildArea="{地下总建筑面积}" upperTotalBuildArea="{地上总建筑面积}" buildUnit="{施工单位}" buildMajorPackageUnit="{施工专业分包单位}" ssybUnit="{商砼预拌单位}" sgtscUnit="{施工图审查单位}" gczyjcUnit="{工程主要检测单位}" safeControlUnit="{安全监督单位}" qualityControlUnit="{质量监督单位}" OrderNumber="1" SyybUnit="{砂浆预拌单位}" Province="022" City="022011" Dist="022011003" BuildNumber="{栋数}">'.format(
            项目类型=项目类型,
            档案馆号=档案馆号,
            项目编号=项目编号,
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
            施工单位=施工单位,
            施工专业分包单位=施工专业分包单位,
            商砼预拌单位=商砼预拌单位,
            砂浆预拌单位=砂浆预拌单位,
            工程主要检测单位=工程主要检测单位,
            安全监督单位=安全监督单位,
            质量监督单位=质量监督单位,
            施工图审查单位=施工图审查单位,
            绿地率=绿地率,
            建筑密度=建筑密度,
            总停车位数=总停车位数,
            地上车位数=地上车位数,
            地下车位数=地下车位数,
            经度=经度,
            纬度=纬度,
            栋数=栋数,
            总长度=总长度,
            总投资金额=总投资金额,
            工程预算=工程预算,
            工程结算=工程结算,
            合同价=合同价,
            资金来源=资金来源,
            设备用房建筑面积=设备用房建筑面积,
            居住建筑面积=居住建筑面积,
            公建建筑面积=公建建筑面积,
            配套设施建筑面积=配套设施建筑面积,
            工业建筑面积=工业建筑面积,
            车位建筑面积=车位建筑面积,
            其他建筑面积=其他建筑面积,
            总设容建筑面积=总设容建筑面积,
            地下总建筑面积=地下总建筑面积,
            地上总建筑面积=地上总建筑面积,
        )

    def 创建单位工程(self, 单体序号, 工程名称):
        self.临时文件 += r'<SingleProject ArchvesId="{档案馆号}" ProjectId="{项目Key}" Type="1" Number="{工程档号}" Name="{工程名称}" Address="{工程地点}" FilingPerson="{归档人}" RetentionPeriod="2" SecretLevel="1" OrderNumber="{单体序号}" Classification="{分类大纲代码}" FilingDate="{归档时间}" TransferingUnit="{移交单位}" ConstructorUnit="{建设单位}" Remark="" Id="{单体Key}" RepConstructionUnit="无" BuildUnit="{施工单位}" DesignUnit="{设计单位}" SurveyUnit="{勘察单位}" SupervisorUnit="{监理单位}" ApprovalUnit="{立项批准单位}" ApprovalNumber="{立项批准文号}" PlanningPermit="{规划许可证号}" LandPlanningPermit="{用地规划许可证号}" BuildNumber="{施工许可证号}" OwnedLandNumber="{国有土地使用证号}" Height="{高度}" BasicType="{基础类型}" StructureType="{结构类型}" UpFloor="{地上层数}" DownFloor="{地下层数}" FloorArea="{建筑面积}" StartDate="{开工日期}" CompletionDate="{竣工日期}" LandArea="{用地面积}" BuildinNumber="1" Budget="{工程预算}" FinalAccounts="{工程结算}" residenceArea="{住宅面积}" upperPublicArea="{地上公建面积}" lowerPublicArea="{地下公建面积}" mainPurpose="{主要用途}" functionType="{建筑物功能分类_数字}" outWallType="{外墙形式}" buildState="{建筑状态_数字}" upperParkSpace="{地上车位数}" lowerParkSpace="{地下车位数}" usePeriod="70" households="{户数}" defenseIntensity="8" fireResistantLevel="1" humanDefenseLevel="1" antiSeismicLevel="1" defenseThunderCheck="合格" buildSafeLevel="1" sgtscUnit="{施工图审查单位}" gczyjcUnit="{工程主要检测单位}" safeControlUnit="{安全监督单位}" qualityControlUnit="{质量监督单位}" contractStartDate="{合同开工时间}" contractCompletionDate="{合同竣工时间}" contractConstructionPeriod="{合同工期}" realConstructionPeriod="{实际工期}" designUseYear="50" landUseYear="70" greenestAcceptDate="{环保验收日期}" defthunderAcceptDate="{防雷验收日期}" planningAcceptDate="{规划验收日期}" fireAcceptDate="{消防验收日期}" gardenAcceptDate="{园林验收日期}" greenEvalDate="{绿色建筑评测日期}" unionAcceptDate="{联合验收日期}" CompletionAcceptDate="{竣工验收日期}" Province="022" City="022011" Dist="022011003" Longitude="{经度}" Latitude="{纬度}" BuildMajorPackageUnit="{施工专业分包单位}" SsybUnit="{商砼预拌单位}" SyybUnit="{砂浆预拌单位}">'.format(
            建设单位=建设单位,
            施工单位=施工单位,
            档案馆号=档案馆号,
            设计单位=设计单位,
            监理单位=监理单位,
            勘察单位=勘察单位,
            立项批准单位=立项批准单位,
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
            合同开工时间=开工日期,
            合同竣工时间=竣工日期,
            工程预算=工程预算,
            工程结算=工程结算,
            国有土地使用证号=国有土地使用证号,
            用地规划许可证号=用地规划许可证号,
            住宅面积=住宅面积,
            地上公建面积=地上公建面积,
            地下公建面积=地下公建面积,
            主要用途=主要用途,
            建筑物功能分类_数字=建筑物功能分类_数字,
            外墙形式=外墙形式,
            建筑状态_数字=建筑状态_数字,
            地上车位数=地上车位数,
            地下车位数=地下车位数,
            户数=户数,
            施工图审查单位=施工图审查单位,
            工程主要检测单位=工程主要检测单位,
            安全监督单位=安全监督单位,
            质量监督单位=质量监督单位,
            合同工期=合同工期,
            实际工期=实际工期,
            环保验收日期=环保验收日期,
            防雷验收日期=防雷验收日期,
            规划验收日期=规划验收日期,
            竣工验收日期=竣工验收日期,
            园林验收日期=园林验收日期,
            绿色建筑评测日期=绿色建筑评测日期,
            联合验收日期=联合验收日期,
            消防验收日期=消防验收日期,
            分类大纲代码=分类大纲代码,
            归档人=立卷人,
            归档时间=现在时间(),
            经度=经度,
            纬度=纬度,
            施工专业分包单位=施工专业分包单位,
            商砼预拌单位=商砼预拌单位,
            砂浆预拌单位=砂浆预拌单位,
        )
        try:
            shutil.rmtree(项目名称)
        except:
            pass
        os.mkdir(单体Key)
        shutil.move(单体Key, 项目名称)
        self.单体序号递增 += 1

    # @pysnooper.snoop()
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
                    if "图" in i[0]:
                        载体类型 = "1"
                    else:
                        载体类型 = "0"
                    # ic(i[0],载体类型)
                    单卷序号 = 0
                    if 判定1 != 0:  # 非第一卷
                        self.临时文件 += r"</File>"
                        名称 = i[0]
                        案卷Key, 案卷档号 = 创建文件项(名称)

                        os.makedirs(
                            os.path.join(os.getcwd(), 项目名称 + "\\" + 单体Key + "\\") + i[0]
                        )
                        # shutil.move(i[0],os.path.join(os.getcwd(),项目名称 + "\\" + 单体Key))
                        文件存储路径 = 项目名称 + "\\" + 单体Key + "\\" + i[0] + "\\"

                        self.案卷序号递增 += 1
                        self.案卷序号 += 1
                        self.总登记号 += 1
                        判定1 += 1
                    else:  # 第一卷
                        名称 = i[0]
                        案卷Key, 案卷档号 = 创建文件项(名称)

                        os.makedirs(
                            os.path.join(os.getcwd(), 项目名称 + "\\" + 单体Key + "\\") + i[0]
                        )
                        文件存储路径 = 项目名称 + "\\" + 单体Key + "\\" + i[0] + "\\"

                        self.案卷序号递增 += 1
                        self.案卷序号 += 1
                        self.总登记号 += 1
                        判定1 += 1
                else:
                    单卷序号 += 1
                    文件Key = str(uuid.uuid4())

                    # ic(">>",i[0],载体类型)
                    self.临时文件 += r'<RecordPaper Number="{文件档号}" Name="{文件名称}" PersonLiable="{责任者}" RetentionPeriod="2" SecretLevel="1" StartTime="{起始时间}" EndTime="{终止时间}" Amount="{页数}" Specifications="无" Tabloid="无" KeyWord="无" Remark="" Qsy="{起始页}" Zzy="{终止页}" CarrierType="{载体类型}" DrawingNumber="{文图号}" Text="无" RecordType="中文" Manuscript="无" ArchivesId="{档案馆号}" FilesId="{所属案卷Key}" SingleProjectId="{所属单体Key}" ProjectId="{所属项目Key}" TransferContentId="" Type="0" SortNum="{文件序号}" OrderNumber="{文件序号}" FileUrl="{单张文件路径}" Id="{Key}"/>'.format(
                        文件名称=i[0],
                        档案馆号=档案馆号,
                        文件档号=案卷档号[0] + "-" + str(单卷序号).zfill(3),
                        责任者=建设单位,
                        文图号=i[4],
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
                        载体类型=载体类型,
                    )
                    # ic(axml.案卷序号-1)
                    切割pdf(i[1], i[2], 文件存储路径, str(axml.案卷序号 - 1), 文件Key)
                    print(str(axml.案卷序号 - 1) + ".pdf  >>>  " + 文件Key + ".pdf")

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
            # 案卷序号 = axml.案卷序号
            案卷序号 = 1
            总登记号 = axml.总登记号
            文件名称 = axml.文件名称
            # axml.案卷序号 = 1
        else:
            axml.项目结尾()
            临时文件 += axml.临时文件
            是否继续 = False

    文件名 = 项目名称 + ".xml"
    soup = BeautifulSoup(临时文件, "xml")
    # print(soup.prettify())
    with open(文件名, "w+", encoding="utf-8") as f:
        f.write(soup.prettify())
