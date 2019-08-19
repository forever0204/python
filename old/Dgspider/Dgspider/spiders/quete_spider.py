import  scrapy
class QuotesSpider(scrapy.Spider):
    '''name 爬虫名称，同一个项目中不能有重复名称的spider。
start_url 起始url列表，执行后每个url会返回一个Response对象
parse()调用的时候传入从每一个 URL 传回的 Response 对象作为参数，负责解析并匹配抓取的数据(解析为 item)，跟踪更多的 URL。
'''

    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
            'http://blog.csdn.net/qq_31573519/article/details/71107162'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)