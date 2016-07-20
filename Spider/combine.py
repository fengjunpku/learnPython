# -*- coding: UTF-8 -*-
import os,sys
import chardet
def scan(dir):
  order = 700001
  unorders = []
  has = 0
  miss = 0
  total = 0
  for parent,dirnames,filenames in os.walk(dir):
    for filename in filenames:
      if filename==".DS_Store":
        continue
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

def combine(dir,name):
  file=open(str(name)+".txt","w")
  count = 0
  filenames = []
  for parent,dirnames,files in os.walk(dir):
    filenames=files
  num_files = len(filenames)
  for filename in filenames:
    count+=1
    print "reading %s"%filename
    readfile=open(dir+"/"+filename,"r")
    file.write(readfile.read())
    readfile.close()
  file.close()
  print "Sum %d files to %s.txt"%(num_files,name)

def clean(dir):
  for file in os.listdir(dir):
    target = os.path.join(dir,file)
    print "removing %s"%target
    os.remove(target)

def check(dir):
  count = 0
  for file in os.listdir(dir):
    checkfile = open(os.path.join(dir,file),"r")
    content = checkfile.read()
    print str(count)+' '+str(chardet.detect(content)['confidence'])+' '+str(chardet.detect(content)['encoding'])
    count+=1

if __name__ == "__main__":
  dirname = "downloads"
  cmdNum = len(sys.argv)
  # Set coding
  reload(sys)
  sys.setdefaultencoding('utf-8')
  if cmdNum == 1:
    scan(dirname)
  elif cmdNum == 3 and sys.argv[1] == "a":
    sumfile = sys.argv[2]
    combine(dirname,sumfile)
  elif cmdNum == 2 and sys.argv[1] == "clean":
    clean(dirname)
  elif cmdNum == 2 and sys.argv[1] == "s":
    check(dirname)