import urllib.request
import re
# urllib.request for opening and reading URLs
# urllib.error containing the exceptions raised by urllib.request
# urllib.parse for parsing URLs
# urllib.robotparser for parsing robots.txt files
url = "http://music.163.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         'Chrome/63.0.3239.108 Safari/537.36'}
def saveFile(data):
    path = 'D:\\Wendang\\crawler_get\\music.html'
    fp = open(path,'w',encoding='utf-8')
    fp.write(data)
    fp.close()
# 请求
# request = urllib.request.Request(url)
req = urllib.request.Request(url=url,headers=headers)
# 爬取结果
response = urllib.request.urlopen(req)
data = response.read()
# 设置解码方式
data = data.decode('utf-8')
# 打印结果
# print(data)
# saveFile(data)
# 将爬取下来的保存文件
# 打印爬取网页的各类信息
print(type(response))
print(response.geturl())
print(response.info())
print(response.getcode())

# 如何打印出我想要的标签页的内容？
# img标签页中的内容如何查看？
# for img, t in set(re.findall(r'<img(.*?)>', str(data))):
#     print(img)