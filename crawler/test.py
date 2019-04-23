from lxml import etree
import requests

BASE_DOMAIN = 'http://dytt8.net'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Referer': 'http://www.ygdy8.net'
}


def get_deatil_urls(url):
    response = requests.get(url, headers=HEADERS)

    # response.text:返回的是一个经过解码后的字符串，是str(unicode)类型
    # response.content:返回的是一个原生的字符串，就是从网页上抓取下来的，没有经过处理
    # 的字符串，是bytes类型
    # requests库，默认会使用猜测的编码方式将抓取下来的网页进行解码，
    # 然后存储到text属性上，在电影天堂的网页中，因为编码方式，requests猜错了，所以就是产生乱码
    # print(response.text)

    # ignore参数，表示在编码和解码时，忽略掉那些无法编码和解码的字符
    # text = response.content.decode('gbk', 'ignore')
    text = response.text
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = map(lambda url: BASE_DOMAIN + url, detail_urls)
    return detail_urls


def parse_detail_page(url):
    '''
    处理电影的详情页面
    :param url:
    :return:
    '''
    movie = {}
    response = requests.get(url, headers=HEADERS)
    text = response.content.decode('gbk', 'ignore')
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    print(title)
    movie['title'] = title

    # 获取电影信息
    zoomE = html.xpath("//div[@id='Zoom']")[0]
    # 获取封面图的src地址
    imgs = zoomE.xpath(".//img/@src")
    # 电影封面图
    cover = imgs[0]
    # 电影截图
    screenshot = imgs[1]
    # 将获取的结果放到字典里
    movie['cover'] = cover
    movie['screenshot'] = screenshot

    def parse_info(info, rule):
        return info.replace(rule, "").strip()

    infos = zoomE.xpath(".//text()")
    # 带索引的遍历
    for index, info in enumerate(infos):
        # startswith :以什么开头
        if info.startswith("◎年　　代"):
            # strip：删除字符串前后的空格
            info = parse_info(info, "◎年　　代")
            movie['year'] = info
        elif info.startswith("◎产　　地"):
            info = parse_info(info, "◎产　　地")
            # print(info)
            movie['country'] = info
        elif info.startswith("◎类　　别"):
            info = parse_info(info, "◎类　　别")
            # print(info)
            movie['category'] = info
        elif info.startswith("◎豆瓣评分"):
            info = parse_info(info, "◎豆瓣评分")
            movie['douban_rating'] = info
        elif info.startswith("◎片　　长"):
            info = parse_info(info, "◎片　　长")
            movie['duration'] = info
        elif info.startswith("◎导　　演"):
            info = parse_info(info, "◎导　　演")
            movie['director'] = info
        # 主演很多列，所以要特殊处理
        elif info.startswith("◎主　　演"):
            info = parse_info(info, "◎主　　演")
            actors = [info]
            for x in range(index + 1, len(infos)):
                actor = infos[x].strip()
                # 到下一个“◎”结束循环
                if actor.startswith("◎"):
                    break
                actors.append(actor)
            # print(actors)
            movie['actors'] = actors
        elif info.startswith("◎简　　介"):
            info = parse_info(info, "◎简　　介")
            for x in range(index + 1, len(infos)):
                profile = infos[x].strip()
                # 【下载地址】开始是结束
                if profile.startswith("【下载地址】"):
                    break
                movie['profile'] = profile
    # 下载地址
    download_url = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")[0]
    # print(download_url)
    movie['download_url'] = download_url
    return movie


def spider():
    base_url = 'http://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html'
    movies = []
    # for是控制总共有7页
    for x in range(1, 8):
        url = base_url.format(x)
        detail_urls = get_deatil_urls(url)
        # for,是遍历一页中所有的电影详情
        for detail_url in detail_urls:
            movie = parse_detail_page(detail_url)
            movies.append(movie)
            print(movie)
        print(movies)


if __name__ == '__main__':
    spider()
