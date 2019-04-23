#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'

import csv


def read_csv_demo1():
    with open('test.csv','r') as fp:
        # reader 是一个迭代器
        reader = csv.reader(fp)
        # 执行以为next 指针会向下一位读取
        next(reader)
        for i in reader:
            name = i[0]
            money = i[-1]
            print({'name':name,'money':money})

def read_csv_demo2():
    with open('test.csv','r') as fp:
        # 用DictReader创建的reader对象
        # 不会包涵标题 行的数据
        # reader 是一个迭代器
        reader = csv.DictReader(fp)
        for i in reader:
            # print(i)
            # OrderedDict([('name', '南郡雅园'), ('pro', '天心小区'), ('address', '(天心暮云)中意二路758号'), ('year', '暂无信息 '), ('taoshu', '0'), ('moy', '3821')]) 字典形式
            value = {'name':i['name'],'moy':i['moy']}
            print(value)

if __name__ == '__main__':
    read_csv_demo2()