import requests,re

names = set()

def main():
    #用户指定爬取几页代码
    for_url(7)
    #打印set()集合中的所有名字，由于set的特性 所以其中并不会有重复代码
    print(names)

#翻页方法
def for_url(inp):
    url = 'http://www.worlduc.com/SpaceShow/leaveword/List.aspx?uid=319173&Page={}'
    for i in range(1, inp+1):
        datail_url = url.format(i)
        parse_detail_page(datail_url)



#单页处理函数，提取本页面所有的姓名并添加到set函数中
def parse_detail_page(url):
    html = requests.get(url)
    text = html.text
    # 正则代码
    name = re.findall(r'<span class="mt5"><a href=".*?" target="_blank">(.*?)</a></span>',text)
    for n in name:
        names.add(n)




if __name__ == '__main__':
    main()
