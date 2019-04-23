#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'

import pymysql

conn = pymysql.connect(host='localhost',user='root',password='1234',database='pymysql_demo',port=3306)

cursor = conn.cursor()

cursor.execute("select 1")

result = cursor.fetchall()
print(result)

conn.close()