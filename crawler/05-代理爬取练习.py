from urllib import request

#代理前
url = 'http://httpbin.org/ip'
req = request.urlopen(url)
print(req.read())

#使用代理
#构建一个handler
handler = request.ProxyHandler({'http':'221.193.222.7:8060'})
opener = request.build_opener(handler)

resp = opener.open(url)
print(resp.read())