from bs4 import BeautifulSoup

html = """
		    <table class="tablelist" cellpadding="0" cellspacing="0">
		    	<tr class="h">
		    		<td class="l" width="374">职位名称</td>
		    		<td>职位类别</td>
		    		<td>人数</td>
		    		<td>地点</td>
		    		<td>发布时间</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45398&keywords=&tid=87&lid=2218">22989-高级网络运维工程师</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2018-11-06</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45403&keywords=&tid=87&lid=2218">22989-AI应用后台开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2018-11-06</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45394&keywords=&tid=87&lid=2218">22989-腾讯云容器技术专家（深圳、北京）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2018-11-06</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45395&keywords=&tid=87&lid=2218">22989-运营产品中心web前端开发</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2018-11-06</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45387&keywords=&tid=87&lid=2218">25923-Web前端高级工程师（深圳）</a><span class="hot">&nbsp;</span></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-11-06</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45389&keywords=&tid=87&lid=2218">15570-手游后台高级工程师</a><span class="hot">&nbsp;</span></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-11-06</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45390&keywords=&tid=87&lid=2218">PCG04-WEB前端高级开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-11-06</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45391&keywords=&tid=87&lid=2218">PCG12-行业数据研发高级工程师</a><span class="hot">&nbsp;</span></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-11-06</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45382&keywords=&tid=87&lid=2218">SA-腾讯社交广告运维工程师(深圳)</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-11-06</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45374&keywords=&tid=87&lid=2218">23295-互娱iOS开发工程师（深圳）</a><span class="hot">&nbsp;</span></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-11-06</td>
		    	</tr>
		    			    	<tr class="f">
		    		<td colspan="5">
		    			<div class="left">共<span class="lightblue total">919</span>个职位</div>
		    			<div class="test"><div class="pagenav"><a href="javascript:;" class="test" id="test">上一页</a><a class="active" href="javascript:;">1</a><a href="position.php?lid=2218&tid=87&keywords=请输入关键词&start=10#a">2</a><a href="position.php?lid=2218&tid=87&keywords=请输入关键词&start=20#a">3</a><a href="position.php?lid=2218&tid=87&keywords=请输入关键词&start=30#a">4</a><a href="position.php?lid=2218&tid=87&keywords=请输入关键词&start=40#a">5</a><a href="position.php?lid=2218&tid=87&keywords=请输入关键词&start=50#a">6</a><a href="position.php?lid=2218&tid=87&keywords=请输入关键词&start=60#a">7</a><a href="position.php?lid=2218&tid=87&keywords=请输入关键词&start=70#a">...</a><a href="position.php?lid=2218&tid=87&keywords=请输入关键词&start=910#a">92</a><a href="position.php?lid=2218&tid=87&keywords=请输入关键词&start=10#a" id="next">下一页</a><div class="clr"></div></div></div>
		    			<div class="clr"></div> 
		    		</td>
		    	</tr>
		    </table>


"""


"""
1. 获取所有tr标签 
2. 获取第2个tr标签
3. 获取所有class等于even的标签
4. 获取所有a标签的href属性,id = test 同时 class = test
5. 获取所有的职位信息(纯文本)
6. 获取所有a标签的href属性值
"""

soup = BeautifulSoup(html,'lxml')

# #1. 获取所有tr标签
trs = soup.find_all('tr')
for tr in trs:
    print(tr)
    print("="*30)

# 2. 获取第2个tr标签 limit最多获取多少元素
# tr2 = soup.find_all('tr',limit=2)[1]
# print(tr2)


# 3. 获取所有class等于even的标签 使用 class_
# trs = soup.find_all('tr',class_='even')
# print(trs)
# trs = soup.find_all('tr',attrs={'class':'even'})
# print(trs)

# 4. 获取所有a标签的href属性,id = test 同时 class = test
# aList = soup.find_all('a',id='test',class_='test')
# for a in aList:
#     print(a)

# 6. 获取所有a标签的href属性值
# aList = soup.find_all('a')
# for a in aList:
#     href = a['href']
#     print(href)

# 5.获取所有的职位信息(纯文本)
# tds = soup.find_all('td',class_='l square')
# for td in tds:
#     aText = td.find_all('a')
#     print(aText[0].string)
trs = soup.find_all('tr')[1:]
movies = []
for tr in trs:
    movie = {}
    # .stripped_strings 获取元素中所有非空白字符

    infos = tr.stripped_strings
    infoList = list(infos)
    movie['职位'] = infoList[0]
    movie['类型'] = infoList[1]
    movie['人数'] = infoList[2]
    movie['地点'] = infoList[3]
    movie['时间'] = infoList[4]
    movies.append(movie)

print(movies)