# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class Sp_outputer(object):
  def __init__(self):
    self._data=None

  def check(self,data):
    if data is None:
        print ">>> null data"
        return False
    self._data=data
    return True
  
  def echo(self):
    #print len(self._data)
    #print "##############"
    print "Downloading <<"+self._data['title']+">>.."
    #print "##############\n"
    #print self._data['url']
    #print "##############"
    #print len(self._data['content'])
    #for pragraph in self._data['content']:
      #print pragraph+'\n'
    #print self._data['next']
  
  def record(self,num,title):
    dir = "downloads/"
    filename = str(num)+"_"+self._data['title']+".txt"
    file = open(dir+filename,"w")
    print "Writing to file: "+dir+filename
    file.write("########################################\n")
    file.write(self._data['title']+'\n')
    file.write("########################################\n\n")
    for pragraph in self._data['content']:
      file.write(pragraph+'\n\n')
    file.close()


