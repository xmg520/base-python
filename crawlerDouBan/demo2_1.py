#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver_path = 'F:\ProgramApp\chromedriver\chromedriver.exe'
#
# driver = webdriver.Chrome(executable_path=driver_path)


# driver.implicitly_wait(10)
#
# driver.get('https://www.douban.com/')
#
# print(driver.page_source)


# 显示页面等待
driver_path = 'F:\ProgramApp\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.douban.com/")
try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'myDy'))
    )
finally:
    driver.quit()