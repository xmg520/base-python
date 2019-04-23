#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'


import pymysql,csv

conn = pymysql.connect(host='localhost',user='root',password='1234',database='pymysql_demo',port=3306)

cursor = conn.cursor()

sql = """
    insert into weather(id,city,province,temperature) values (%s,%s,%s,%s) 
"""

with open("test.csv","r",encoding='utf-8',newline='') as fp:
    reader = csv.DictReader(fp)

    for i in reader:
        id = i['id']
        city = i['city']
        province = i['province']
        temperature = i['temperature']
        cursor.execute(sql,(id,city,province,temperature))
        conn.commit()
conn.close()