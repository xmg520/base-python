
# 人人网大鹏 ：http://www.renren.com/880151247/profile
# 人人网登陆：'http://www.renren.com/PLogin.do'

import requests

url = 'http://www.renren.com/PLogin.do'

headers = {
     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
     'Accept-Language': 'en',
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
}

data = {
    'email':'903563099@qq.com',
    'password':'mzx159'
}

session = requests.session()

session.post(url=url,data=data,headers=headers)

response = session.get('http://www.renren.com/880151247/profile')

with open('renrendap.html','w',encoding='utf-8') as fp:
    fp.write(response.text)