# -*- coding: UTF-8 -*-
import sys
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *  
from PyQt4.QtNetwork import *
##########################################
class Sp_conn(object):
  def __init__(self):
    self._url=None
    self._response=None
    self.render = Render()
  
  def visit(self,url):
    if url is None:
      print "Please give a url!"
      return None
    self.render.request(url)
    self._response = self.render.status
    self._url = url
    return self._response
  
  def getpage(self):
    if self._url is None:
      print "Please call visit() first!"
      return None
    if self._response == 200:
      return self.render.frame.toHtml()
    else:
      print "connect failed"
      return self._response
###############################
class netManager(QNetworkAccessManager):
  def __init__(self):
    QNetworkAccessManager.__init__(self)
    self.finished.connect(self._finished)
    self.status = 0

  def _finished(self, reply):
    status = reply.attribute(0)#0 means QNetworkRequest::HttpStatusCodeAttribute
    self.status, ok = status.toInt()
#################################################
class Render(QWebPage):  
  def __init__(self):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)
    self.manager = netManager()
    self.setNetworkAccessManager(self.manager)
    self.loadFinished.connect(self._loadFinished)  

  def request(self, url):
    self.mainFrame().load(QUrl(url))
    self.app.exec_()
    self.status = self.manager.status

  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit()
#######################################################
if __name__ == "__main__":
  # Set coding
  reload(sys)
  sys.setdefaultencoding('utf-8')
  url = 'http://www.hbooker.com/chapter/book_chapter_detail/100257072'  
  ##
  conn = Sp_conn()
  conn.visit(url)
  conn.getPage()