import zipfile
from unrar import rarfile
import os
def decompress(file_name):
    if(file_name.find(".zip"))> -1:
        try:
            myzip=zipfile.ZipFile(file_name)
            mystr=myzip.filename.split(".")
            myzip.extractall(mystr[0])
            myzip.close()
            os.remove(file_name)
            print(file_name+"解压成功")
        except:
            print(flie_name+"解压失败")
            pass

    else:
        try:
            myrar=rarfile.RarFile(file_name)
            mystr=file_name.split(".")
            myrar.extractall(mystr[0])
            os.remove(file_name)
            print(file_name+"解压成功")
        except:
            print(file_name+"解压失败")
            pass

def file_name(list_name,path):
    for file in os.listdir(path):
        file_path=os.path.join(path,file)
        if os.path.isdir(file_path):
            listdir(file_path,list_name)
        else:
            list_name.append(file_path)

list_name=[]
path="C:\\Users\\lenovo\\Desktop\\第二次"
file_name(list_name,path)
for i in list_name:
    decompress(i)

