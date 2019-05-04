from PyPDF2 import PdfFileReader,PdfFileWriter
from io import BytesIO

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

from pdfrw import PdfReader
import argparse
import os

from shutil import move

TARGET_FOLDER = "processed_pdf"
FAKE_STRING = "             "   #empty string
#FAKE_STRING = "     test  "

def getPageWithStr(str=FAKE_STRING):
    packet = BytesIO()
    # create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)
    can.drawString(10, 10, str)
    can.save()
    #move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    return new_pdf.getPage(0)

def process_file(infile, outfile):
    # read your existing PDF
    existing_pdf = PdfFileReader(open(infile, "rb"))
    print (infile + ' is processed.')
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page

    for i in range(existing_pdf.numPages):
        page = existing_pdf.getPage(i)
        page.mergePage(getPageWithStr())
        output.addPage(page)
    # finally, write "output" to a real file
    outputStream = open(outfile, "wb")
    output.write(outputStream)
    outputStream.close()

def isDoublePdf(fn):
    x = PdfReader(fn)
    return True if x.pages[0].Resources.Font else False

def walkPath(path):
    flag = False
    for parent, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(".pdf"):
                fn = os.path.join(parent, filename)
                # print(fn)
                if not isDoublePdf(fn):
                    if not flag:
                        flag = True
                        print("Below files is not double side pdf:")
                        print("="*30)
                        # if not os.path.exists(TARGET_FOLDER):
                            # os.mkdir(TARGET_FOLDER)
                    # print(filename)
                    tmp_file = os.path.join(path, '.tmp_' + filename)
                    process_file(fn, tmp_file)
                    move(tmp_file, fn)


    return flag

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dir", required=False, help="path")
args = vars(ap.parse_args())
print("="*30)
flag = walkPath(args["dir"] or os.curdir)
if not flag:
    print("All files is double side")
print("="*30)
print("Generate faked pdf done")
