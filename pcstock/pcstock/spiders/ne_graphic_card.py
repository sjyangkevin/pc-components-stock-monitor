from datetime import datetime

import scrapy
from pcstock.items import Product
from scrapy.loader import ItemLoader

class NEGraphicCardSpider(scrapy.Spider):
    name = "ne_graphic_card"

    def start_requests(self):
        page_num = 1
        max_page = 1

        while page_num <= max_page:
            yield scrapy.Request(
                url="https://www.newegg.ca/GPUs-Video-Graphics-Cards/SubCategory/ID-48/Page-{0}?Tid=7708".format(page_num),
                callback=self.parse
            )

            page_num += 1

    def parse(self, response, **kwargs):
        item_detail_pages = response.xpath(
            '//div[contains(@class, "item-info")]/a[@class = "item-title"]/@href'
        ).getall()

        for page in item_detail_pages:
            if page is not None:
                next_page = response.urljoin(page)
                yield scrapy.Request(url=next_page, callback=self.parse_item_detail)
    
    def parse_item_detail(self, response, **kwargs):

        rate = response.xpath(
            '//div[@class = "product-rating"]/i[contains(@class, "rating")]/@title'
        ).get().split(' ')[0]

        item_price_comb = response.xpath(
            '//div[@class = "product-price"]//li[@class = "price-current"]'
        )

        price = \
            item_price_comb.xpath('strong/text()').get() + \
            item_price_comb.xpath('sup/text()').get()
        
        loader = ItemLoader(item=Product(), selector=response)

        loader.add_value(
            'source',
            'newegg'
        )
        loader.add_value(
            'type',
            'GPU'
        )
        loader.add_xpath(
            'name',
            '//div[@class = "product-wrap"]/h1[@class = "product-title"]'
        )
        loader.add_value(
            'link',
            response.url
        )
        loader.add_value('rate', rate)
        loader.add_value('price', price)
        loader.add_value(
            'online_stock',
            self.get_inventory(
                response.xpath('//div[@class = "product-inventory"]/strong/text()').get()
            )
        )
        loader.add_value('on_stock', 'No Information')
        loader.add_value('bc_stock', 'No Information')
        loader.add_value('qc_stock', 'No Information')
        loader.add_value('ns_stock', 'No Information')
        loader.add_value(
            'last_updated',
            datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        )

        yield loader.load_item()
    
    def get_inventory(self, inventory):
        return 'Available' if inventory == 'In stock.' else 'Not Available'