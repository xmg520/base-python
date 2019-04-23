#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'

import pymysql

conn = pymysql.connect(host='localhost',user='root',password='1234',database='pymysql_demo',port=3306)
cursor = conn.cursor()

sql = """
    select * from user
"""

cursor.execute(sql)
# # result = cursor.fetchone()
# results = cursor.fetchall()
# print(results)

# while True:
#     result = cursor.fetchone()
#     if result :
#         print(result)
#     else:
#         break
# results = cursor.fetchall()
# for i in results:
#     print(i)

# 查找指定 个 个数
# results = cursor.fetchmany(2)
# for i in results:
#     print(i)

conn.close()