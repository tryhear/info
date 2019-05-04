# coding: utf-8
# pdf_watermark.py

import os
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
import reportlab.pdfbase.ttfonts
import datetime,time

reportlab.pdfbase.pdfmetrics.registerFont(reportlab.pdfbase.ttfonts.TTFont('song', './msyh.ttc'))
from reportlab.lib.units import mm
import xlrd
import tkinter as tk
from tkinter import filedialog

def create_watermark(content, x, y):
    """创建PDF水印模板
    """
    # 使用reportlab来创建一个PDF文件来作为一个水印文件
    c = canvas.Canvas('test.pdf', pagesize=(302 * mm, 487 * mm), bottomup=1)
    # c = canvas.Canvas('watermark.pdf')
    # c.setFont('Courier', 20)
    c.setFont('song', 17)

    # 设置水印文件
    c.saveState()
    c.translate(x, y)
    #c.rotate(90)

    # 水印文字
    c.drawString(0, 0, content)
    c.restoreState()
    # 保存水印文件

    c.save()

    pdf_watermark = PdfFileReader(open('test.pdf', 'rb'))
    return pdf_watermark
    
def create_watermark1(content, x, y):
    """创建PDF水印模板
    """
    # 使用reportlab来创建一个PDF文件来作为一个水印文件
    c = canvas.Canvas('test.pdf', pagesize=(210 * mm, 297 * mm), bottomup=1)
    # c = canvas.Canvas('watermark.pdf')
    # c.setFont('Courier', 20)
    c.setFont('song', 12)

    # 设置水印文件
    c.saveState()
    c.translate(x, y)
    #c.rotate(90)

    # 水印文字
    c.drawString(0, 0, content)
    c.restoreState()
    # 保存水印文件

    c.save()

    pdf_watermark1 = PdfFileReader(open('test.pdf', 'rb'))
    return pdf_watermark1

