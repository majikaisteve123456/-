**程序员是世界上最懒的动物**

~批改16级上机把我累得yo，还要review项目管理考试，fighting

1. 先把批量解压压缩包的脚本今天写了再说

   原始的version：

```
import zipfile
myzip=zipfile.ZipFile("C:\\Users\\lenovo\\Desktop\\1.zip")
print("文件名"+myzip.filename)
mystr=myzip.filename.split(".")#将压缩包名进行分隔
myzip.extractall(mystr[0])#解压
myzip.close()
os.remove("C:\\Users\\lenovo\\Desktop\\1.zip")
```

​     进化的version：

  只考虑两种压缩包的形式.rar 和.zip

rar格式文件解压需要注意的东西：

* 下unrar包
* 下unrar library即UnRAR.dll 
* 添加换将变量 ，将文件夹中的UnRAR.dll和UnRAR.lib用小写重命名改为unrar.lib和unrar.dll去掉64

```
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

```





2. 后面有时间，用selenium+junit 模拟浏览器操作下载学弟学妹的压缩包


3. 后面有时间用文本匹配检查学弟学妹写的程序的相似度
