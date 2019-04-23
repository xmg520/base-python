#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'
import datetime as dt

print(dt.datetime.now())#返回默认格式的当前时间

print(dt.datetime(2017,6,1,hour=13,minute=17,second=28)) # 在设置年月日 后面可以设置 hour、minute、second 制作成指定的小时分钟秒

print(dt.datetime.today()) # 获取此时此刻时间

"""
%a	星期的英文单词的缩写：如星期一， 则返回 Mon
%A	星期的英文单词的全拼：如星期一，返回 Monday
%b	月份的英文单词的缩写：如一月， 则返回 Jan
%B	月份的引文单词的缩写：如一月， 则返回 January
%c	返回datetime的字符串表示，如03/08/15 23:01:26
%d	返回的是当前时间是当前月的第几天
%f	微秒的表示： 范围: [0,999999]
%H	以24小时制表示当前小时
%I	以12小时制表示当前小时
%j	返回 当天是当年的第几天 范围[001,366]
%m	返回月份 范围[0,12]
%M	返回分钟数 范围 [0,59]
%P	返回是上午还是下午–AM or PM
%S	返回秒数 范围 [0,61]。。。手册说明的
%U	返回当周是当年的第几周 以周日为第一天
%W	返回当周是当年的第几周 以周一为第一天
%w	当天在当周的天数，范围为[0, 6]，6表示星期天
%x	日期的字符串表示 ：03/08/15
%X	时间的字符串表示 ：23:22:08
%y	两个数字表示的年份 15
%Y	四个数字表示的年份 2015
%z	与utc时间的间隔 （如果是本地时间，返回空字符串）
%Z	时区名称（如果是本地时间，返回空字符串）

"""


print(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f'))

print(dt.datetime.now().strftime('%H:%M:%S'))#格式化自定义时间
print(dt.datetime.now().__format__('%H-%M-%S')) # __format__方法在datetime中 等同于 strftime方法