# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import time
import os

while True:
    os.system('cls')
    print('\n正在抓取近期档案相关采购项目：\n')
    for c in range(99,0,-1):
        html=requests.get('http://www.sczfcg.com/CmsNewsController.do?method=recommendBulletinList&rp=25&page=%s&moreType=provincebuyBulletinMore&channelCode=shiji_cggg'%c,headers={'User-Agent':'Baiduspider'})
        soup=BeautifulSoup(html.text,'lxml')
        title=soup.select('.colsList a[target]')
        dt=soup.select('.colsList span')
        
        k=1
        for i in title:
            test=i.get_text()
            if '德阳'  in test:
                if '档案' in test:
                    k+=1
                    print('\n'+str(test),end=',')
                    try:
                        dt1=dt[k].get_text()
                        print(dt1)
                        print('')
                    except:
                        pass
                elif '数字化' in test:
                    k+=1
                    print('\n'+str(test),end=',')
                    try:
                        dt1=dt[k].get_text()
                        print(dt1)
                        print('')
                    except:
                        pass
                k+=1
                # print(test,end=',')
                try:
                    dt1=dt[k].get_text()
                    # print(dt1)
                except:
                    pass
                
            elif '档案数字化' in test:
                k+=1
                print(test,end=',')
                try:
                    dt1=dt[k].get_text()
                    print(dt1)
                    print('')
                except:
                    pass
            else:
                k+=1
        
    time.sleep(60000)
    
