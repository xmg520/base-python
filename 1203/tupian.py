#!/usr/bin/env python
#coding:utf-8

import requests,os

url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1543839116181&di=9faa48e6b3a321c03b97d98c26019ee5&imgtype=0&src=http%3A%2F%2Fimg2.3lian.com%2F2014%2Ff5%2F73%2Fd%2F70.jpg'

res = requests.get(url).content

w = open('test.jpg','wb')

for i in res:
    w.write(i.content)
w.close()