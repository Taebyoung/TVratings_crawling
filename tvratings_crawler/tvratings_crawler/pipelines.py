from .mongodb import collection

class TVratings_Pipeline(object):
    
    def process_item(self, item, spider):
        
        data = {"genre": item["genre"], 
                "rank": item["rank"],  
                "channel": item["channel"], 
                "program": item["program"], 
                "rate": item["rate"], 
               }
        
        collection.insert(data)
        
        return item
