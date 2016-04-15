#coding=utf-8
import cv2
import csv
import numpy as np
from pandas.io.parsers import read_csv
from matplotlib import pyplot as plt
import os


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

filesplit=readdata('photo.txt')
for s in filesplit:
    if len(s)!=5:
        continue
    img = cv2.imread(s[0])
    height, weight =np.shape(img)[:2]
    x1, x2, y1, y2 =[int(x) for x in s[1:]]
    x=int(x1)
    y=int(y1)
    w=int(x2-x1)
    h=int(y2-y1)
    scale=0.4
    miny=max(0,y-scale*h)
    minx=max(0,x-scale*w)
    maxy=min(height,y+(1+scale)*h)
    maxx=min(weight,x+(1+scale)*w)
    roi=img[miny:maxy,minx:maxx]
    rectshape=roi.shape
    maxlenght=max(rectshape[0],rectshape[1])
    img0=np.zeros((maxlenght,maxlenght,3))
    img0[(maxlenght*.5-rectshape[0]*.5):(maxlenght*.5+rectshape[0]*.5),(maxlenght*.5-rectshape[1]*.5):(maxlenght*.5+rectshape[1]*.5)]=roi
    cv2.imwrite('crop'+s[0],img0)




#生成目录
'''fr=open('imagelist.txt','w')
FileList=GetFileList('photo')
fr.writelines(str(len(FileList))+'\n')
for i,oldname in enumerate(FileList):
    newname='photo\\photo'+str(i)+oldname[-4:]+'\n'
    fr.writelines(newname)
    #os.rename(oldname,newname)
fr.close()'''
