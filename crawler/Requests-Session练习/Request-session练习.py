# #!/usr/bin/env python
# #-*-coding:utf-8-*-
# __author__ = 'Mzx'
import requests
# # python2 和 python3的兼容代码
# # try:
# #     # python2 中
# #     import cookielib
# #     print(f"user cookielib in python2.")
# # except:
# #     # python3 中
# #     import http.cookiejar as cookielib
# #     print(f"user cookielib in python3.")
#
# bbsSession = requests.session()
# # bbsSession.cookies = cookielib.LWPCookieJar(filename='bbsCookies.txt')
#
# trurl = 'http://segmentfault.com/user/login'
#
# data = {
#     'username':'15211046933',
#     'password':'mzx159'
# }
#
# header = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Language': 'en',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
# }
#
#
#
# def  bbsLogin():
#     # responseRes = bbsSession.post(trurl,data,header)
#     bbsSession.get(url=trurl,data=data,headers=header)
#     r = bbsSession.get(url='https://segmentfault.com/u/badman_5c7bc70010f1a ')
#     print(r.text)
#     # print(f"statusCode = {responseRes.status_code}")
#     # print(f"text = {responseRes.text}")
#     # bbsSession.cookies.save()
#     # isLoginStatus()
#
#
# def isLoginStatus():
#     # 通过访问个人中心页面的返回状态码来判断是否为登录状态
#     routeUrl = 'https://bbs.wyjsjxh.com/my.htm'
#
#     # 下面有两个关键点
#     # 第一个是header，如果不设置，会返回500的错误
#     # 第二个是allow_redirects，如果不设置，session访问时，服务器返回302，
#     # 然后session会自动重定向到登录页面，获取到登录页面之后，变成200的状态码
#     # allow_redirects = False  就是不允许重定向
#     responseRes = bbsSession.get(url=url,headers=header,allow_redirects=False)
#     # print(f"text = {responseRes.text}")
#     print(f"isLoginStatus = {responseRes.status_code}")
#     if responseRes.status_code != 200:
#         print("Cookie登陆失败")
#     else:
#         print("Cookie登陆成功")
#
#
# if __name__ == "__main__":
#     bbsLogin()

s = requests.session()
login_data = {'email': '15211046933', 'password': 'wolaoma520', }
# post 数据实现登录
s.post('http://www.zhihu.com/login', login_data)
# 验证是否登陆成功，抓取'知乎'首页看看内容
r = s.get('http://www.zhihu.com')
print(r.text)