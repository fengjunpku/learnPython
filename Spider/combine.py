# -*- coding: UTF-8 -*-
import os,sys
def scan(dir):
  order = 900001
  unorders = []
  has = 0
  miss = 0
  total = 0
  for parent,dirnames,filenames in os.walk(dir):
    for filename in filenames:
      has = len(filenames)
      this = int(filename.split("_")[0])
      if this != order:
        print order
        unorders.append(order)
        order=this+1
      else:
        order+=1
  miss = len(unorders)
  total = has + miss
  print "total : %d, miss : %d"%(total,miss)

def combine(dir,num):
  file=open("900000_sum.txt","w")
  count = 0
  filenames = []
  for parent,dirnames,files in os.walk(dir):
    filenames=files
  for filename in filenames:
    count+=1
    print "reading %s"%filename
    #if count>num:
      #return
    readfile=open(dir+"/"+filename,"r")
    file.write(readfile.read())
    readfile.close()
  file.close()

if __name__ == "__main__":
  # Set coding
  reload(sys)
  sys.setdefaultencoding('utf-8')
  #scan("downloads")
  combine("downloads",3)