#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'

# import requests
from selenium import webdriver
from lxml import etree
import json


driver_path = 'F:\ProgramApp\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://v1.hitokoto.cn/')

# print(type(driver.page_source))
html = etree.HTML(driver.page_source)
context = html.xpath("/html/body/pre/text()")
for i in context:
    json_str = json.loads(i)
    print(json_str['hitokoto'])

driver.quit()
