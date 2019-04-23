#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# driver_path = 'F:\ProgramApp\chromedriver\chromedriver.exe'
#
# driver = webdriver.Chrome(executable_path=driver_path)
#
# driver.get('https://www.baidu.com/')

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver_path = 'F:\ProgramApp\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path)

# # 隐式页面等待
# driver.implicitly_wait(10)
#
# driver.get('https://www.douban.com/')
#
# print(driver.page_source)