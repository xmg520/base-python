#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'

import requests,re,os
import urllib.request

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

url = 'http://www.doutula.com/photo/list/?page=1'

html = requests.get(url,headers).text

"""
<img src="(.*?)" style=
data-original="(.*?)" alt=
"""
img_urls = re.findall(r'data-original="(.*?)" alt=',html)
names = re.findall(r'alt="(.*?)" class=',html)
j = 0
for i in img_urls:
    # os.path.splitext(i)【】 分离文件与扩展名  0、1
    suffix = os.path.splitext(i)[1]
    alt = names[j]
    j +=1
    name = alt+suffix
    print(suffix)
    # urllib.request.urlretrieve(i,'image/'+name)
