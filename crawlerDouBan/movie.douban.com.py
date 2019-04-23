"""
环境：python3 + requests + windows + re
目标网站：http://58921.com/alltime/wangpiao
目的：所有电影名
"""
import requests,re

url = "http://58921.com/alltime/wangpiao?page={}"

# 翻页
for i in range(10):
    url_end = url.format(i)
    # 页面解析
    response = requests.get(url_end)
    response.encoding = 'utf-8'
    text = response.text
    # 获取电影名
    names = re.findall(r'<a href="/film/\d+?" title="(.*?)">', text)
    for j in names:
        print(j)