#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'

import time,threading

def coding():
    for x in range(3):
        print("这正在写代码%s"%x)
def drawing():
    for x in range(3):
        print("这正在画图%s"%x)

def main():
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)

    t1.start()
    t2.start()

if __name__ == '__main__':
    main()