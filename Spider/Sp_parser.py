# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import time


class Sp_parser(object):
  def __init__(self):
    self._soup=None
  
  #<title>傲世九重天-第一部 天外之楼 第四章 九劫剑的秘密-顶点小说</title>
  def _get_title(self):
    #return self._soup.title.get_text()
    _title = self._soup.find('h1').get_text()
    _title = _title.replace('?','？')
    _title = _title.replace(' ','_')
    _title = _title.replace('*','0')
    _title = _title.replace(' ','_')
    _title = _title.replace('<','《')
    _title = _title.replace('>','》')
    return _title
  
  #<dd id="contents">
  def _get_content(self):
    return self._soup.find('div',id="txt").get_text()
  #<dd id="footlink"><a href="16507280.html">上一页</a><a href="index.html">返回目录</a><a href="16507282.html">下一页</a></dd><dd id="tipsfoot"></dd>
  def _get_next(self):
    return self._soup.find('dd',id="footlink").find_all('a')[2].get('href')
  
  def parse(self,page):
    if page is None or str(page)=="":
      print ">>>>NULL page"
      return None
    self._soup = BeautifulSoup(page,'html.parser',from_encoding='utf-8')
    data={}
    #set tile
    data['title'] = self._get_title()
    #set content
    data['content'] = []
    pragraphs = self._get_content().split();
    for pragraph in pragraphs:
      data['content'].append(pragraph)
    #set next
      #data['next'] = self._get_next()
    ###################
    return data
      
  def get_links(self):
    if self._soup is None:
      print "Please call parse() first!"
      return None
    
    return None



