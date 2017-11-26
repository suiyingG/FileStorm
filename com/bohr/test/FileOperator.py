import os
import os.path
import re
'''
用于删除复制的时候自动重命名的多余文件，删除前会把文件路径打印出来

'''
rootdir = "I:\BaiduNetdiskDownload\传智34期\\1、php核心编程、MySQL数据库"

files = os.listdir(rootdir)
#print(rootdir)
#print(files)
for filespath in files:
    #print(filespath)
    files1 = os.listdir(rootdir + "\\" + filespath)
    for x in files1:
        #print(x)
        x = rootdir + "\\" + x
    #print(files1)
    #print(files1)
    for filename in files1:
        print(filename)
        #str = re.match(".+?\(1\)\.[.]{3}$", filename)
        str = re.match(".+?\.[.]{3}$", filename)
        if str != None:
            print(str)
            pass
        else:
            #print(filename)
            pass
        '''if str !=  None:
            #print(str)
            print(rootdir + "\\" + filespath + "\\" + filename)
            os.remove(rootdir + "\\" + filespath + "\\" +filename)
       '''
