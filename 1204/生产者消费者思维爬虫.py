#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'
# 正则读写模块
import re,os
# 获取网页模块
import requests
# 队列模块
from queue import Queue
# 多线程类
import threading

import urllib.request

# 生产者
class Procuder(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Procuder,self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self,url):
        response = requests.get(url=url,headers=self.headers)
        html = response.text
        img_urls = re.findall(r'data-original="(.*?)" alt=',html)
        names = re.findall(r'alt="(.*?)" class=', html)
        j = 0
        for i in names:
            img_url = img_urls[j]
            j+=1
            suffix = os.path.splitext(img_url)[1]
            name = re.sub(r'[\sS\.,。!！\?？]','',i)
            filename = name+suffix
            self.img_queue.put((img_url,filename))


# 消费者
class Consumer(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Consumer,self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty() and self.img_queue.empty():
                break
            img_url,filename = self.img_queue.get()
            urllib.request.urlretrieve(img_url,'image/'+filename)
            print(filename+'下载完成')

def main():
    page_queue = Queue(100)
    img_queue = Queue(1000)
    url = 'http://www.doutula.com/photo/list/?page={}'
    for i in range(1,101):
        url_ax = url.format(i)
        page_queue.put(url_ax)

    # 分别启动 Procuder线程 Consumer线程
    for x in range(5):
        t = Procuder(page_queue,img_queue)
        t.start()
    for x in range(5):
        t = Consumer(page_queue,img_queue)
        t.start()

if __name__ == '__main__':
    main()