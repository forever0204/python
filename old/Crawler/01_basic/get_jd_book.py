'''
爬取京东的编程类图书
'''
import urllib.request
import urllib.parse

import requests
from bs4 import BeautifulSoup
import os
targetPath = "D:\Tupian\crawler_get\jd_book"




# def get_book(url):
for i in range(100):
    url = 'https://list.jd.com/list.html?cat=1713,3287,3797&page='+str(i)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                             'Chrome/63.0.3239.108 Safari/537.36'}
    # 浏览器头
    html = urllib.request.urlopen(url).read()
    # 读取到的html页面
    html = str(html,encoding='utf-8')
    # print(html)
    # fp = open('D:\Wendang\crawler\jd.html','w',encoding='utf-8')
    # fp.write(BeautifulSoup(html).prettify())
    # //*[@id="plist"]#plist
    all_book = BeautifulSoup(html, 'lxml').find(id='plist').find_all('li')
    # print(BeautifulSoup(html).prettify())
    # id 为plist中的所有li
    #大图 https://img13.360buyimg.com/shaidan/jfs/t6130/167/771989293/235186/608d0264/592bf167Naf49f7f6.jpg
    #小图       //img13.360buyimg.com/ n7    /jfs/t6130/167/771989293/235186/608d0264/592bf167Naf49f7f6.jpg
    for book in all_book:
        try:
            img = book.find('a').find('img')
            # img = img.replace('data-lazy-img','src')
            # print(type(img))# img的类型
            # print(img.attrs)# img中所有属性的字典
            # print('src' in img.attrs)
            if 'src' in img.attrs:
                book_img_small = 'http:'+img['src']
            else:
                book_img_small = 'http:'+img['data-lazy-img']
            # {'data-img': '1', 'height': '200', 'width': '200',
            #  'src': '//img12.360buyimg.com/n7/jfs/t2851/14/1309443716/77855/47617a5e/573ab66eNe797b873.jpg'}
            # {'data-img': '1', 'height': '200', 'width': '200',
            #  'data-lazy-img': '//img13.360buyimg.com/n7/jfs/t3214/126/2309313357/292133/6c038027/57e09a03Nc57334e1.jpg'}

            print(book_img_small)
            image = requests.get(book_img_small)
            # image = urllib.request.urlretrieve(book_img_small)
            file_name=book_img_small[-15:len(book_img_small)]
            print('开始保存图片')
            f = open(targetPath + '\\' + file_name, 'ab')
            f.write(image.content)
            print(file_name, '图片保存成功！')
            f.close()
            # if img['data-lazy-img']:
            #     print(img['data-lazy-img'])
            # if img['data-lazy-img']:
            #     print('11')
            # print(img['data-lazy-img'])
            # book_img_small =img['src']
            # book_img_lazy  = img['data-lazy-img']
            # print(book_img_small)
            # print(book.find('a'))#['data-lazy-img'])
            # print(book_img_lazy)
            # book_info = book.find('a')['em']
            # book_img = book_img_small.replace('/n7/','/shaidan/')
            # print(book_img)
            # print(book_info)
        except KeyError:
            print('error')
        # print(len(all_book))
    # if __name__ == '__main__':
    #
    #     get_book(url)