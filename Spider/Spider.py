# -*- coding: UTF-8 -*-
import sys
import os
import Sp_parser,Sp_outputer,Sp_urlManager,cd_conn
import time
from multiprocessing import Process
################################
class Spider(object):
  def __init__(self):
    self.conn = cd_conn.CD_Conn()
    #self.conn = Sp_conn.Sp_conn()
    self.parser = Sp_parser.Sp_parser()
    self.outputer = Sp_outputer.Sp_outputer()
    self._root = ''
    self._url = ''
    self._num = 0
    self._title = ''
    
  def download(self,root,url,num,title):
    self._root = root
    self._url = url
    self._num = num
    self._title = title
    if self.isDown():
      print str(self._num)+" done"
      return
    if self.conn.visit(self._root+self._url) == 200:
      whole_page=self.conn.getpage()
      data=self.parser.parse(whole_page)
      if self.outputer.check(data):
        #self.outputer.echo()
        self.outputer.record(self._num,self._title)

  def isDown(self):
    dir = "downloads/"
    filename = str(self._num)+"_"+self._title+".txt"
    #print filename
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
  root_url = "http://www.23us.cc/html/123/123638/"
  #m_url = "http://m.quledu.com/"
  man = Sp_urlManager.urlsManager(root_url)
  #############
  if man.start():
    print "Init Sucessfully..."
  else:
    print "Failed, try again!"
    exit()
  print "total : %d"%man.num
  ##############
  spider = Spider()
  for url in man.pool:
    #print "######################"
    print "Starting: "+str(man.nums[url])+" / "+str(man.num)
    pro = Process(target=spider.download,args=(root_url,url,man.nums[url],man.dict[url],))
    pro.start()
    pro.join(3)
    #sp.download(root_url,url,man.nums[url],man.dict[url])