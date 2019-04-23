#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'


"""
https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%BB%8F%E5%85%B8&sort=rank&page_limit=240&page_start=0
"""

import requests,json,csv

url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%BB%8F%E5%85%B8&sort=rank&page_limit=240&page_start=0"

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',

}

title = "电影名,评分,链接"
movies = []

response = requests.get(url=url,headers=headers)

text = json.loads(response.text)
subject = text['subjects']

with open('电影.csv','w',encoding='utf-8',newline='') as fp:
    fp.writelines(title+'\n')
    for i in subject:
        fp.writelines(i["title"]+','+ i["rate"]+','+ i["url"]+'\n')
