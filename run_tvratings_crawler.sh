cd ~/Documents/dev/TVratings_crawling/
rm -rf tvratings_crawler/tvratings_crawler.csv
cd tvratings_crawler/
scrapy crawl tvratings_crawler -o tvratings_crawler.csv 

# How to crawl by specifying a datev (for example, December 6)
# - "scrapy crawl TVrating_Crawler -o tvrating_crawler.csv -a month=12 -a day=6"
