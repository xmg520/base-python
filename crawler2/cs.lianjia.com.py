#!/usr/bin/env python
#coding:utf-8

"""

https://cs.lianjia.com/xiaoqu/cro21/
戴晓：爬取
长沙小区的所在区域，小区名称，详细地址，建成年代，均价，在售套数，
利用numpy和pandas处理不规则数据，求出每个区的平均房价、最高和最低房价，求出那个区的房价最高和最低，并分别存入csv，xls，xlsx格式，

"""

import requests,os,re
import pandas as pd

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

lists = []

def print_info(i):
    name = ['名称','地区','详细地址','建成年代','均价','在售套数']
    test = pd.DataFrame(columns=name,data=lists)
    test.to_csv("F:/2019技能竞赛/搞事小组/任务五/data"+str(i)+".csv")

def parser(url):
    res = requests.get(url=url,headers=headers).text
    return res

def url_page(html,num):
    """
    <div class="title">\S<a href="https://cs.lianjia.com/xiaoqu/3516638251643452/" target="_blank">南郡雅园</a></div>
    """
    urls = re.findall(r'<a href="(https://cs.lianjia.com/xiaoqu/\d+?/)" target="_blank">',html,re.S)
    j = 0
    for i in urls:
        page_parse(parser(i),num[j])
        print(j)
        j+=1

def turn_page():
    url = 'https://cs.lianjia.com/xiaoqu/pg{}cro21/'
    j = 0
    for i in range(1,15):
        url_ax = url.format(i)
        num = re.findall(r'class="totalSellCount"><span>(\d+?)</span>套</a>',parser(url_ax),re.S)
        url_page(parser(url_ax),num)
        j+=1
        print_info(j)

def page_parse(html,num):
    list = []
    # 小区名称
    name = re.findall(r'<h1 class="detailTitle">(.*?)</h1>',html,re.S)
    list.append(name[0])

    # 所在区域
    """
    长沙小区</a><span class="stp">&nbsp;&gt;&nbsp;</span><a href="https://cs.lianjia.com/xiaoqu/.*?/">(.*?)小区</a>
    """
    area = re.findall(r'长沙小区</a><span class="stp">&nbsp;&gt;&nbsp;</span><a href="https://cs.lianjia.com/xiaoqu/.*?/">(.*?)小区</a>',html,re.S)
    area_end = area[0]+'区'
    list.append(area_end)
    # 详细地址
    """
    <div class="detailDesc">(天心暮云)中意二路758号</div>
    """
    address = re.findall(r'<div class="detailDesc">(.*?)</div>',html,re.S)
    list.append(address[0])
    # 建成年代
    year = re.findall(r'<span class="xiaoquInfoContent">(.*?) </span>',html,re.S)
    list.append(year[0].replace("年建成",""))
    # 均价
    """
    <span class="xiaoquUnitPrice">\d+?</span>
    """
    money = re.findall(r'<span class="xiaoquUnitPrice">(\d+?)</span>',html,re.S)
    list.append(money[0])
    # 在售套数
    num_end = str(num)
    list.append(num_end)
    print(list)
    lists.append(list)

def main():
    turn_page()

if __name__ == '__main__':
    main()