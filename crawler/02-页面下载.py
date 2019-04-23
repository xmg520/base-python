from urllib import request
from urllib import parse

#urlretrieve(网址，本地目录)
# request.urlretrieve('https://www.baidu.com/','./downs/baidu.html')

#urlencode函数的用法
# params = {'name':'张三','age':18,'greet':'hello world'}
# result = parse.urlencode(params)
# print(result)
#name=%E5%BC%A0%E4%B8%89&age=18&greet=hello+world


# url = 'https://www.baidu.com/s'
# params = {'wd':'吴彦祖'}
# qs = parse.urlencode(params)
# url = url + '?'+ qs
# print(url)
# resp = request.urlopen(url)
# print(resp.read())

#parse_qs函数的用法
params = {'name':'张三','age':18,'greet':'hello world'}
qs = parse.urlencode(params)
print(qs)
request = parse.parse_qs(qs)
print(request)