#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'

import pymysql,csv

conn = pymysql.connect(host='localhost',user='root',password='1234',database='pymysql_demo',port=3306)

cursor = conn.cursor()

sql = """
    insert into filmType(id,name,num) values (null,%s,%s)
"""

with open('data.csv','r',encoding='utf-8',newline='') as fp:
    reader = csv.DictReader(fp)
    # print(reader)
    for i in reader:
        name = i['name'],
        works = i['num']
        cursor.execute(sql,(name,works))
        conn.commit()

conn.close()