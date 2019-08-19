import requests
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS("C:\\Program Files\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
web_url = 'https://unsplash.com'  #要访问的网页地址
folder_path = 'D:/Wendang/crawler_get'
driver.get(web_url)
all_a = BeautifulSoup(driver.page_source, 'lxml').find_all('a', title='Download photo')
# [<a class="_37zTg _1l4Hh _1CBrG _1zIyn xLon9 _1Tfeo" download="" href="https://unsplash.com/photos/RWAIyGmgHTQ/download?force=true" rel="nofollow" target="_blank" title="Download photo"><span><svg aria-hidden="false" class="Apljk _11dQc _1Jd5C" height="32" version="1.1" viewbox="0 0 32 32" width="32"><path d="M25.8 15.5l-7.8 7.2v-20.7h-4v20.7l-7.8-7.2-2.7 3 12.5 11.4 12.5-11.4z"></path></svg><span class="_2Aga-">Download</span></span></a>
# 提取里面的herf，下载大图
for href in all_a:
    img_url=href['href']
    print(img_url)
    img = requests.get(img_url)
    img_name = str(img_url)[28:39] + '.jpg'
    # print(file_name)
    f = open(folder_path+'//'+img_name, 'ab')
    f.write(img.content)
    print(img_name, '图片保存成功！')
    f.close()
# print(all_a)
