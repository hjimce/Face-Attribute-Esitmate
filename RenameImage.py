#coding=utf-8
#生成目录
import  os
from  Base import  GetFileList
fname='photo_01'
FileList=GetFileList(fname)
for i,oldname in enumerate(FileList):
    newname=fname+'\\'+fname+str(i)+oldname[-4:]
    os.rename(oldname,newname)
