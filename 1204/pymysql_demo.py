#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'

import pymysql

# def conn(sql):
#     conn = pymysql.connect(host='localhost',user='root',password="1234",database='pymysql_demo',port=3306)
#     cursor = conn.cursor()
#     cursor.execute(sql)
#     conn.commit()
#     conn.close()
#
# if __name__ == '__main__':
#     # 插入 insert into user(id,username,age,password) values(2,吴彦祖,18,1234)
#     # insert_sql = """
#     # insert into user(id,username,age,password) values(NULL,"吴彦祖",18,1234)
#     # """
#
#     username = 'spider'
#     age = 21
#     password = '9034'
#
#     insert_sql = """
#         insert into user (id,username,age,password) values (null,%s,%s,%s)
#     """
#     conn(insert_sql)

conn = pymysql.connect(host='localhost',user='root',password='1234',database='pymysql_demo',port=3306)
cursor = conn.cursor()

insert_sql = """
    insert into user (id,username,age,password) values (null,%s,%s,%s)
"""

username = 'spider'
age = 21
password = '9034'

cursor.execute(insert_sql,(username,age,password))
conn.commit()
conn.close()