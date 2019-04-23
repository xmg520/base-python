
# 人人网大鹏 ：http://www.renren.com/880151247/profile
# 人人网登陆：'http://www.renren.com/PLogin.do'

from urllib import request,parse
from http.cookiejar import CookieJar

# 1.1 登陆
# 1.2 创建一个Cookiejar对象
cookiejar = CookieJar()
# 1.3 使用Cookiejar 创建一个 HTTPPCookieProcessor 对象
handler = request.HTTPCookieProcessor(cookiejar)
# 1.4 使用上一步创建的handler创建一个opener
opener = request.build_opener(handler)
# 1.5 使用 opener发送登陆的请求 （人人网的邮箱和密码）
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

data = {
    'email':"903563099@qq.com",
    'password':"mzx159"
}

login_url = 'http://www.renren.com/PLogin.do'
req = request.Request(login_url,data=parse.urlencode(data).encode('utf-8'),headers=headers)
opener.open(req)

#1.6 访问个人主页
dapeng_url = 'http://www.renren.com/880151247/profile'

#获取个人主页页面的时候，不要新建一个opner 而应该使用之前的那个opener 因为之前那个opener已经包含了登陆所需要的cookie信息
req = request.Request(dapeng_url,headers=headers)
resq = opener.open(req)

with open('renren1.html','w',encoding='utf-8') as fp:
    fp.write(resq.read().decode('utf-8'))

