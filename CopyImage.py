#coding=utf-8
#拷贝文件到另外一个文件
import  shutil
import os
'''dirimg=['black','brown','white','yellow']
for s in dirimg:
    print s
    path='pick\\'+s
    dl=os.listdir(path)

    for img in dl:
        newpath='photo_4pick\\'+s+'\\'+img
        oldpath='photo_4\\'+img
        shutil.copy(oldpath,newpath)'''
dl=os.listdir('ori')
for img in dl:
        newpath='all\\'+img
        oldpath='photo_05\\'+img
        shutil.copy(oldpath,newpath)