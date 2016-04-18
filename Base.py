#coding=utf-8
def writedata(listdata,filepath="newlabel.txt"):
    fr=open(filepath,'w')
    fr.writelines(listdata)
    fr.close()
def readdata(filepath):
    fr=open(filepath,'r')
    filesplit=[]
    for line in fr.readlines():
        s=line.split()
        filesplit.append(s);
    fr.close()
    return filesplit

def IsSubString(SubStrList,Str):
    flag=True
    for substr in SubStrList:
        if not(substr in Str):
            flag=False

    return flag

def GetFileList(FindPath,FlagStr=[]):
    import os
    FileList=[]
    FileNames=os.listdir(FindPath)
    if (len(FileNames)>0):
       for fn in FileNames:
           if (len(FlagStr)>0):
               #返回指定类型的文件名
               if (IsSubString(FlagStr,fn)):
                   fullfilename=os.path.join(FindPath,fn)
                   FileList.append(fullfilename)
           else:
               #默认直接返回所有文件名
               fullfilename=os.path.join(FindPath,fn)
               FileList.append(fullfilename)

    #对文件名排序
    if (len(FileList)>0):
        FileList.sort()

    return FileList