import requests

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

data = {
    'first':'true',
    'pn':1,
    'kd':'java'
}

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Referer':'https://www.lagou.com/jobs/list_java?labelWords=&fromSearch=true&suginput='
}



response = requests.post(url=url,data=data,headers=headers)

# print(response.text)

#json() json字符串类型 转成  字典
print(response.json())