




#生成目录
'''fr=open('imagelist.txt','w')
FileList=GetFileList('photo')
fr.writelines(str(len(FileList))+'\n')
for i,oldname in enumerate(FileList):
    newname='photo\\photo'+str(i)+oldname[-4:]+'\n'
    fr.writelines(newname)
    #os.rename(oldname,newname)
fr.close()'''
