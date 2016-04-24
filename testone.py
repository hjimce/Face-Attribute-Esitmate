#coding=utf-8
import os
import numpy as np
from matplotlib import pyplot as plt
import cv2
import shutil
import time
import random
plt.ion()
plt.show()
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
def readdata(filepath):
    fr=open(filepath,'r')
    filesplit=[]
    for line in fr.readlines():
        s=line.split()
        filesplit.append(s);
    fr.close()
    return filesplit


caffe_root = '/home/hjimce/tools/caffe/'
import sys
sys.path.insert(0, caffe_root + 'python')
import caffe



mean_filename='./imagenet_mean.binaryproto'
proto_data = open(mean_filename, "rb").read()
a = caffe.io.caffe_pb2.BlobProto.FromString(proto_data)
mean  = caffe.io.blobproto_to_array(a)[0]



gender_net_pretrained='./caffenet_train_iter_1000.caffemodel'

gender_net_model_file='./deploy_gender.prototxt'
gender_net = caffe.Classifier(gender_net_model_file, gender_net_pretrained,mean=mean,
					   channel_swap=(2,1,0),
					   raw_scale=255,
					   image_dims=(256, 256))

gender_list=['black','brown','white','yellow']
gender_listc=['黑种人','棕种人','白种人','黄种人']




'''acu=0.
all=0.
for r in gender_list:
	dir='batch2/'+r
	fs=os.listdir(dir)
	for f in fs:
		imgp=dir+'//'+f
		input_image=caffe.io.load_image(imgp)
		prediction_gender=gender_net.predict([input_image])[0].argmax()
		str_gender=gender_list[prediction_gender]
		print r,str_gender
		if str_gender==r:
			acu+=1
		else:
			plt.imsave(r+'/'+f,input_image)
		all+=1

print 'acu:',acu/all'''
fileimg_m=GetFileList('cropphoto_4')
random.shuffle(fileimg_m)
for img in fileimg_m:
	input_image = caffe.io.load_image(img)
	prediction_gender=gender_net.predict([input_image])
	propra={}
	for i in range(len(gender_list)):
		propra[gender_listc[i]]=int(prediction_gender[0][i]*100)
	propra= sorted(propra.iteritems(), key=lambda d:d[1],reverse=True)#字典根据值排序
	prostr=''
	for key in propra:
		prostr=prostr+'\t'+key[0]+':'+str(key[1])+'%'+'\t'
	print prostr
	str_gender=gender_listc[prediction_gender[0].argmax()]
	resized_image = cv2.resize(cv2.imread(img), (500, 500))
	cv2.imshow(str_gender,resized_image)
	cv2.moveWindow(str_gender, 100, 100);
	cv2.waitKey(0)







