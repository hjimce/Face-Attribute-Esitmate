#coding=utf-8
import  cv2
import  os
import random
import  numpy as np
#随机旋转，img为旋转图片，landmark为人脸特征点，alpha旋转角度0~360，bbox人脸框
class BBox(object):
    """
        Bounding Box of face

    """
    def __init__(self, bbox):
        self.left = bbox[0]
        self.right = bbox[1]
        self.top = bbox[2]
        self.bottom = bbox[3]
        self.x = bbox[0]
        self.y = bbox[2]
        self.w = bbox[1] - bbox[0]
        self.h = bbox[3] - bbox[2]

    def expand(self, scale=0.05):
        bbox = [self.left, self.right, self.top, self.bottom]
        bbox[0] -= int(self.w * scale)
        bbox[1] += int(self.w * scale)
        bbox[2] -= int(self.h * scale)
        bbox[3] += int(self.h * scale)
        return BBox(bbox)

    def project(self, point):
        x = (point[0]-self.x) / self.w
        y = (point[1]-self.y) / self.h
        return np.asarray([x, y])

    def reproject(self, point):
        x = self.x + self.w*point[0]
        y = self.y + self.h*point[1]
        return np.asarray([x, y])

    def reprojectLandmark(self, landmark):
        p = np.zeros((len(landmark), 2))
        for i in range(len(landmark)):
            p[i] = self.reproject(landmark[i])
        return p

    def projectLandmark(self, landmark):
        p = np.zeros((len(landmark), 2))
        for i in range(len(landmark)):
            p[i] = self.project(landmark[i])
        return p

    def subBBox(self, leftR, rightR, topR, bottomR):
        leftDelta = self.w * leftR
        rightDelta = self.w * rightR
        topDelta = self.h * topR
        bottomDelta = self.h * bottomR
        left = self.left + leftDelta
        right = self.left + rightDelta
        top = self.top + topDelta
        bottom = self.top + bottomDelta
        return BBox([left, right, top, bottom])
def rotate(img,alpha,bbox=None):
	if bbox is None:
		bbox_temp=BBox((0,img.shape[1],0,img.shape[0]))
	else:
		bbox_temp=bbox


	center = ((bbox_temp.left+bbox_temp.right)/2., (bbox_temp.top+bbox_temp.bottom)/2.)

	rot_mat = cv2.getRotationMatrix2D(center, alpha, 1)
	img_rotated_by_alpha = cv2.warpAffine(src=img,M=rot_mat,dsize=(img.shape[1],img.shape[0]))

	face = img_rotated_by_alpha
	return face
def addnoise(img,mu=0,sigma=10):
    noise=np.random.normal(mu, sigma, size=img.shape)
    return  img+noise
fp='cropblack'
ls=os.listdir(fp)
for l in ls:
    imgpath=fp+'//'+l
    img = cv2.imread(imgpath)
    rimg=rotate(img,random.randint(0,360))#旋转扩充
    #rimg=addnoise(img,mu=0,sigma=30)
    cv2.imwrite('rotate//rotate2'+l,rimg)
