import pymongo

client = pymongo.MongoClient('mongodb://15.164.198.126:27017/')  # MongoDB IP Address 
db = client.tvrating_crawler
collection = db.tvrating
