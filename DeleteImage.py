#coding=utf-8
#拷贝文件到另外一个文件
import  os
from  Base import  GetFileList
de=os.listdir('p1')
for img in de:
    path='photo_01\\'+img
    print path
    if os.path.exists(path):
        os.remove(path)