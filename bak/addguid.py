import uuid
import sys

def addguid(file):
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if 'Key=""' in line:
                line = line.replace('Key=""','Key="'+str(uuid.uuid4()).upper()+'"')
            file_data += line
    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)
    print ("done!")

if __name__ =='__main__':
    addguid(sys.argv[1])