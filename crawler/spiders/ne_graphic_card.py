import scrapy

class NEGraphicCardSpider(scrapy.Spider):
    name = "ne_graphic_card"

    def start_requests(self):
        page_num = 1
        max_page = 100

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
        
        item_name = response.xpath(
            '//div[@class = "product-wrap"]/h1[@class = "product-title"]/text()'
        ).get()

        item_link = response.url

        item_rate = response.xpath(
            '//div[@class = "product-rating"]/i[contains(@class, "rating")]/@title'
        ).get().split(' ')[0]

        item_price_comb = response.xpath(
            '//div[@class = "product-price"]//li[@class = "price-current"]'
        )

        item_price = \
            '$' + \
            item_price_comb.xpath('strong/text()').get() + \
            item_price_comb.xpath('sup/text()').get()

        stock_detail = {
            "ONLINE": response.xpath('//div[@class = "product-inventory"]/strong/text()').get()
        }

        yield {
            "item_name": item_name,
            "item_link": item_link,
            "item_rate": item_rate,
            "item_price": item_price,
            "stock_detail": stock_detail
        }