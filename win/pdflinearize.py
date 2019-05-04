import os
import os.path
 
def CompressImage(image_name):
    os.system("magick -resize \"3000x4000\" %s %s" % (image_name,image_name))
            
def CompressAll():
    ext_names = ['.JPG','.jpg','.jepg']
    for each_image in os.listdir('./'):
        for ext_name in ext_names:
            if each_image.endswith(ext_name):
                CompressImage(each_image)
                break

# CompressAll()
'''
rootdir = ".\\"
for parent,dirnames,filenames in os.walk(rootdir):
    for dirname in dirnames:
        thedir = parent+'\\'+dirname
        print(thedir)
        os.system("magick %s\\*.jpg %s\\%s.pdf" %(thedir,thedir,thedir))
       

# PdfLinearize()
rootdir = ".\\"
for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        if filename.endswith('.pdf'):
            for dirname in dirnames:
                thedir=parent+'\\'+dirname
                print(thedir)
                thefilename = thedir+'\\'+filename
                print(thefilename)
                print("qpdf --linearize %s %s.1" %(thefilename,thefilename))
                os.system("qpdf --linearize %s %s.1" %(thefilename,thefilename))
                
''' 

# PdfLinearize()
#rootdir = ".\\"
rootdir=os.getcwd()
for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        if filename.endswith('.pdf'):
            thefile=parent+'\\'+filename
            print (parent+'\\'+filename)
            #print (os.path.dirname(thefile))
            try:
                os.chdir(os.path.dirname(thefile))
            except:
                os.chdir(rootdir)
            #print("qpdf --linearize %s %s.1" %(thefile,thefile))
            os.system("qpdf --linearize %s %s.1" %(filename,filename))
            #print("move %s.1 %s /Y" % (filename,filename))
            os.system("move /Y %s.1 %s>logo.txt" %(filename,filename))
            os.system("del /F logo.txt")
                