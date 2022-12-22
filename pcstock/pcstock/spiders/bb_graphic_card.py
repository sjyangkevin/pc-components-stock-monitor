from datetime import datetime

import scrapy
import urllib.parse
from pcstock.items import Product
from scrapy.loader import ItemLoader

class BBGraphicCardSpider(scrapy.Spider):
    name = "bb_graphic_card"

    def start_requests(self):
        
        page_num = 1
        max_page = 1

        while page_num <= max_page:
            yield scrapy.Request(
                url="https://www.bestbuy.ca/api/v2/json/search?categoryid=20397&currentRegion=QC&include=facets, redirects&lang=en-CA&page={page}&pageSize=24&path=&query=&exp=labels,search_abtesting_5050_conversion:b&sortBy=relevance&sortDir=desc".format(page=page_num),
                callback=self.parse
            )

            page_num += 1

    def parse(self, response, **kwargs):
        
        response_json = response.json()

        url_domain   = '{uri.scheme}://{uri.netloc}/'.format(uri=urllib.parse.urlparse(response.url))

        product_list = response_json.get('products')

        for product in product_list:

            item_name    : str = product.get('name')
            item_rate    : int = product.get('customerRating')
            item_price   : float = product.get('salePrice') if product.get('salePrice') is not None else product.get('regularPrice')

            next_page    : str = urllib.parse.urljoin(url_domain, product.get('productUrl'))
            
            if next_page is not None:
                yield scrapy.Request(
                    url=next_page,
                    callback=self.parse_item_detail,
                    meta={
                        "name": item_name,
                        "rate": item_rate,
                        "price": item_price
                    }
                )

    def parse_item_detail(self, response, **kwargs):

        loader = ItemLoader(item=Product(), selector=response)

        loader.add_value(
            'source',
            'bestbuy'
        )
        loader.add_value(
            'type',
            'GPU'
        )
        loader.add_value('name', response.meta.get('name'))
        loader.add_value('link', response.url)
        loader.add_value('rate', response.meta.get('rate'))
        loader.add_value('price', response.meta.get('price'))
        loader.add_value(
            'online_stock',
            self.get_inventory(
                response.xpath('//span[contains(@class, "availabilityMessage_3ZSBM")]/text()').get()
            )
        )
        loader.add_value('on_stock', 'Not Available')
        loader.add_value('bc_stock', 'Not Available')
        loader.add_value('qc_stock', 'Not Available')
        loader.add_value('ns_stock', 'Not Available')
        loader.add_value(
            'last_updated',
            datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        )

        yield loader.load_item()
    
    def get_inventory(self, inventory):
        return 'Not Available' if inventory == 'Sold out online' else 'Available'