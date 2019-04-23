#!/usr/bin/env python
#coding:utf-8
import requests
from urllib import request
from urllib import parse

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Referer':'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput='
}

data = {
    'first':'true',
    'pn':1,
    'kd':'Hadoop'
}

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

res = request.Request(url=url,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST')
text = request.urlopen(res)


print(text.read().decode('utf-8'))
# with open('test.log','w') as f:
#     for i in text.read()
#     f.write()