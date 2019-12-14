import os
import shutil
import traceback

count=0
dirs=os.listdir()
for dir in dirs:
    path=os.path.join(os.getcwd(),dir)
    path1=os.path.join(os.getcwd(),dir,dir,dir)

    if not os.path.isfile(path):
        try:
            if os.path.isdir(os.path.join(path, dir,dir)):
                pass
            else:
                print(path)
                count+=1
                print(path+"error!!!")
                #input()
            #os.system("cd %s\\%s\\%s" %(dir,dir,dir))

            #os.system("del %s\\*.* /q" % path)
            os.system("move /Y %s\\*.* %s" %(path1,path))
            shutil.rmtree(os.path.join(os.getcwd(),dir,dir))

        except:
            traceback.print_exc()
    else:
        pass
print(count)
input()