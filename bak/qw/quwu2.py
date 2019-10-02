    
import cv2
import numpy as np
import os,sys
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
    #os.system("magick %s -resize 1654x2339! %s" % (image_name,image_name))
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
            
            shape=img_mask.shape
            if shape[0]>3690 or shape[1]>3690:
                print('too big!',shape)
                continue
            w=int(shape[1]*0.6)
            h=int(shape[0]*0.6)
            #print(shape,w,h)
            
            p1=((int((shape[1]-w)/2)),int((shape[0]-h)/2))
            p2=((int((shape[1]/2)+(w/2)),int((shape[0]-h)/2)))
            p3=((int((shape[1]/2)+(w/2)),int((shape[0]/2)+(h/2))))
            p4=((int((shape[1]-w)/2),int((shape[0]/2)+(h/2))))
            points=[p1,p2,p3,p4]
            kernel_o = np.ones((1, 1), np.uint8)
            #kernel_c = np.ones((2, 2), np.uint8)
            #print(points)
            
            img_mask=cv2.fillPoly(img_mask,[np.array(points)],[255,255,255])
            img_mask=img_mask.astype(np.uint8)
            ret,img_mask=cv2.threshold(img_mask,35,255,cv2.THRESH_BINARY)
            img_mask = cv2.morphologyEx(img_mask, cv2.MORPH_OPEN, kernel_o)
            mask=cv2.bitwise_not(img_mask)
            #mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel_c)
            #cv2.imwrite(apath+"_mask.jpg",mask)

            dst=cv2.bitwise_or(img,bg,mask=mask)
            ret,dst=cv2.threshold(dst,40,255,cv2.THRESH_BINARY)
            #cv2.imwrite(apath+"_dst.jpg",dst)
            dst=cv2.add(img,dst)

            
            b, g, r = cv2.split(dst)
            r[r > 220] = 255
            b[b > 220] = 255
            g[g > 220] = 255
            b = cv2.equalizeHist(b)
            g = cv2.equalizeHist(g)
            r = cv2.equalizeHist(r)
            O = cv2.merge([b,g,r])
            
            cv2.imwrite(apath+"_.jpg",O)
            #cv2.imwrite(apath,dst)
            #cv2.imwrite(apath.split('\\')[-1].split('.')[0]+'_.jpg',dst)
        else:
            pass