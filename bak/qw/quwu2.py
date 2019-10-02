    
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
                w=int(shape[1]*0)
                h=int(shape[0]*0)
            else:
                w=int(shape[1]*0.6)
                h=int(shape[0]*0.6)
            #print("h: ",shape[0],"w: ",shape[1])
            
            p1=((int((shape[1]-w)/2)),int((shape[0]-h)/2))
            p2=((int((shape[1]/2)+(w/2)),int((shape[0]-h)/2)))
            p3=((int((shape[1]/2)+(w/2)),int((shape[0]/2)+(h/2))))
            p4=((int((shape[1]-w)/2),int((shape[0]/2)+(h/2))))
            points=[p1,p2,p3,p4]
            
            p1_top=(0,0)
            p2_top=(int(shape[1]),0)
            p3_top=(int(shape[1]),int(shape[0]*0.04))
            p4_top=(0,int(shape[0]*0.04))
            points_top=[p1_top,p2_top,p3_top,p4_top]
            #print(points_top)
            
            p1_left=(0,0)
            p2_left=(int(shape[1]*0.03),0)
            p3_left=(int(shape[1]*0.03),int(shape[0]))
            p4_left=(0,int(shape[0]))
            points_left=[p1_left,p2_left,p3_left,p4_left]
            #print(points_left)
            
            p1_right=(int(shape[1]*0.97),0)
            p2_right=(int(shape[1]),0)
            p3_right=(int(shape[1]),int(shape[0]))
            p4_right=(int(shape[1]*0.97),int(shape[0]))
            points_right=[p1_right,p2_right,p3_right,p4_right]
            #print(points_right)
            
            p1_button=(0,int(shape[0]*0.97))
            p2_button=(int(shape[1]),int(shape[0]*0.97))
            p3_button=(int(shape[1]),int(shape[0]))
            p4_button=(0,int(shape[0]))
            points_button=[p1_button,p2_button,p3_button,p4_button]
            #print(points_button)
            
            img_mask=cv2.fillPoly(img_mask,[np.array(points)],[255,255,255])
            img_mask=img_mask.astype(np.uint8)
            ret,img_mask=cv2.threshold(img_mask,35,255,cv2.THRESH_BINARY)
            kernel_o = np.ones((1, 1), np.uint8)
            img_mask = cv2.morphologyEx(img_mask, cv2.MORPH_OPEN, kernel_o)
            mask=cv2.bitwise_not(img_mask)
            
            #cv2.imwrite(apath+"_mask.jpg",mask)

            dst=cv2.bitwise_or(img,bg,mask=mask)
            ret,dst=cv2.threshold(dst,40,255,cv2.THRESH_BINARY)
            #cv2.imwrite(apath+"_dst.jpg",dst)
            dst=cv2.add(img,dst)
            

            if shape[0]>3690 or shape[1]>3690:
                pass
            else:
                dst=cv2.fillPoly(dst,[np.array(points_top)],[255,255,255])
                dst=cv2.fillPoly(dst,[np.array(points_left)],[255,255,255])
                dst=cv2.fillPoly(dst,[np.array(points_right)],[255,255,255])
                dst=cv2.fillPoly(dst,[np.array(points_button)],[255,255,255])
                '''
                b, g, r = cv2.split(dst)
                r[r > 200] = 255
                b[b > 200] = 255
                g[g > 200] = 255
                b = cv2.equalizeHist(b)
                g = cv2.equalizeHist(g)
                r = cv2.equalizeHist(r)
                dst = cv2.merge([b,g,r])
                '''
            cv2.imwrite(apath+"_.jpg",dst)
            #cv2.imwrite(apath,dst)
            #cv2.imwrite(apath.split('\\')[-1].split('.')[0]+'_.jpg',dst)
        else:
            pass