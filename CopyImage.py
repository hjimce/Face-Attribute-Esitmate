#coding=utf-8
#拷贝文件到另外一个文件
import  shutil
import os
dirimg=['black','brown','white','yellow']
for s in dirimg:
    path='pickcut\\'+s
    dl=os.listdir(path)

    for img in dl:
        newpath='pick\\'+s+'\\'+img
        oldpath='photo_01\\'+img
        shutil.copy(oldpath,newpath)