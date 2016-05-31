# -*- coding: UTF-8 -*-
import sys
import os
import Sp_conn,Sp_parser,Sp_outputer,Sp_urlManager,cd_conn
import time
import threading
################################
class Spider(object):
  def __init__(self):
    self.conn = cd_conn.CD_Conn()
    #self.conn = Sp_conn.Sp_conn()
    self.parser = Sp_parser.Sp_parser()
    self.outputer = Sp_outputer.Sp_outputer()

  def download(self,root,url,num,title):
    if self.isDown(num,title):
      #print "Has done"
      return
    if self.conn.visit(root+url) == 200:
      whole_page=self.conn.getpage()
      data=self.parser.parse(whole_page)
      self.outputer.check(data)
      #self.outputer.echo()
      self.outputer.record(num,title)
  
  def isDown(self,num,title):
    dir = "downloads/"
    filename = str(num)+"_"+title+".txt"
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
  root_url = "http://www.23wx.com/html/21/21741/"
  sp = Spider()
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
    #print "Starting: "+man.dict[url]
    thread = threading.Thread(target = sp.download, args = (root_url,url,man.nums[url],man.dict[url]))
    thread.start()
    thread.join(3)
    #sp.download(root_url,url,man.nums[url],man.dict[url])

    
    
    