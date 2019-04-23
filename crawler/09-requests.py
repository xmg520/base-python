import requests

# url = 'http://www.baidu.com/'
# response = requests.get(url)

#返回unicode格式的数据
# print(type(response.text))
# print(response.text)

#返回content 字节流数据
# print(type(response.content))
# print(response.content.decode('utf-8'))

# print(response.url)
# print(response.encoding)
# print(response.status_code)

params = {
    'wd':'吴彦祖'
}

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

#get与post请求方法
response = requests.get('https://www.baidu.com/s',params=params,headers=headers)

with open('baidu.html','w',encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))