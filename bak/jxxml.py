# -*-coding:utf-8 -*-

from lxml import etree
import prettytable
import csv
import sys,os

def jxxml(file):
    try:
        tree = etree.parse(file)
        treeview = etree.tounicode(tree, pretty_print=True)
    except:
        print('文件不存在！')
    
    dtsl = len(tree.xpath('//单位工程'))
    for i in range(dtsl):
        j = i + 1
        print(j, end=':')
        print(tree.xpath('//单位工程[%s]/@Gcmc' % j)[0])
        wjm = tree.xpath('//单位工程[%s]/@Gcmc' % j)[0]
        wjm = wjm + '.csv'
        f = open(wjm, 'w+', encoding='gbk', newline='')
        writer = csv.writer(f)

        table = prettytable.PrettyTable(["文件名", "文图号", "形成时间", "起始页", "终止页"])
        table.align["文件名"] = "r"
        table.padding_witdth = 1
        writer.writerow(["文件名", "起始页", "终止页", "形成时间", "文图号","责任者"])
        
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
            kgrq=kgrq[0].rsplit('/')
            kgrq=kgrq[0]+kgrq[1].zfill(2)+kgrq[2].zfill(2)
        except:
            kgrq=''
        jgrq = tree.xpath('//单位工程[%s]/@Jgrq' % j)
        try:
            jgrq=jgrq[0].rsplit('/')
            jgrq=jgrq[0]+jgrq[1].zfill(2)+jgrq[2].zfill(2)
        except:
            jgrq=''

        table.add_row(['项目名称', '', xmmc[0], ':', ''])
        table.add_row(['项目地点', '', xmdd[0], ':', ''])
        table.add_row(['建设单位', '', jsdw[0], ':', ''])
        table.add_row(['监理单位', '', jldw[0], ':', ''])
        table.add_row(['勘察单位', '', kcdw[0], ':', ''])
        table.add_row(['设计单位', '', sjdw[0], ':', ''])
        table.add_row(['立项批准单位', '', lxpzdw[0], ':', ''])
        table.add_row(['立项批准文号', '', lxpzwh[0], ':', ''])
        table.add_row(['规划许可证号', '', ghxkzh[0], ':', ''])
        table.add_row(['用地规划许可证号', '', ydghxkzh[0], ':', ''])
        table.add_row(['施工许可证号', '', sgxkzh[0], ':', ''])
        table.add_row(['工程档号', '', gcdh[0], ':', ''])
        table.add_row(['开工日期', '', kgrq, ':', ''])
        table.add_row(['竣工日期', '', jgrq, ':', ''])

        writer.writerow(['项目名称', ':', xmmc[0], '', '', ''])
        writer.writerow(['项目地点', ':', xmdd[0], '', '', ''])
        writer.writerow(['建设单位', ':', jsdw[0], '', '', ''])
        writer.writerow(['施工单位', ':', sgdw[0], '', '', ''])
        writer.writerow(['监理单位', ':', jldw[0], '', '', ''])
        writer.writerow(['勘察单位', ':', kcdw[0], '', '', ''])
        writer.writerow(['设计单位', ':', sjdw[0], '', '', ''])
        writer.writerow(['立项批准单位', ':', lxpzdw[0], '', '', ''])
        writer.writerow(['立项批准文号', ':', lxpzwh[0], '', '', ''])
        writer.writerow(['规划许可证号', ':', ghxkzh[0], '', '', ''])
        writer.writerow(['用地规划许可证号', ':', ydghxkzh[0], '', '', ''])
        writer.writerow(['施工许可证号', ':', sgxkzh[0], '', '', ''])
        writer.writerow(['工程档号', ':', gcdh[0], '', '', ''])
        xmid=''
        zdjh=''
        writer.writerow(['单体序号', ':', xmid, '', '', ''])
        writer.writerow(['总登记号', ':', zdjh, '', '', ''])
        writer.writerow(['开工日期', ':', kgrq, '', '', ''])
        writer.writerow(['竣工日期', ':', jgrq, '', '', ''])
        writer.writerow(['', '', '', '', ''])

        ajsl = len(tree.xpath('//单位工程[%s]/案卷' % j))
        for aj_i in range(ajsl):
            aj_j = aj_i + 1

            zdjh = tree.xpath('//单位工程[%s]/案卷[%s]/@Zdjh' % (j, aj_j))
            table.add_row(['', '', '', '', ''])

            table.add_row(
                ['第%s卷：' % aj_j + tree.xpath('//单位工程[%s]/案卷[%s]/@Ajtm' % (j, aj_j))[0], '', '', '0', ''])
            writer.writerow([tree.xpath('//单位工程[%s]/案卷[%s]/@Ajtm' %(j, aj_j))[0], '0', '', '', '', tree.xpath('//单位工程[%s]/案卷[%s]/@Zrz' %(j, aj_j))[0]])

            wjsl = len(tree.xpath('//单位工程[%s]/案卷[%s]/文件' % (j, aj_j)))
            for wj_i in range(wjsl):
                wj_j = wj_i + 1
                wjtm=tree.xpath('//单位工程[%s]/案卷[%s]/文件[%s]/@Wjtm'%(j,aj_j,wj_j))
                qsy=tree.xpath('//单位工程[%s]/案卷[%s]/文件[%s]/@Qsy'%(j,aj_j,wj_j))
                zzy=tree.xpath('//单位工程[%s]/案卷[%s]/文件[%s]/@Zzy'%(j,aj_j,wj_j))
                xcsj=tree.xpath('//单位工程[%s]/案卷[%s]/文件[%s]/@Xcsj'%(j,aj_j,wj_j))
                try:
                    xcsj=xcsj[0].rsplit('/')
                    xcsj=xcsj[0]+xcsj[1].zfill(2)+xcsj[2].zfill(2)
                except:
                    xcsj=''
                wth=tree.xpath('//单位工程[%s]/案卷[%s]/文件[%s]/@Wth'%(j,aj_j,wj_j))
                zrz=tree.xpath('//单位工程[%s]/案卷[%s]/文件[%s]/@Zrz'%(j,aj_j,wj_j))
                row=[wjtm[0],qsy[0],zzy[0],xcsj,wth[0],zrz[0]]
                #table.add_row(row)
                writer.writerow(row)
        f.close()
        '''
        try:
            # print(wjm)
            os.system('info_auto.py %s'%wjm)
            #print('-----------------------------------------------')
        except:
            pass
            # print(table)
            # print('\n')
        '''
if __name__ == "__main__":
    jxxml(sys.argv[1])