import requests

from lxml import etree

url = 'https://movie.douban.com/cinema/nowplaying/changsha/'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Referer':'https://movie.douban.com/cinema/nowplaying/changsha/'
}

response = requests.get(url=url,headers=headers)
text  = response.text

html = etree.HTML(text)

trs = html.xpath("//ul[@class='lists']")[0]
pls = []

for tr in trs:
    title = tr.xpath(".//@data-title")
    score = tr.xpath(".//@data-score")
    duration = tr.xpath(".//data-duration")
    region = tr.xpath(".//data-region")

    pl = {
        '电影名':title,
        '评分':score,
        '时长':duration,
        '上映地址':region
    }
    pls.append(pl)