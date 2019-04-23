#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'

url = 'https://fe-api.zhaopin.com/c/i/sou?start=900&pageSize=90&cityId=489&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&at=cb2ac160c91442b89145e063e115f8b3&rt=4a092b3339694f47a189f6a17bf03087&_v=0.77611190&userCode=1031018434&x-zp-page-request-id=1298bca417b64719b3f9981ab8208854-1554087485875-593851'

import requests
zhaopBse = requests.session()

headers = {
    'Accept':'application/json, text/plain, */*',
    'Referer':'https://sou.zhaopin.com/?p=11&jl=489&sf=0&st=0&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
responZhaop = zhaopBse.get(url=url,headers=headers)
print(responZhaop.text)