import os
import shutil

rootdir = ".\\"
for parent,dirnames,filenames in os.walk(rootdir):
    for dirname in dirnames:
        thedir = parent+'\\'+dirname
        print(thedir)
        try:
            shutil.move(thedir+thedir+'\\1\\1.pdf',thedir)
            shutil.move(thedir+thedir+'\\2\\2.pdf',thedir)
            shutil.move(thedir+thedir+'\\3\\3.pdf',thedir)
            shutil.move(thedir+thedir+'\\4\\4.pdf',thedir)
            shutil.move(thedir+thedir+'\\5\\5.pdf',thedir)
            shutil.move(thedir+thedir+'\\6\\6.pdf',thedir)
        except:
            pass
        try:
            shutil.move(thedir+'\\1\\1.pdf',thedir)
            shutil.move(thedir+'\\2\\2.pdf',thedir)
            shutil.move(thedir+'\\3\\3.pdf',thedir)
            shutil.move(thedir+'\\4\\4.pdf',thedir)
            shutil.move(thedir+'\\5\\5.pdf',thedir)
            shutil.move(thedir+'\\6\\6.pdf',thedir)
        except:
            pass