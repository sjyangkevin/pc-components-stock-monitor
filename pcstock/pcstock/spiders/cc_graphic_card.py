from datetime import datetime

import scrapy
from pcstock.items import Product
from scrapy.loader import ItemLoader

class CCGraphicCardSpider(scrapy.Spider):
    name = "cc_graphic_card"
    
    def start_requests(self):
    
        page_num = 1
        max_page = 2

        while page_num < max_page:
            yield scrapy.Request(
                url="https://www.canadacomputers.com/index.php?cPath=43_557&ajax=true&page=" + str(page_num),
                callback=self.parse
            )

            page_num += 1
    
    def parse(self, response, **kwargs):
        item_detail_pages = response.xpath(
            '//div[contains(@class, "productInfoSearch")]/span[contains(@class, "productTemplate_title")]/a/@href'
        ).getall()

        for page in item_detail_pages:
            if page is not None:
                next_page = response.urljoin(page)
                yield scrapy.Request(next_page, callback=self.parse_item_detail)

    def parse_item_detail(self, response, **kwargs):

        online_stock = response.xpath(
            '//div[contains(@id, "stock_detail")]/div[@id = "prov-ONLINE"]//div[contains(@class, "item-stock")]/p/span/strong/text()'
        ).extract_first('0').replace('-', '0')

        on_stock = self.get_inventory(
            response.xpath(
                '//div[contains(@id, "stock_detail")]/div[@id = "prov-{province}"]/div[contains(@class, "item__avail__num {province}")]/div/div[contains(@class, "col-3")]/div[@class = "item-stock"]/p/span[@class = "stocknumber"]/strong/text()'.format(province="ON")
            ).getall()
        )

        bc_stock = self.get_inventory(
            response.xpath(
                '//div[contains(@id, "stock_detail")]/div[@id = "prov-{province}"]/div[contains(@class, "item__avail__num {province}")]/div/div[contains(@class, "col-3")]/div[@class = "item-stock"]/p/span[@class = "stocknumber"]/strong/text()'.format(province="BC")
            ).getall()
        )

        qc_stock = self.get_inventory(
            response.xpath(
                '//div[contains(@id, "stock_detail")]/div[@id = "prov-{province}"]/div[contains(@class, "item__avail__num {province}")]/div/div[contains(@class, "col-3")]/div[@class = "item-stock"]/p/span[@class = "stocknumber"]/strong/text()'.format(province="QC")
            ).getall()
        )

        ns_stock = self.get_inventory(
            response.xpath(
                '//div[contains(@id, "stock_detail")]/div[@id = "prov-{province}"]/div[contains(@class, "item__avail__num {province}")]/div/div[contains(@class, "col-3")]/div[@class = "item-stock"]/p/span[@class = "stocknumber"]/strong/text()'.format(province="NS")
            ).getall()
        )

        loader = ItemLoader(item=Product(), selector=response)
        
        loader.add_value(
            'source',
            'canadacomputers'
        )
        loader.add_value(
            'type',
            'GPU'
        )
        loader.add_value(
            'image_urls',
            [response.xpath('//div[@class = "img-container"]/img[contains(@src, "75x75")]/@src').extract_first()]
        )
        loader.add_xpath(
            'name', 
            '//h1[contains(@class, "h3")]/strong'
        )
        loader.add_value(
            'link',
            response.url
        )
        loader.add_xpath(
            'rate',
            '//div[contains(@class, "row")]/span[contains(@class, "h3")]/text()'
        )
        loader.add_xpath(
            'price',
            '//div[contains(@class, "price-show-panel")]//span[contains(@class, "h2-big")]/strong/text()'
        )
        loader.add_value('online_stock', 'Available' if online_stock != '0' else 'Not Available')
        loader.add_value('on_stock', on_stock)
        loader.add_value('bc_stock', bc_stock)
        loader.add_value('qc_stock', qc_stock)
        loader.add_value('ns_stock', ns_stock)
        loader.add_value(
            'last_updated',
            datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        )

        yield loader.load_item()
    
    def get_inventory(self, inventory):
        
        if len(inventory) > 0:
            return 'Available'
        else:
            return 'Not Available'


        






