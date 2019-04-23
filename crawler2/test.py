#!/usr/bin/env python
#coding:utf-8

# import requests,os,re
# import pandas as pd
#
# url_one = 'https://cs.lianjia.com/xiaoqu/pg15cro21/'
#
# url_two = 'https://cs.lianjia.com/xiaoqu/3520035651265161/'
#
# html = requests.get(url_two).text
#
# html_one = requests.get(url_one).text
#
# list = []
# # 小区名称
# name = re.findall(r'<h1 class="detailTitle">(.*?)</h1>', html, re.S)
# list.append(name[0])
#
# # 所在区域
# """
# 长沙小区</a><span class="stp">&nbsp;&gt;&nbsp;</span><a href="https://cs.lianjia.com/xiaoqu/.*?/">(.*?)小区</a>
# """
# area = re.findall(
#     r'长沙小区</a><span class="stp">&nbsp;&gt;&nbsp;</span><a href="https://cs.lianjia.com/xiaoqu/.*?/">(.*?)小区</a>', html,
#     re.S)
# area_end = area[0] + '区'
# list.append(area_end)
# # 详细地址
# """
# <div class="detailDesc">(天心暮云)中意二路758号</div>
# """
# address = re.findall(r'<div class="detailDesc">(.*?)</div>', html, re.S)
# list.append(address[0])
# # 建成年代
# year = re.findall(r'<span class="xiaoquInfoContent">(.*?) </span>', html, re.S)
# list.append(year[0])
# # 均价
# """
# <span class="xiaoquUnitPrice">\d+?</span>
# """
# money = re.findall(r'<span class="xiaoquUnitPrice">(\d+?)</span>', html, re.S)
# list.append(money[0] + '元/m2')
# # 在售套数
# num = re.findall(r'class="totalSellCount"><span>(\d+?)</span>套</a>',html_one,re.S)
# num_end = str(num) + "套"
# list.append(num_end)
#
# print(list)

url_str = 'http://www.budejie.com/text/3'
print(url_str.split('/')[-1])