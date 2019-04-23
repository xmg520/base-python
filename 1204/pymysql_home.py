#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'

import pymysql,csv

conn = pymysql.connect(host='localhost',user='root',password='1234',database='pymysql_demo',port=3306)

cursor = conn.cursor()

sql = """
    insert into home(id,name,pro,address,year,num,price) values (null,%s,%s,%s,%s,%s,%s)
"""

with open('test.csv','r') as fp:
    reader = csv.DictReader(fp)
    for i in reader:
        name = i['name']
        pro = i['pro']
        address = i['address']
        year = i['year']
        num = i['taoshu']
        price = i['moy']
        cursor.execute(sql,(name,pro,address,year,num,price))
        conn.commit()

conn.close()