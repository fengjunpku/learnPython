# -*- coding: UTF-8 -*-
import sys

import sys  
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *  
  
class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit()  

reload(sys)
sys.setdefaultencoding('utf-8')
url = 'http://miaomiaoxiong.net/md/#OpenMP_note'  
r = Render(url)  
html = r.frame.toHtml() 
print html