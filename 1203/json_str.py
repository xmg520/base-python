#!/usr/bin/env python
#-*-coding:utf-8-*-
__author__ = '$USER'

import json
"""
1.对象（字典）。使用花括号{}
2.列表（数组）。使用方括号[]
3.整形、浮点数、布尔类型、NULL类型
4.字符串类型（字符串必须要用双引号，不能用单引号）

多个数据之间使用逗号分开。
注意：JSON本质就是一个字符串。
"""

# 字符串传 JSON json.dumps(xxx)
persons = [
    {
        'username':'mzx',
        'sex':'man',
        'age':19,
        "args": {
            "特点":"吃饭、睡觉、打豆豆"
        }
     },
    {
        'username':'myf',
        'sex':'man',
        'age':30
    }
]
# 解决json打印ascii码
json_str = json.dumps(persons,ensure_ascii=False)

print(type(json_str))
print(json_str)

# with open('person.json','w',encoding='utf-8') as fp:
# #     # fp.write(json_str)
# #     json.dump(persons,fp,ensure_ascii=False)


# 错误示范
# class Person(object):
#     count = 'china'
#
# a = {
#     'person':Person()
# }
# json.dumps(a)

json_str_two = '[{"username": "mzx", "sex": "man", "age": 19, "args": {"特点": "吃饭、睡觉、打豆豆"}}, {"username": "myf", "sex": "man", "age": 30}]'

json_str_lists = json.loads(json_str_two)
print(type(json_str_lists))
for i in json_str_lists:
    print(i)