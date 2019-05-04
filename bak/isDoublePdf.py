from pdfrw import PdfReader
import argparse
import os



def isDoublePdf(fn):
    x = PdfReader(fn)
    isdouble = False
    for i in range(len(x.pages)):
        if x.pages[i].Resources.Font:
            isdouble = True
            break
        else:
            isdouble = False
    return isdouble

def walkPath(path):
    flag = False
    for f in os.listdir(path):
        if f.endswith(".pdf"):
            fn = os.path.join(path, f)
            if not isDoublePdf(fn):
                if not flag:
                    flag = True
                    print("Below files is not double side pdf:")
                    print("="*30)
                print(f)
    return flag

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dir", required=False, help="path")
args = vars(ap.parse_args())
print("="*30)
flag = walkPath(args["dir"] or os.curdir)
if not flag:
    print("All files is double side")
print("="*30)

input()