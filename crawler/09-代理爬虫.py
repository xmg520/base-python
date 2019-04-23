import requests


#{"http":"221.193.222.7:8060"})

proxy = {
    'http':'221.193.222.7:8060'
}

url = 'http://httpbin.org/ip'

#url,proxies
response = requests.get(url=url,proxies=proxy)
print(response.text)