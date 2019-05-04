# -*-coding:utf-8 -*-

from lxml import etree
import prettytable
import sys
import os
import xlsxwriter


def jxxml(file):
    try:
        tree = etree.parse(file)
        treeview = etree.tounicode(tree, pretty_print=True)
    except BaseException:
        print('文件不存在！')

    dtsl = len(tree.xpath('//单位工程'))
    for i in range(dtsl):
        j = i + 1
        print(j, end=':')
        print(tree.xpath('//单位工程[%s]/@Gcmc' % j)[0])
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
    jxxml(sys.argv[1])
