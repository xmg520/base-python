
# 人人网大鹏 ：http://www.renren.com/880151247/profile
# 人人网登陆：http://www.renren.com/SysHome.do


from urllib import request

#1. 不适用 Cookie 去请求大鹏的主页

dapeng_url = 'http://www.renren.com/880151247/profile'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Cookie':'JSESSIONID=abc4zR2YAoJ-y-Te8MHBw; _r01_=1; anonymid=jo3nv3z3mzmx33; depovince=HUN; ick_login=d1b216eb-4ac2-47c1-b1fe-984a2ca44586; first_login_flag=1; ln_uact=903563099@qq.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20140215/1355/h_main_iFrd_cd6500000f29111a.jpg; jebecookies=0ae16066-2551-4e52-9b1d-e327625f0e62|||||; jebe_key=4c1cc7bb-886f-46d6-8603-212e91a0b6a0%7Ccfcd208495d565ef66e7dff9f98764da%7C1541384381530%7C0; _de=E448D232DB35D629E2A69D838E8B6F33696BF75400CE19CC; p=c90535d97fbb35e4c3899c80d8cd96a86; t=6d5b2583b8d03fe609b6bc343d7d3e936; societyguester=6d5b2583b8d03fe609b6bc343d7d3e936; id=583176036; xnsid=1e52f8a0; loginfrom=syshome'
}

req = request.Request(url=dapeng_url,headers=headers)

resp = request.urlopen(req)

# print(resp.read().decode('utf-8'))
with open('dapeng_renren.html','w',encoding='utf-8') as fp:
    # write函数必须写入一个 str 的数据类型
    # resp.read()读出来的是一个bytes 数据类型
    # bytes -> decode -> str
    # str -> decode -> bytes
    fp.write(resp.read().decode('utf-8'))