#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'

from selenium import webdriver

driver_path = r'F:\ProgramApp\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com/")

# 直接访问
# driver.get("https://www.douban.com/")
# js访问
driver.execute_script('window.open("https://www.douban.com/")')
print(driver.window_handles)
driver.switch_to_window(driver.window_handles[1])

print(driver.current_url)

# switch_to_window 切换到指定窗口
# window_handles 窗口集合，是一个列表，里面装的是窗口句柄 ，从0开始