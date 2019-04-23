#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'

import requests,re
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=',
    'Cookie': 'JSESSIONID=ABAAABAAADEAAFI46B1371E4A9C0A3D1E95BD94A3B1930E; _ga=GA1.2.153359104.1546942766; user_trace_token=20190108181927-cc834b32639940cf96f429423ff57edb; LGUID=20190108181927-e0e065d3-132e-11e9-b2be-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1546942766; _gid=GA1.2.1545535845.1547381875; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; X_MIDDLE_TOKEN=f52af67a85212ae2bb0b53910d9a8a4c; LGSID=20190113224707-1974f5fe-1742-11e9-ad59-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2F4123246.html; _gat=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216847c7726d62d-0452ae818a2b27-6313363-1044480-16847c7726ea1d%22%2C%22%24device_id%22%3A%2216847c7726d62d-0452ae818a2b27-6313363-1044480-16847c7726ea1d%22%7D; sajssdk_2015_cross_new_user=1; _putrc=BD045E652958CF65123F89F2B170EADC; login=true; unick=%E9%A9%AC%E7%AB%A0%E8%BD%A9; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=afe2a387a3684f3487c8990617b779174aba2817cdf4b1fe46581525ff2d9be3; SEARCH_ID=0d20e501445e489488a90690f0a53bec; LGRID=20190113231603-244422e9-1746-11e9-ad5b-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1547392563',
    'Origin':'https://www.lagou.com',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest'
}

def parse_positon(url):
    response = requests.post(url=url,headers=headers)
    response.encoding = 'utf-8'
    text = response.text
    html = etree.HTML(text)
    # 职位名称
    position_name = html.xpath("//span[@class='name']/text()")[0]
    job_request_spans = html.xpath("//dd[@class='job_request']//span")
    salary_span = job_request_spans[0]
    # 工资
    salary = salary_span.xpath(".//text()")[0].strip()
    # 所在城市
    city = job_request_spans[1].xpath(".//text()")[0].strip()
    city = re.sub(r'[\s/]','',city)
    # 经验不限
    work_years = job_request_spans[2].xpath(".//text()")[0].strip()
    work_years = re.sub(r"[\s/]","",work_years)
    # 学历
    education = job_request_spans[3].xpath(".//text()")[0].strip()
    education = re.sub(r"[\s/]","",education)
    # 是否全职
    work_time = job_request_spans[4].xpath(".//text()")[0].strip()
    # 职位诱惑：
    advantage = html.xpath("//dd[@class='job-advantage']/p/text()")[0].strip()
    # 职位描述
    desc = "".join(html.xpath("//div[@class='job-detail']//text()")).strip()

    page_context = "position_name"
    print("职位名称:"+position_name
          +"\n所在城市:"+city
          +"\n经验不限:"+work_years
          +"\n学历:"+education
          +"\n是否全职:"+work_time
          +"\n职位诱惑:"+advantage
          +"\n"+desc
          +"\n"+"="*50
          +"\n")
    with open('doubanRequest.txt','a',encoding='utf-8',newline='') as fp:
        fp.writelines("职位名称:"+position_name
          +"\n所在城市:"+city
          +"\n经验不限:"+work_years
          +"\n学历:"+education
          +"\n是否全职:"+work_time
          +"\n职位诱惑:"+advantage
          +"\n"+desc
          +"\n"+"="*50
          +"\n")
    fp.close()

def request_list_page():
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

    data = {
        'first':'false',
        'pn':1,
        'kd':'python'
    }
    for i in range(1,14):
        data['pn'] = i
        response = requests.post(url=url,headers=headers,data=data)
        text = response.json()
        positons = text['content']['positionResult']['result']
        for i in positons:
            psId = i['positionId']
            positon_url = 'https://www.lagou.com/jobs/%d.html' % psId
            parse_positon(positon_url)


def main():
    request_list_page()
if __name__ == '__main__':
    main()