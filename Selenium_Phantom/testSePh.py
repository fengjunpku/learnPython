#-*- coding: utf-8 -*-
from selenium import webdriver
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
 
driver = webdriver.PhantomJS(executable_path=r"D:\Programs\phantomjs-2.1.1-windows\bin\phantomjs.exe")  #这要可能需要制定phatomjs可执行文件的位置
driver.get("http://miaomiaoxiong.net/md/#OpenMP_note")
time.sleep(0.5)
#print driver.current_url
print driver.page_source
driver.quit()