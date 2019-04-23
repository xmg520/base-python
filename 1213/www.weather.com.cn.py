#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'

import requests,os,re,json,csv

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}

url = "http://www.weather.com.cn/"

response = requests.get(url=url,headers=headers).content.decode(encoding='utf-8')#解决python3爬取中文乱码问题

# response.encoding = response.apparent_encoding #解决python3爬取中文乱码问题

"""
      <ul class="on">

<span class="ord"><i>1</i></span><span class="city"><a href="http://www.weather.com.cn/weather1d/101050703.shtml" target="_blank">漠河</a></span><span class="prov"><a href="http://www.weather.com.cn/html/province/heilongjiang.shtml" target="_blank">黑龙江</a></span><span class="wd">-38℃<span class="wdTime">(05时)</span></span></li><li>
<span class="ord"><i>2</i></span><span class="city"><a href="http://www.weather.com.cn/weather1d/101050705.shtml" target="_blank">呼中</a></span><span class="prov"><a href="http://www.weather.com.cn/html/province/heilongjiang.shtml" target="_blank">黑龙江</a></span><span class="wd">-37℃<span class="wdTime">(07时)</span></span></li><li>
<span class="ord"><i>3</i></span><span class="city"><a href="http://www.weather.com.cn/weather1d/101050704.shtml" target="_blank">呼玛</a></span><span class="prov"><a href="http://www.weather.com.cn/html/province/heilongjiang.shtml" target="_blank">黑龙江</a></span><span class="wd">-36℃<span class="wdTime">(07时)</span></span></li><li>
<span class="ord"><i>4</i></span><span class="city"><a href="http://www.weather.com.cn/weather1d/101081016.shtml" target="_blank">图里河</a></span><span class="prov"><a href="http://www.weather.com.cn/html/province/neimenggu.shtml" target="_blank">内蒙古</a></span><span class="wd">-35℃<span class="wdTime">(05时)</span></span></li><li>
<span class="ord"><i>5</i></span><span class="city"><a href="http://www.weather.com.cn/weather1d/101050702.shtml" target="_blank">塔河</a></span><span class="prov"><a href="http://www.weather.com.cn/html/province/heilongjiang.shtml" target="_blank">黑龙江</a></span><span class="wd">-34℃<span class="wdTime">(04时)</span></span></li><li>
<span class="ord"><i>6</i></span><span class="city"><a href="http://www.weather.com.cn/weather1d/101081015.shtml" target="_blank">根河</a></span><span class="prov"><a href="http://www.weather.com.cn/html/province/neimenggu.shtml" target="_blank">内蒙古</a></span><span class="wd">-34℃<span class="wdTime">(07时)</span></span></li><li>
<span class="ord"><i>7</i></span><span class="city"><a href="http://www.weather.com.cn/weather1d/101050706.shtml" target="_blank">新林</a></span><span class="prov"><a href="http://www.weather.com.cn/html/province/heilongjiang.shtml" target="_blank">黑龙江</a></span><span class="wd">-34℃<span class="wdTime">(07时)</span></span></li><li>
<span class="ord"><i>8</i></span><span class="city"><a href="http://www.weather.com.cn/weather1d/101081014.shtml" target="_blank">额尔古纳</a></span><span class="prov"><a href="http://www.weather.com.cn/html/province/neimenggu.shtml" target="_blank">内蒙古</a></span><span class="wd">-33℃<span class="wdTime">(07时)</span></span></li><li>
<span class="ord"><i>9</i></span><span class="city"><a href="http://www.weather.com.cn/weather1d/101050802.shtml" target="_blank">乌伊岭</a></span><span class="prov"><a href="http://www.weather.com.cn/html/province/heilongjiang.shtml" target="_blank">黑龙江</a></span><span class="wd">-31℃<span class="wdTime">(05时)</span></span></li><li>
<span class="ord"><i>10</i></span><span class="city"><a href="http://www.weather.com.cn/weather1d/101050805.shtml" target="_blank">嘉荫</a></span><span class="prov"><a href="http://www.weather.com.cn/html/province/heilongjiang.shtml" target="_blank">黑龙江</a></span><span class="wd">-30℃<span class="wdTime">(08时)</span></span></li>

"""
# print(response)

ids = []
citys = []
provinces = []
temperatures = []
parse = []
value = []

# 序号
id = re.findall(r'span class="ord"><i>(\d+?)</i></span>',response)
for i in range(0,10):
    ids.append(id[i])
# print(id)

# 城市
city = re.findall(r'<span class="city"><a href=".*?" target="_blank">(.*?)</a>',response)
for i in range(0,10):
    citys.append(city[i])
# print(city)

# 省份
province = re.findall(r'<span class="prov"><a href=".*?" target="_blank">(.*?)</a>',response)
for i in range(0,10):
    provinces.append(province[i])
# print(province)

# 温度
temperature = re.findall(r'</span><span class="wd">(.*?)<',response)
for i in range(0,10):
    temperatures.append(temperature[i])


for i in range(0,10):
    """
        values = [
        {'username':'张三','age':18,'height':180},
        {'username':'李四','age':19,'height':190},
        {'username':'王五','age':20,'height':200}
        ]
    """

    line = '{"id":'+ids[i]+","+'"city":"'+citys[i]+'","province":"'+provinces[i]+'","temperature":"'+temperatures[i]+'"}'
    line_json = json.loads(line)
    print(line_json)
    # parse.append(line_json)

title = ['id','city','province','temperature']

with open('test.csv','w',encoding='utf-8',newline='') as fp :
    writer = csv.DictWriter(fp,title)
    writer.writeheader()
    writer.writerows(parse)


# name = re.findall(r'<li class="on"><span class="ord"><i>(\d+?)</i></span><span class="city"><a href=".*?" target="_blank">(.*?)</a></span><span class="prov"><a href=".*?" target="_blank">(.*?)</a></span><span class="wd">(.*?)</span></li>',response)
#
# print(name)