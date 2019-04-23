#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'
import requests,re
start_url = 'http://www.worlduc.com/SpaceShow/leaveword/List.aspx?uid=319173&Page=1'

parse_url = 'http://www.worlduc.com/SpaceShow/leaveword/List.aspx?uid=319173&Page={}'

Session = requests.session()

start_context = Session.get(start_url).text


def parse_page(url):
    page_context = Session.get(url=url).text
    names = re.findall('<span class="mt5"><a href=".+?" target="_blank">(.+?)</a>',page_context)
    # print(url)
    print(names)

# print(start_context)
end_url_num = re.findall('<a href=".+?Page=(\d)">末页',start_context)[0]
for i in range(int(end_url_num)+1):
    parse_url_end = parse_url.format(i)
    parse_page(parse_url_end)

