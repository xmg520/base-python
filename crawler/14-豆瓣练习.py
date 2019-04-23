
import requests
from lxml import etree

# 1.把目标网站页面抓取下来
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Referer':'https://movie.douban.com/'
}

url = 'https://movie.douban.com/cinema/nowplaying/changsha/'

response = requests.get(url,headers=headers)
text = response.text

# print(response.text)
#response.text ：返回一个经过解码后的字符串，是str 类
#response.content ：返回的一个原生字符串，没有经过处理的字符串 是bytes类型
# 2.把抓取下来的数据根据一定的规则进行提取
html = etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[0]
# print(etree.tostring(ul,encoding='utf-8').decode('utf-8'))
lis = ul.xpath("./li")
plcs = []
for li in lis:
    title = li.xpath("./@data-title")
    duration = li.xpath("./@data-duration")
    score = li.xpath("./@data-score")
    region = li.xpath("./@data-region")
    thumbnail = li.xpath(".//img/@src")
    plc = {
        '电影':title,
        '片长':duration,
        '评分':score,
        '上映地点':region,
        '图片地址':thumbnail
    }
    plcs.append(plc)

for pl in plcs:
    print(pl)