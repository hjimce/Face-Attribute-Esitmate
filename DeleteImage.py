#coding=utf-8
#拷贝文件到另外一个文件
'''import  os
from  Base import  GetFileList
race=['black','white','yellow','brown']
for r in race:
    de=os.listdir('error\\'+r)
    for img in de:
        path=r+'\\'+img
        if os.path.exists(path):
            os.remove(path)'''
#求取两个文件夹差异文件
import  os
from  Base import  GetFileList
de=os.listdir('delete\\'+'delete')
for img in de:
    path='delete\\'+'ori\\'+img
    if os.path.exists(path):
        os.remove(path)