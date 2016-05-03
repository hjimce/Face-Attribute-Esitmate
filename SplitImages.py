#coding=utf-8
#拷贝文件到另外一个文件
import  shutil
import os
import random
dirimg=['black','brown','white','yellow']
dirimgs=['cropblack','cropbrown','cropwhite','cropyellow']
for d,s in zip(dirimg,dirimgs):
    dl=os.listdir(s)
    random.shuffle(dl)
    for i,img in enumerate(dl):
        if i%2==0:
            newpath='batch1\\'+d+'\\'+img
        else:
            newpath='batch2\\'+d+'\\'+img
        oldpath=s+'\\'+img
        shutil.copy(oldpath,newpath)