#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'

"""
1. 获取所有tr标签 
2. 获取第2个tr标签
3. 获取所有class等于even的tr标签
4. 获取所有a标签的href属性
5. 获取所有的职位信息(纯文本)
"""

from lxml import etree

# 目标网站
# 设置解析编码
parse = etree.HTMLParser(encoding='utf-8')
# 解析
html = etree.parse("tencent.html",parser=parse)
# html = etree.HTML(url)

# 打印网站代码
# print(etree.tostring(html,encoding='utf-8').decode('utf-8'))

# 获取所有tr标签
# trs = html.xpath("//tr")
# for i in trs:
#     print(etree.tostring(i,encoding='utf-8').decode('utf-8'))

# 获取第2个tr标签
# tr2 = html.xpath("//tr[2]")
# for i in tr2:
#     print(etree.tostring(i,encoding='utf-8').decode('utf-8'))

# 获取所有class等于even的tr标签
# trEven = html.xpath("//tr[@class='even']")
# for i in trEven:
#     print(etree.tostring(i,encoding='utf-8').decode('utf-8'))

# 获取所有a标签的href属性
# ahrefs = html.xpath("//a/@href")
# for i in ahrefs:
#     # a标签中的href属性可以直接打印出来
#     # print(etree.tostring(i,encoding='utf-8').decode('utf-8'))
#     print(i)

# 获取所有的职位信息(纯文本)
trs = html.xpath("//tr[position()>1]")
positions = []
i = 0

for tr in trs:
    ahref = tr.xpath(".//a/@href")[0]
    fullurl = "http://hr.tencent.com/" + ahref
    title = tr.xpath(".//td[1]//text()")
    category = tr.xpath(".//td[2]/text()")
    address = tr.xpath(".//td[4]/text()")
    publictime = tr.xpath(".//td[5]/text()")

    position = {
        '网址':fullurl,
        '标题': title,
        '类型': category,
        '地址': address,
        '时间': publictime
    }

    if i < 10:
        positions.append(position)
        i = i + 1

for i in positions:
    print(i)