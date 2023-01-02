# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
from contextlib import suppress

import pymongo
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from pcstock.settings import MONGO_COLLECTION, IMAGES_STORE

from PIL import Image

class ProductPipeline:

    collection_name = MONGO_COLLECTION

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db  = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db     = self.client[self.mongo_db]
    
    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        
        item.setdefault('rate', 0.0)

        if not self.db[self.collection_name].find_one(
            {
                "source": item["source"],
                "name": item["name"]
            }
        ):
            self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
        else:
            self.db[self.collection_name].update_one({"name": item["name"]}, {"$set": ItemAdapter(item).asdict()})

        return item

class ProductImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)
    
    def item_completed(self, results, item, info):
        with suppress(KeyError):
            ItemAdapter(item)[self.images_result_field] = [x for ok, x in results if ok]

            image_paths = [x['path'] for ok, x in results if ok]

            for img_path in image_paths:
                path = os.path.join(IMAGES_STORE, img_path)
                img = Image.open(path)
                img.thumbnail((75, 75), Image.ANTIALIAS)
                img.save(path)

            item['images'] = item['images'][0]['path'].split('/')[-1]

            return item