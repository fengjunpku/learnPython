# -*- coding: UTF-8 -*-
import sys
import os
import Sp_conn,Sp_parser,Sp_outputer,Sp_urlManager,cd_conn
import time
import threading
################################
class Spider(threading.Thread):
  def __init__(self,root,url,num,title):
    threading.Thread.__init__(self)
    self.conn = cd_conn.CD_Conn()
    #self.conn = Sp_conn.Sp_conn()
    self.parser = Sp_parser.Sp_parser()
    self.outputer = Sp_outputer.Sp_outputer()
    self._root = root
    self._url = url
    self._num = num
    self._title = title
    

  def download(self):
    if self.isDown():
      print str(self._num)+" done"
      return
    if self.conn.visit(self._root+self._url) == 200:
      whole_page=self.conn.getpage()
      data=self.parser.parse(whole_page)
      if self.outputer.check(data):
        #self.outputer.echo()
        self.outputer.record(self._num,self._title)

  def run(self):
    self.download()

  def isDown(self):
    dir = "downloads/"
    filename = str(self._num)+"_"+self._title+".txt"
    return os.path.isfile(dir+filename)
  
  def next_url(self):
    return self.outputer._data['next']

if __name__ == "__main__":
  def handler(signum, frame):
    raise AssertionError
  # Set coding
  reload(sys)
  sys.setdefaultencoding('utf-8')
  ###########
  root_url = "http://www.23wx.com/html/56/56569/"
  man = Sp_urlManager.urlsManager(root_url)
  #############
  if man.start():
    print "Init Sucessfully..."
  else:
    print "Failed, try again!"
    exit()
  print "total : %d"%man.num
  ##############
  for url in man.pool:
    #print "######################"
    print "Starting: "+str(man.nums[url])+" / "+str(man.num)
    tsp = Spider(root_url,url,man.nums[url],man.dict[url])
    tsp.start()
    tsp.join(3)
    #sp.download(root_url,url,man.nums[url],man.dict[url])

    
    
    