# from urllib import request,parse
#
# url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
#
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
#     'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
# }
#
# data = {
#     'first':'true',
#     'pn':1,
#     'kd':'python'
# }
#
# req = request.Request(url,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST')
#
# requ = request.urlopen(req)
#
# print(requ.read().decode('utf-8'))

from urllib import request,parse

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
res = request.Request(url,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST')

resp = request.urlopen(res)

print(resp.read().decode('utf-8'))
