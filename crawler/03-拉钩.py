from urllib import request,parse

#url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
#url = 'http://test.wyjsjxh.com/index.php/wap/index/login.html'

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
}

data = {
    'first':'true',
    'pn':1,
    'kd':'python'
}

req = request.Request(url,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST')

resp = request.urlopen(req)

print(resp.read().decode('utf-8'))