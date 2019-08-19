from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os

class AlbumCover():

    def __init__(self):
        self.init_url = "http://music.163.com/#/artist/album?id=3684&limit=120&offset=0" #请求网址
        self.folder_path = 'D:/Wendang/crawler_get/jj' #想要存放的文件目录

    def save_img(self, url, file_name):  ##保存图片
        print('开始请求图片地址，过程会有点长...')
        img = self.request(url)
        print('开始保存图片')
        f = open(file_name, 'ab')
        f.write(img.content)
        print(file_name, '图片保存成功！')
        f.close()

    def request(self, url):  # 封装的requests 请求
        r = requests.get(url)  # 像目标url地址发送get请求，返回一个response对象。有没有headers参数都可以。
        return r

    def mkdir(self, path):  ##这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print('创建名字叫做', path, '的文件夹')
            os.makedirs(path)
            print('创建成功！')
            return True
        else:
            print(path, '文件夹已经存在了，不再创建')
            return False

    def get_files(self, path):  # 获取文件夹中的文件名称列表
        pic_names = os.listdir(path)
        return pic_names

    def spider(self):
        print("Start!")
        driver = webdriver.PhantomJS("C:\\Program Files\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
        driver.get(self.init_url)
        driver.switch_to.frame("g_iframe")
        html = driver.page_source

        self.mkdir(self.folder_path)  # 创建文件夹
        print('开始切换文件夹')
        os.chdir(self.folder_path)  # 切换路径至上面创建的文件夹

        file_names = self.get_files(self.folder_path)  # 获取文件夹中的所有文件名，类型是list

        all_li = BeautifulSoup(html, 'lxml').find(id='m-song-module').find_all('li')
        # all_li = BeautifulSoup(html, 'lxml').find(id='discover-module').find_all('div')

        # print(type(all_li))

        for li in all_li:
            album_img = li.find('img')['src']
            album_name = li.find('p', class_='dec')['title']
            album_date = li.find('span', class_='s-fc3').get_text()
            # album_img = li.find('img')['src']
            # album_name = li.find('a',class_='msk')['title']
            # album_date  ='20171228'
            end_pos = album_img.index('?')
            album_img_url = album_img[:end_pos]

            photo_name = album_date + '-' + album_name.replace('/', '').replace(':', ',').replace(' ','')[0:30] + '.jpg'
            print(album_img_url, photo_name)

            if photo_name in file_names:
                print('图片已经存在，不再重新下载')
            else:
                try:
                    self.save_img(album_img_url,photo_name)
                except os.error as e:
                    print('error %d %s' % (e.args[0], e.args[1]))

album_cover = AlbumCover()
album_cover.spider()