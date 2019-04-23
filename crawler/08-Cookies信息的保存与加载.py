from urllib import request
from http.cookiejar import MozillaCookieJar

cookiejar = MozillaCookieJar('cookie.txt')#此处写了变量名后，后面save 与 load 就不用再写

cookiejar.load(ignore_discard=True)

handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

url = 'http://httpbin.org/cookies/set?course=abc'
resp = opener.open(url)

for cookie in cookiejar:
    print(cookie)

#保存cookie  ignore_discard=True 即将过期的cookie也会保存
# cookiejar.save(ignore_discard=True)