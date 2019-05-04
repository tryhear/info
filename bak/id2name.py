# -*-coding:utf-8 -*-

from lxml import etree
import sys
import xlsxwriter


def jxxml(file):
    try:
        tree = etree.parse(file)
    except BaseException:
        print('文件不存在！')

    dtsl = len(tree.xpath('//单位工程'))
    for i in range(dtsl):
        j = i + 1
        print(j, end=':')
        print(tree.xpath('//单位工程[%s]/@Gcmc' % j)[0])
        wjm = tree.xpath('//单位工程[%s]/@Gcmc' % j)[0]

        workbook = xlsxwriter.Workbook(wjm + '检索表.xlsx')
        worksheet = workbook.add_worksheet()

        ajsl = len(tree.xpath('//单位工程[%s]/案卷' % j))

        worksheet.write(0, 0, '题名')
        worksheet.write(0, 1, '文件名')

        xrh = 1
        test1 = 0
        for aj_i in range(ajsl):
            aj_j = aj_i + 1
            wjsl = len(tree.xpath('//单位工程[%s]/案卷[%s]/文件' % (j, aj_j)))

            if test1 > 0:
                xrh += 1
            xh = 1
            for wj_i in range(wjsl):
                wj_j = wj_i + 1
                wjtm = tree.xpath(
                    '//单位工程[%s]/案卷[%s]/文件[%s]/@Wjtm' %
                    (j, aj_j, wj_j))
                wjid = tree.xpath(
                    '//单位工程[%s]/案卷[%s]/文件[%s]/@Id' %
                    (j, aj_j, wj_j))

                worksheet.write(xrh, 0, wjtm[0])
                worksheet.write(xrh, 1, wjid[0]+'.pdf')
                xh += 1
                xrh += 1
                test1 += 1

        workbook.close()

if __name__ == "__main__":
    jxxml(sys.argv[1])
