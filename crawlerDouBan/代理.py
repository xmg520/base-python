#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'

from selenium import webdriver

driver_path = r'F:\ProgramApp\chromedriver\chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://119.57.108.89:53281")

driver = webdriver.Chrome(executable_path=driver_path,chrome_options=options)

driver.get("http://httpbin.org/ip")