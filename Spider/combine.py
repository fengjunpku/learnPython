# -*- coding: UTF-8 -*-
import os,sys
def scan(dir):
  order = 700001
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

def combine(dir,name):
  file=open(str(name)+".txt","w")
  count = 0
  filenames = []
  for parent,dirnames,files in os.walk(dir):
    filenames=files
  for filename in filenames:
    count+=1
    print "reading %s"%filename
    readfile=open(dir+"/"+filename,"r")
    file.write(readfile.read())
    readfile.close()
  file.close()

def clean(dir):
  for file in os.listdir(dir):
    target = os.path.join(dir,file)
    os.remove(target)

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
  elif cmdNum == 2 and sys.argv[1] == "c":
    clean(dirname)
