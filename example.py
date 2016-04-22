import os
import numpy as np
from matplotlib import pyplot as plt
import cv2
import shutil
import time

#plt.ion()

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



gender_net_pretrained='./caffenet_train_iter_2500.caffemodel'

gender_net_model_file='./deploy_gender.prototxt'
gender_net = caffe.Classifier(gender_net_model_file, gender_net_pretrained,mean=mean,
					   channel_swap=(2,1,0),
					   raw_scale=255,
					   image_dims=(256, 256))

gender_list=['black','brown','white','yellow']



'''file='cropphoto_4'
fileimg_fe=GetFileList(file)
#fileimg_fe=readdata('test.txt')
#np.random.shuffle(fileimg_fe)
error=0.
input_images=[]
paths=[]
for i,img in enumerate(fileimg_fe):
	if i%32!=0:
		input_images.append(caffe.io.load_image(img))
		paths.append(img)
	else:
		if len(input_images)==0:
			continue
		print 'predict'
		prediction_genders=gender_net.predict(input_images)
		for img,path,pre in zip(input_images,paths,prediction_genders):
			print path,pre.argmax()
			str_gender=gender_list[pre.argmax()]
			filename='pick/'+str_gender+'/'+path[len(file):]
			plt.imsave(filename,img)
			#print filename
		input_images=[]
		paths=[]'''

acu=0.
all=0.
for r in gender_list:
	dir='batch1/'+r
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
			'''plt.imshow(input_image)
			plt.title(str_gender)
			plt.show()'''
		all+=1

print 'acu:',acu/all
'''fileimg_m=GetFileList('test_male')
for img in fileimg_m:
	input_image = caffe.io.load_image(img)
	prediction_gender=gender_net.predict([input_image])

	str_gender=gender_list[prediction_gender[0].argmax()]
	print str_gender
	if prediction_gender[0].argmax()==0:
		error+=1

		


print 'acu:',(error+2)/(len(fileimg_m)+len(fileimg_fe))'''






