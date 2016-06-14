#!/usr/bin/python
#coding:UTF-8
import os
#print oct(os.stat('Download').st_mode)[-3:]
#print os.path.isdir('Download')
#print os.path.isfile('Download')

root = "."
for parent,dirnames,filenames in os.walk("/home/fengjun/bin"):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
	#for dirname in  dirnames:                       #输出文件夹信息
		#print "parent is:" + parent
		#print  "dirname is:" + dirname
	for filename in filenames:                        #输出文件信息
		#print "parent is:" + parent
		print "filename is:" + filename
		#print "the full name of the file is:" + os.path.join(parent,filename) #输出文件路径信息
