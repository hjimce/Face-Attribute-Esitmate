#coding=utf-8
#生成目录
from Base import  GetFileList
fr=open('down.txt','w')
FileList=GetFileList('new')
fr.writelines(str(len(FileList))+'\n')
for i,oldname in enumerate(FileList):
    newname=oldname+'\n'
    fr.writelines(newname)
fr.close()
