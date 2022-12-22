# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class ProductPipeline:
    def open_spider(self, spider):
        self.file = open('data.jsonl', 'w')
    
    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        
        item.setdefault('rate', 0.0)

        line = json.dumps(ItemAdapter(item).asdict()) + '\n'
        self.file.write(line)
        return item
