import requests,re,os

# 电影名，年份信息
page_urls = []

# 爬取目标网站
url = 'http://58921.com/alltime/'

# 信息头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'
}

# 获取页面解析
text_html = requests.get(url,headers)

# 解析页面设置转码
text_html.encoding='utf-8'

# 匹配所有年份
year = re.findall(r'<a href="(/alltime/\d+?)" title="\d+?">\d+?</a>',text_html.text)

# 解析函数方法
def parse(url):
    text = requests.get(url,headers)
    text.encoding='utf-8'
    return text.text

# 输出详细信息方法
def outPut():
    pass

# 获取页面详细信息方法
def parse_page(url):
    response_text = parse(url)
    print(response_text)



# 单页面获取目标详细页面方法
def parse_url(url):
    text = requests.get(url,headers)
    text.encoding = 'utf-8'
    response_text = text.text

    """
    film/5331
    """
    urls = re.findall(r'<a href="(/film/\d+?)" title=".*?">',response_text,re.S);
    if urls:
        for i in urls:
            page_urls.append("http://58921.com"+i)
            # print("http://58921.com"+i)



# 爬取每个年份前两页(若有两页)下的数据
for i in range(year.__len__()):
    url = 'http://58921.com'+year[i]
    two_page = re.findall(r'转到第 2 页',parse(url))
    # 判断是否有两页数据，并分别把数据写入 names、years 列表
    if two_page:
        for j in range(2):
            url_parse = url+'?page='+str(j)
            # print(url_parse)
            parse_url(url_parse)
    else:
        url_parse = url + '?page=0'
        parse_url(url_parse)

for i in range(page_urls.__len__()):
    parse_page(page_urls[i])
    break

# 把names、years 列表中数据 写出到本地文件
# with open('test.log','w',encoding='utf-8',newline='') as fp:
#     fp.writelines("电影名,年份\n")
#     for i in range(names.__len__()):
#         fp.writelines(names[i]+","+str(years[i])+'\n')
