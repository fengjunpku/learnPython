# -*- coding: UTF-8 -*-
import urllib2
import re
from bs4 import BeautifulSoup

class urlsManager(object):
  def __init__(self,root_url):
    self.root = root_url
    self.pool = []
    self.dict = {}
    self.nums = {}
    self.num = 0
  
  def start(self):
    request = urllib2.Request(self.root)
    request.add_header("user-agent", "Mozilla/5.0")
    response = urllib2.urlopen(request)
    if response.getcode() != 200:
      print "Connect failed"
      return False
    webcode = response.info().getparam('charset')
    page = response.read()
    #print page
    if webcode == "gb2312":
      page = page#.decode("gb2312").encode("utf-8")
    soup = BeautifulSoup(page,'html.parser',from_encoding='utf-8')
    pattern = re.compile(r'^\/\d+')
    #pattern = re.compile(r'/wcxs-\d+-\d+')
    #soup = soup.find_all('div',{'class','box'})[1]
    count = 300001
    for entry in soup.find('div',id='list').find_all('a'):
      url = entry.get('href')
      title = entry.get_text()
      title = title.replace('?','？')
      title = title.replace('：','_')
      title = title.replace(' ','_')
      title = title.replace('*','0')
      title = title.replace('<','《')
      title = title.replace('>','》')
      if url == None:
        continue
      match = pattern.match(url)
      if match:
        self.pool.append(url)
        self.dict[url] = title
        self.nums[url] = count
        print url+' : '+title
        count+=1
    self.num = len(self.pool)
    return True
  
def Num_Links(url):
  request = urllib2.Request(url)
  request.add_header("user-agent", "Mozilla/5.0")
  response = urllib2.urlopen(request)
  if response.getcode() != 200:
    print "Connect failed"
    return
  webcode = response.info().getparam('charset')
  page = response.read()
  if webcode == "gbk":
    page = page.decode("gbk").encode("utf-8")
  soup = BeautifulSoup(page,'html.parser',from_encoding='utf-8')
  pattern = re.compile(r'^\d+')
  url_pool=[]
  toc_dict={}
  for line in soup.find_all('a'):
    url = line.get('href')
    title = line.get_text()
    #print url.split(".")[0]
    match = pattern.match(url)
    
    if match:
      url_pool.append(url)
      toc_dict[url]=title
      print toc_dict[url]
  return len(url_pool)