    
import cv2
import os
import os.path
import time

def CompressImage(image_name):
    os.system("magick %s -resize 1654x2339! %s" % (image_name,image_name))
    print(image_name," resized")

rootdir = ".\\"
for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        apath = os.path.join(parent, filename)  # 合并成一个完整路径
        if filename.split('.')[1]=='jpg':
            #print(apath)
            CompressImage(apath)
            img = cv2.imread(apath)
            mask=cv2.imread('c:\\mask200.jpg',0)
            bg=cv2.imread('c:\\backgroud200.jpg')
            #dst_TELEA = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)
            dst=cv2.bitwise_or(img,bg,mask=mask)
            dst=cv2.add(dst,img)
            #cv2.imwrite(apath.split('\\')[-1].split('.')[0]+'_.jpg',dst)
            cv2.imwrite(apath,dst)
        else:
            pass