from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600))
display.start()

username = "******"
password = "******"
title = "test haha"
content = "xx"

#driver = webdriver.PhantomJS()
driver = webdriver.Firefox()
driver.implicitly_wait(60)
driver.set_page_load_timeout(60)

try:
  driver.get("https://bbs.pku.edu.cn/v2/thread.php?bid=7")
  driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
  print " Title : "+driver.title
  #print driver.page_source

  #inputElement = driver.find_element_by_name("username")
  #inputElement.send_keys(username)
  #time.sleep(1.003)
  #inputElement = driver.find_element_by_name("password")
  #inputElement.send_keys(password)
  #time.sleep(0.584)
  #inputElement.send_keys(Keys.RETURN)

  #print " Login as : "+driver.find_element_by_css_selector("p.username.small").text

  #time.sleep(3.616)
  #title_input = driver.find_element_by_css_selector("div.input-wrapper.title-input input")
  #title_input.send_keys(title)
  #time.sleep(2.18)
  #content_input = driver.find_element_by_css_selector("div.input-wrapper.content-input textarea")
  #content_input.send_keys(content)
  #time.sleep(0.312)
  #content_input.send_keys(Keys.CONTROL,Keys.RETURN)

  #ptitle = driver.find_element_by_css_selector("header h3")
  #print " Post title : "+title


except Exception as e:
  print e
  
finally:
  driver.close()
  display.stop()
  os.system("pkill geckodriver")
