import os
import numpy as np
from matplotlib import pyplot as plt
import cv2
import shutil



def GetFileList(FindPath,FlagStr=[]):      
	import os
	FileList=[]
	FileNames=os.listdir(FindPath)
	if len(FileNames)>0:
		for fn in FileNames:
			if len(FlagStr)>0:
				if IsSubString(FlagStr,fn):
					fullfilename=os.path.join(FindPath,fn)
					FileList.append(fullfilename)
			else:
				fullfilename=os.path.join(FindPath,fn)
				FileList.append(fullfilename)

   
	if len(FileList)>0:
		FileList.sort()

	return FileList
def IsSubString(SubStrList,Str):      
	flag=True
	for substr in SubStrList:
		if not(substr in Str):
			flag=False

	return flag

txt=open('train.txt','w')
filename=['cropblack','cropbrown','cropwhite','cropyellow']
#filename=['batch1//black','batch1//brown','batch1//white','batch1//yellow']
#filename=['batch2//black','batch2//brown','batch2//white','batch2//yellow']
for i,f in enumerate(filename):
	imgfile=GetFileList(f)
	for img in imgfile:
		str0=img+'\t'+str(i)+'\n'
		txt.writelines(str0)

txt.close()


'''txt=open('test.txt','w')
filename=['cropblack','cropbrown','cropwhite','cropyellow']
for i,f in enumerate(filename):
	imgfile=GetFileList(f)[-100::-50]
	for img in imgfile:
		str0=img+'\t'+str(i)+'\n'
		txt.writelines(str0)

txt.close()

txt=open('val.txt','w')
filename=['cropblack','cropbrown','cropwhite','cropyellow']
for i,f in enumerate(filename):
	imgfile=GetFileList(f)[-50::]
	for img in imgfile:
		str0=img+'\t'+str(i)+'\n'
		txt.writelines(str0)

txt.close()'''


