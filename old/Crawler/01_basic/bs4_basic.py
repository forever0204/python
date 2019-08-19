import urllib.request

from bs4 import BeautifulSoup

# html_doc='''
# <a href="javascript:;" hidefocus="true" data-action="prev" class="prv" title="上一首(ctrl+←)">上一首</a>
# <a href="javascript:;" hidefocus="true" data-action="play" class="ply j-flag" title="播放/暂停(p)">播放/暂停</a>
# <a href="javascript:;" hidefocus="true" data-action="next" class="nxt" title="下一首(ctrl+→)">下一首</a>
# </div>
# <div class="head j-flag"><img src="http://s4.music.126.net/style/web2/img/default/default_album.jpg"><a href="javascript:;" hidefocus="true" class="mask"></a></div>
# <div class="play">
# <div class="j-flag words"></div>
# <div class="m-pbar" data-action="noop">
# '''
url = 'https://list.jd.com/list.html?cat=1713,3287,3797&page=1&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main'
html_doc = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html_doc,'lxml')
# find = soup.find('a')
# find_all = soup.find_all('a')
# print(find_all)
# print("find's return type is ", type(find))  #输出返回值类型
# # print("find's content is", find)  #输出find获取的值
# # print("find's Tag Name is ", find.name)  #输出标签的名字
# # print("find's Attribute(class) is ", find['class'])  #输出标签的class属性值
# print(find.string)
div = soup.find('div')
print(div)
