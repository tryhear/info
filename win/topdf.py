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
rootdir = ".\\"
for parent,dirnames,filenames in os.walk(rootdir):
    for dirname in dirnames:
        thedir = parent+'\\'+dirname
        print(thedir)
        os.system("magick %s\\*.jpg %s\\%s.pdf" %(thedir,thedir,thedir))