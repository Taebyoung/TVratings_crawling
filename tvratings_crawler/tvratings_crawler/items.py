
import scrapy


class TvratingsCrawlerItem(scrapy.Item):
    genre = scrapy.Field()      # Genre: types of TV programs (General, Drama, Entertainment)
    rank = scrapy.Field()       # rank: top 20 rank
    program = scrapy.Field()    # program: name of TV program
    channel = scrapy.Field()    # channel: name of broadcast channel
    rate = scrapy.Field()       # rate: TV Ratings
    pass
