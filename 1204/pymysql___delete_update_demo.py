#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'

import pymysql

conn = pymysql.connect(host='localhost',user='root',password='1234',database='pymysql_demo',port=3306)
cursor = conn.cursor()

# 删除代码
# delete from user where id = ?

# delete_sql = """
# delete from user where id = 1
# """
# cursor.execute(delete_sql)

# 除了查找以外， 插入，删除，更新（都需要执行commit操作）


# 更新代码
# update user set username='aaa' where id = 3

update_sql = """
update user set username="吴彦祖" where id = 3
"""
cursor.execute(update_sql)

conn.commit()
conn.close()