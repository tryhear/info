import os
import shutil
import traceback

count=0
dirs=os.listdir()
for dir in dirs:
    path=os.path.join(os.getcwd(),dir)
    #print(path)
    if not os.path.isfile(path):
        try:
            #os.remove(path)
            os.system("del %s\\*.* /q" % path)
            #print(path)
            if os.path.isdir(os.path.join(path, dir,dir)):
                pass
            else:
                print(path)
                count+=1
            #os.system("cd %s\\%s\\%s" %(dir,dir,dir))
        except:
            traceback.print_exc()
    else:
        pass
print(count)