#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'

import requests,re,time

url = 'https://v1.hitokoto.cn/?encode=text&charset=utf-8'

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'cookie':'_ga=GA1.2.876737642.1544707176; _gid=GA1.2.1101523237.1546952614',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    ':authority':'v1.hitokoto.cn',
    ':method':'GET',
    ':path':'/?encode=text&charset=utf-8',
    'upgrade-insecure-requests':'1'
}
with open("test.txt", 'a',encoding='utf-8',newline='') as fp:
    for i in range(2000):
        response = requests.get(url,headers)
        text = response.text
        print(text)
        fp.writelines(text+'\n')
fp.close()