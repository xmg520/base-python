import requests
from lxml import etree

BASE_DOMAIN = 'http://www.ygdy8.net'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Referer':' http://www.ygdy8.net/html/gndy/dyzz/list_23_2.html'
}


def get_datail_urls(url):

    response = requests.get(url=url, headers=HEADERS)

    text = response.text

    html = etree.HTML(text)

    detail_urls = html.xpath(".//table[@class='tbspan']//a/@href")
    detail_urls = map(lambda url:BASE_DOMAIN+url,detail_urls)
    return detail_urls

# 单个页面的处理
def parse_detail_page(url):
    movie = {}
    response = requests.get(url,headers=HEADERS)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")
    movie['电影名称'] = title
    zoomE = html.xpath("//div[@id='Zoom']")[0]
    imgs = zoomE.xpath(".//img/@src")
    cover = imgs[0]
    screenshot = imgs[1]
    movie['海报图'] = cover
    movie['电影截图'] = screenshot

    def parse_info(info,rule):
        return info.replace(rule,"").strip()

    infos = zoomE.xpath(".//text()")
    for index,info in enumerate(infos):
        if info.startswith("◎年　　代"): # startswith()查找以 XXX 开头的
            info = info.replace("◎年　　代","").strip() #strip 去除str 前后空格
            movie['年代'] = info
        elif info.startswith("◎类　　别"):
            info = parse_info(info,"◎类　　别")
            movie['类别'] = info
        elif info.startswith("◎豆瓣评分"):
            info = parse_info(info,'◎豆瓣评分')
            movie['豆瓣评分'] = info
        elif info.startswith("◎片　　长"):
            info = parse_info(info,'◎片　　长')
            movie['片长'] = info
        elif info.startswith("◎简　　介"):
            info = parse_info(info,"◎简　　介")
            for i in range(index+1,len(infos)):
                profile = infos[i].strip()
                movie['简介'] = profile
    download_url = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")
    movie['下载'] = download_url
    return movie


def spider():
    base_url = 'http://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html'
    # 第一个for循环，是用来控制总共有7页的
    #定义列表
    movies = []

    for x in range(1,8):
        url = base_url.format(x)
        print(url)
        detail_urls = get_datail_urls(url)
        # 第二个for循环，是用来遍历一页中所有电影的 详情
        # for detail_url in detail_urls:
        #     movie = parse_detail_page(detail_url)
        #     movies.append(movie)
        #     print(movie)
    # print(movies)
if __name__ == '__main__':
    spider()