#!/usr/bin/env python
#coding:utf-8

import pandas as pd




def print_info(url,name):
    house = pd.read_csv(url, encoding='gbk')


    price = house['price']
    # 最大值
    max_price = price.max()
    min_price = price.min()
    mean_price = price.mean()
    median_price = price.median()


    print(name,"最大房价",max_price)
    print(name,"最低房价",min_price)
    print(name,"中间房价",mean_price)
    # print(median_price)

def main():
    url = './data/data{}.csv'
    list = ['芙蓉区','开福区','天心区','望城区','雨花区','岳麓区','长沙县区']
    for i in range(7):
        url_ax = url.format(i+1)
        print_info(url_ax,list[i])
        print("*"*30)


if __name__ == '__main__':
    main()