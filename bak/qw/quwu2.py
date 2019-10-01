    
import cv2
import numpy as np
import os
import os.path
import time
#np.set_printoptions(threshold=np.nan)

def baweraopen(image,size):
    '''
    @image:单通道二值图，数据类型uint8
    @size:欲去除区域大小(黑底上的白区域)
    '''
    output=image.copy()
    nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(image)
    for i in range(1,nlabels-1):
        regions_size=stats[i,4]
        if regions_size<size:
            x0=stats[i,0]
            y0=stats[i,1]
            x1=stats[i,0]+stats[i,2]
            y1=stats[i,1]+stats[i,3]
            for row in range(y0,y1):
                for col in range(x0,x1):
                    if labels[row,col]==i:
                        output[row,col]=0
    return output

def CompressImage(image_name):
    os.system("magick %s -resize 2480x3508! %s" % (image_name,image_name))
    print(image_name," resized")

rootdir = ".\\"
for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        apath = os.path.join(parent, filename)  # 合并成一个完整路径
        if filename.split('.')[1]=='jpg':
            print(apath+" okey!")
            #CompressImage(apath)
            img = cv2.imread(apath).astype(np.uint8)
            bg=np.ones(img.shape).astype(np.uint8)

            img_mask=cv2.bitwise_not(cv2.imread(apath,0))
            img_mask=baweraopen(img_mask,400)
            img_mask=img_mask.astype(np.uint8)
            ret,mask=cv2.threshold(img_mask,35,255,cv2.THRESH_BINARY)
            mask=cv2.bitwise_not(mask)
            

            dst=cv2.bitwise_or(img,bg,mask=mask)
            dst=cv2.add(dst,img)
            '''
            b, g, r = cv2.split(dst)
            b = cv2.equalizeHist(b)
            g = cv2.equalizeHist(g)
            
            r[r > 230] = 255
            r = cv2.equalizeHist(r)
            #g[g > 100] = 255
            #b[b > 100] = 255
            O = cv2.merge([b,g,r])
            '''
            #cv2.imwrite(apath+"_.jpg",dst)
            cv2.imwrite(apath,dst)

            
            #cv2.imwrite(apath.split('\\')[-1].split('.')[0]+'_.jpg',dst)
        else:
            pass