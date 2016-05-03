#coding=utf-8
import  cv2
from  Base import  readdata
import numpy as np
#根据人脸框bbox，从一张完整图片裁剪出人脸
filesplit=readdata('bbox.txt')
for s in filesplit:
    print s
    if len(s)!=5 and len(s)!=9:
        continue
    s=s[:5]
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