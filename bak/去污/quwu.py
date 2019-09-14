import cv2
import os
import os.path
import time

def CompressImage(image_name):
    os.system("magick %s -resize 2480x3508! %s" % (image_name,image_name))
    print(image_name," resized")

rootdir = ".\\"
for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        apath = os.path.join(parent, filename)  # 合并成一个完整路径
        if filename.split('.')[1]=='jpg':
            #print(apath)
            CompressImage(apath)
            img = cv2.imread(apath)
            mask=cv2.imread('c:\\mask.jpg',0)
            dst_TELEA = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)
            cv2.imwrite(apath+'_.jpg',dst_TELEA)
        else:
            pass