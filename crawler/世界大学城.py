# 导入模块
import requests
from lxml import etree


# 伪装身份
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Referer':'http://www.worlduc.com/SpaceShow/Index.aspx?uid=319173'
}

NAMES = []

def parse_detail_page(url):
    response = requests.get(url=url, headers=headers)

    text = response.text

    html = etree.HTML(text)

    spans = html.xpath("//span[@class='mt5']")
    for s in spans:
        # print(etree.tostring(s,encoding='utf-8').decode('utf-8'))
        name = s.xpath(".//text()")
        NAMES.append(name)


def spider():
    url = 'http://www.worlduc.com/SpaceShow/leaveword/List.aspx?uid=319173&Page={}'
    for x in range(1,8):
        detail_url = url.format(x)
        parse_detail_page(detail_url)
    print(NAMES)

if __name__ == '__main__':
    spider()