# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field

from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

from pcstock.utils import parse_currency, parse_rating

class Product(scrapy.Item):
    
    source = Field(
        output_processor=TakeFirst()
    )

    type = Field(
        output_processor=TakeFirst()
    )

    image_urls = scrapy.Field()

    images = scrapy.Field()

    name = Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst()
    )
    link = Field(
        output_processor=TakeFirst()
    )
    rate = Field(
        input_processor=MapCompose(parse_rating),
        output_processor=TakeFirst()
    )
    price = Field(
        input_processor=MapCompose(parse_currency),
        output_processor=TakeFirst()
    )
    online_stock = Field(
        output_processor=TakeFirst()
    )
    on_stock = Field(
        output_processor=TakeFirst()
    )
    bc_stock = Field(
        output_processor=TakeFirst()
    )
    qc_stock = Field(
        output_processor=TakeFirst()
    )
    ns_stock = Field(
        output_processor=TakeFirst()
    )

    last_updated = Field(
        output_processor=TakeFirst()
    )
