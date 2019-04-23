#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'

import requests,json

url = 'https://s.taobao.com/search?q=%E6%B8%B8%E6%88%8F%E4%B8%BB%E6%9C%BA&imgfile=&js=1&style=grid&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190325&ie=utf8'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'cookie':'thw=cn; t=e03c3391c7ad5e7b8539450625e24dca; cookie2=16804e803cff4738a65f3fd77a526190; _tb_token_=76bd5be1b433e; cna=CPJrFJ4GcHICAdpok1Tbi/x1; tg=0; enc=KCy3MsXXWCQDp%2FTQD6p%2FrNoYQeug5kO3jsIFa%2BGxO%2FBBj4hyNgfJfVMcIInIrIurBmBivotmgjcPozeeJiHhww%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; swfstore=163305; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; UM_distinctid=16724418914801-0ace6c97681c0d-4313362-1fa400-16724418915a83; miid=1078846543250486701; v=0; tracknick=ma903563099; lgc=ma903563099; dnk=ma903563099; tk_trace=oTRxOWSBNwn9dPyorMJE%2FoPdY8zZPEr%2FCrvCMS%2BG3sTRRWrQ%2BVVTl09ME1KrX3XAa5vvBwNgqmDt9YzCZ11uh17PD6BgY1xI68S%2FTvjLEd3XAiFikNyIP%2BoGouUqvT0idn7aD2qN8DwAtheaDAhWmdsin3rJYyW2cifhfgyHJReU2cXdCCi9kYjplEZ7t3xxBPx38MkUq5ZDzCK2jLAK%2BdPGZBuMQn%2F%2Bjrk3rpParSOI4YDvlLdr0TnBIS7LiMET7hwsV%2F9cdJCCw6enIN9Pjim4YQEPzcFF1U9BNErRPaM8ClcHYZ4zf4dHY4LlQFdKwcK1VW1DARMvd6sNt0vtOzji; skt=86459f2d5dc59424; csg=701dfa9c; uc3=vt3=F8dByErWzbzUONVeYkQ%3D&id2=UojSLcWw30uG%2Bw%3D%3D&nk2=DlH%2F4kQUACrD%2BvE%3D&lg2=UtASsssmOIJ0bQ%3D%3D; existShop=MTU1MzA3MzIwNQ%3D%3D; _cc_=U%2BGCWk%2F7og%3D%3D; mt=ci=55_1; whl=-1%260%261548680971793%261553075410013; JSESSIONID=8EDAE05EAB36153E3431C295774F5E44; uc1=cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&cookie21=UtASsssmeW6lpyd%2BBROh&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false&pas=0&cookie14=UoTZ502N5qYaMA%3D%3D&cart_m=0&tag=8&lng=zh_CN; isg=BJubqLrnQ7rhfbgzeQxpyidjKv_F2K4HhCA-T43YABqxbLpOFURlwoauBozHzAdq; l=bBrbcPXcvNtqGAM2BOCgquI8LF7tHIRfguPRwCcvi_5CZ1Ysj1QOlOKYwev6Vj5lOgLB4-L8Y1yt2U9_Js5..',
    'referer':'https://s.taobao.com/search?q=%E6%B8%B8%E6%88%8F%E4%B8%BB%E6%9C%BA&imgfile=&js=1&style=grid&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190325&ie=utf8'
}

print(requests.get(url=url,headers=headers).text)