def add_watermark(input_pdf_file, output_pdf, pdf_watermark, output_dir='output', max_page=5):
    pdf_output = PdfFileWriter()
    input_stream = open(input_pdf_file, 'rb')
    pdf_input = PdfFileReader(input_stream)

    page = pdf_input.getPage(0)
    page.mergePage(pdf_watermark.getPage(0))
    pdf_output.addPage(page)

    # 最后输出文件
    output_stream = open(os.path.join(output_dir, os.path.basename(output_pdf)), 'wb')
    pdf_output.write(output_stream)
    output_stream.close()
    input_stream.close()
    return True


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    fn = filedialog.askopenfilename(filetypes=(('Excel源', '*.xlsx'), ('csv源', '*.csv')))
    oschdir = os.path.dirname(fn)
    os.chdir(oschdir)
    fn = fn.split('/')[-1]
    #print(fn)
    fn1 = fn.split('.')[0]
    #print(fn1)

    data = xlrd.open_workbook(fn)
    sheet1 = data.sheet_by_index(0)
    nr = sheet1.nrows
    nc = sheet1.ncols
    pdf_output = PdfFileWriter()
    pdf_output1 = PdfFileWriter()
    
    the_day = datetime.datetime.strptime(sheet1.cell_value(0,6),"%Y-%m-%d")
    next_day = datetime.datetime.strptime(sheet1.cell_value(0,6),"%Y-%m-%d")+datetime.timedelta(1)
    week = next_day.weekday()
    #print (week)
    if week==5:
        next_day = next_day+datetime.timedelta(2)
    elif week==6:
        next_day = next_day+datetime.timedelta(1)
    next_day=str(next_day)[:10]
    #print(next_day)

    for i in range(nr):
        if sheet1.cell_value(i, 0) == '':
            continue
        #print(sheet1.row_values(i))
        pdf_watermark = create_watermark(sheet1.cell_value(i, 0), 1010, 664)
        add_watermark('mba.pdf', 'tmp.pdf', pdf_watermark, output_dir='.\\')
        
        #案卷题名
        c=21
        s=sheet1.cell_value(i, 1)
        if len(s)>c:
            a,b,*_ = ([s[i:i+c] for i in range(0,len(s),c)])
            print (a,b,' 已折行')
            pdf_watermark = create_watermark(a, 960, 564)
            add_watermark('tmp.pdf', 'tmp0.pdf', pdf_watermark, output_dir='.\\')
            pdf_watermark = create_watermark(b, 960, 541)
            add_watermark('tmp0.pdf', 'tmp1.pdf', pdf_watermark, output_dir='.\\')
        else:
            pdf_watermark = create_watermark(sheet1.cell_value(i, 1), 960, 541)
            add_watermark('tmp.pdf', 'tmp1.pdf', pdf_watermark, output_dir='.\\')
        
        pdf_watermark = create_watermark(sheet1.cell_value(i, 2), 1007, 699)
        add_watermark('tmp1.pdf', 'tmp2.pdf', pdf_watermark, output_dir='.\\')
        
        pdf_watermark = create_watermark(sheet1.cell_value(i, 3), 1024, 195)
        add_watermark('tmp2.pdf', 'tmp3.pdf', pdf_watermark, output_dir='.\\')
        
        pdf_watermark = create_watermark(sheet1.cell_value(i, 4), 1154, 195)
        add_watermark('tmp3.pdf', 'tmp4.pdf', pdf_watermark, output_dir='.\\')
        
        pdf_watermark = create_watermark(sheet1.cell_value(i, 5), 960, 385)
        add_watermark('tmp4.pdf', 'tmp5.pdf', pdf_watermark, output_dir='.\\')
        
        pdf_watermark = create_watermark(str(the_day)[:10], 1024, 322)
        add_watermark('tmp5.pdf', 'tmp6.pdf', pdf_watermark, output_dir='.\\')

        input_stream = open('mba.pdf', 'rb')
        pdf_input = PdfFileReader(input_stream)
        page = pdf_input.getPage(0)
        page.mergePage(PdfFileReader(open('tmp6.pdf', 'rb')).getPage(0))
        pdf_output.addPage(page)
        # 最后输出文件
        try:
            os.makedirs('.\\卷皮')
        except:
            pass
        output_stream = open(os.path.join('卷皮', os.path.basename('卷皮 - '+fn1+'.pdf')), 'wb')
        pdf_output.write(output_stream)
        output_stream.close()
        input_stream.close()

    for i in range(nr):
        if sheet1.cell_value(i, 0) == '':   #图纸
            pdf_watermark1 = create_watermark('本案卷共有文件材料'+sheet1.cell_value(i,7)+'页，其中：', 123, 623)
            add_watermark('mbb.pdf', 'test1.pdf', pdf_watermark1, output_dir='.\\')
            pdf_watermark1 = create_watermark('文字材料0页，图样材料'+sheet1.cell_value(i,7)+'页，', 123, 591)
            add_watermark('test1.pdf', 'test3.pdf', pdf_watermark1, output_dir='.\\')
            pdf_watermark1 = create_watermark('照片0张', 123, 560)
            add_watermark('test3.pdf', 'test4.pdf', pdf_watermark1, output_dir='.\\')
            pdf_watermark1 = create_watermark(str(the_day)[:10], 389, 292)
            add_watermark('test4.pdf', 'test5.pdf', pdf_watermark1, output_dir='.\\')
            pdf_watermark1 = create_watermark(next_day, 389, 226)
            add_watermark('test5.pdf', 'test6.pdf', pdf_watermark1, output_dir='.\\')
            pdf_watermark1 = create_watermark(next_day, 389, 160)
            add_watermark('test6.pdf', 'test7.pdf', pdf_watermark1, output_dir='.\\')
        else:   #非图纸
            pdf_watermark1 = create_watermark('本案卷共有文件材料'+sheet1.cell_value(i,7)+'页，其中：', 123, 623)
            add_watermark('mbb.pdf', 'test1.pdf', pdf_watermark1, output_dir='.\\')
            pdf_watermark1 = create_watermark('文字材料'+sheet1.cell_value(i,7)+'页，图样材料0页，', 123, 591)
            add_watermark('test1.pdf', 'test3.pdf', pdf_watermark1, output_dir='.\\')
            pdf_watermark1 = create_watermark('照片0张', 123, 560)
            add_watermark('test3.pdf', 'test4.pdf', pdf_watermark1, output_dir='.\\')
            pdf_watermark1 = create_watermark(str(the_day)[:10], 389, 292)
            add_watermark('test4.pdf', 'test5.pdf', pdf_watermark1, output_dir='.\\')
            pdf_watermark1 = create_watermark(next_day, 389, 226)
            add_watermark('test5.pdf', 'test6.pdf', pdf_watermark1, output_dir='.\\')
            pdf_watermark1 = create_watermark(next_day, 389, 160)
            add_watermark('test6.pdf', 'test7.pdf', pdf_watermark1, output_dir='.\\')
        
        input_stream1 = open('mbb.pdf', 'rb')
        pdf_input1 = PdfFileReader(input_stream1)
        page = pdf_input1.getPage(0)
        page.mergePage(PdfFileReader(open('test7.pdf', 'rb')).getPage(0))
        pdf_output1.addPage(page)

        # 最后输出文件
        try:
            os.makedirs('.\\备考表')
        except:
            pass
        output_stream1 = open(os.path.join('备考表', os.path.basename('备考表 - '+fn1+'.pdf')), 'wb')
        pdf_output1.write(output_stream1)
        output_stream1.close()
        input_stream1.close()

    print('\ndone!')
