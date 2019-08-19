'''''
批量下载云音乐首页的图片

采用伪装浏览器的方式爬取豆瓣网站首页的图片，保存到指定路径文件夹下
'''

# 导入所需的库
import urllib.request, socket, re, sys, os

# 定义文件保存路径
targetPath = "D:\Tupian\crawler_get"


def saveFile(path):
    # 检测当前路径的有效性
    if not os.path.isdir(targetPath):
        os.mkdir(targetPath)
        # 设置每个图片的路径
    pos = path.rindex('/')
    t = os.path.join(targetPath, path[pos + 1:])
    return t


# 用if __name__ == '__main__'来判断是否是在直接运行该.py文件


# 网址
# url = "http://music.163.com/"
# 网易云音乐链接
url = 'https://www.douban.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         'Chrome/63.0.3239.108 Safari/537.36'}

req = urllib.request.Request(url=url, headers=headers)

res = urllib.request.urlopen(req)

data = res.read()

# <img class="d-flag" src="http://p1.music.126.net/bnA1sVK3VXT-A5ZWonjOLw==/18875316114537699.jpg"
# id="auto-id-qrmOei6EESwF6eMJ" style="transition: none; opacity: 1;">
for link, t in set(re.findall(r'(http?://[\w./]+\.(jpg|gif|png))', str(data))):

    print(link)
    try:
        urllib.request.urlretrieve(link, saveFile(link))
    except:
        print('失败')