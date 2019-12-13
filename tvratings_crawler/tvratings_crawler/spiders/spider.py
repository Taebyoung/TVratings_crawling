import scrapy
from tvratings_crawler.items import TvratingsCrawlerItem
from datetime import date, timedelta

class Spider(scrapy.Spider):

    name = "TVratings_Crawler"
    allow_domain = ["https://search.naver.com/"]
    
    def __init__(self, month=12, day=1, **kwargs):
        self.month=month        # Use when specifying a date
        self.day=day            # Use when specifying a date
        today = date.today()
        yesterday = date.today() - timedelta(1)
        self.month=yesterday.strftime('%m')
        self.day=yesterday.strftime('%d')  # If no date is specified, it is used as yesterday's date
        super().__init__(**kwargs)
  
    def start_requests(self, **kwargs):
        month = self.month
        day = self.day.zfill(2)
        urls = [
        "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=blUw&query={}%EC%9B%94{}%EC%9D%BC%20%EC%A2%85%ED%95%A9%20%EC%8B%9C%EC%B2%AD%EB%A5%A0".format(month, day),
        "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=blUw&query={}%EC%9B%94{}%EC%9D%BC%20%EB%93%9C%EB%9D%BC%EB%A7%88%20%EC%8B%9C%EC%B2%AD%EB%A5%A0".format(month, day),
        "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=blUw&query={}%EC%9B%94{}%EC%9D%BC%20%EC%98%88%EB%8A%A5%20%EC%8B%9C%EC%B2%AD%EB%A5%A0".format(month, day),
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for i in range(1, 21):
            genre = response.xpath('//*[@id="main_pack"]/div[1]/div/div[2]/div/h4/text()').extract()
            rank = response.xpath('//*[@id="main_pack"]/div[1]/div/div[2]/div/div[3]/div/table/tbody/tr[{}]/td[1]/p/span/span/text()'.format(i)).extract()
            program = response.xpath('//*[@id="main_pack"]/div[1]/div/div[2]/div/div[3]/div/table/tbody/tr[{}]/td[2]/p/a/text()'.format(i)).extract()
            channel = response.xpath('//*[@id="main_pack"]/div[1]/div/div[2]/div/div[3]/div/table/tbody/tr[{}]/td[3]/p/a/text()'.format(i)).extract()
            rate = response.xpath('//*[@id="main_pack"]/div[1]/div/div[2]/div/div[3]/div/table/tbody/tr[{}]/td[4]/p/text()'.format(i)).extract()
            
            item = TvratingsCrawlerItem()
            item["genre"] = genre
            item["rank"] = rank
            item["program"] = program
            item["channel"] = channel
            item["rate"] = rate
            yield item
