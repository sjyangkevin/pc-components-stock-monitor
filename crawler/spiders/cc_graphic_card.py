import scrapy

class CCGraphicCardSpider(scrapy.Spider):
    name = "cc_graphic_card"

    def start_requests(self):
    
        page_num = 1
        max_page = 20

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
        
        item_name = response.xpath(
            '//h1[contains(@class, "h3")]/strong/text()'
        ).get()

        item_link = response.url

        item_rate = response.xpath(
            '//div[contains(@class, "row")]/span[contains(@class, "h3")]/text()'
        ).extract_first('not available')
        
        item_price = response.xpath(
            '//div[contains(@class, "price-show-panel")]//span[contains(@class, "h2-big")]/strong/text()'
        ).get()
        
        stock_detail = {
            "ONLINE": response.xpath(
                '//div[contains(@id, "stock_detail")]/div[@id = "prov-ONLINE"]//div[contains(@class, "item-stock")]/p/span/strong/text()'
            ).extract_first('0').replace('-', '0'),
            "ON": self.calculate_stock_availability(
                response.xpath(
                    '//div[contains(@id, "stock_detail")]/div[@id = "prov-{0}"]/div[contains(@class, "item__avail__num {0}")]/div/div[contains(@class, "col-3")]/div[@class = "item-stock"]/p/span[@class = "stocknumber"]/strong/text()'.format("ON")
                ).getall()
            ),
            "QC": self.calculate_stock_availability(
                response.xpath(
                    '//div[contains(@id, "stock_detail")]/div[@id = "prov-{0}"]/div[contains(@class, "item__avail__num {0}")]/div/div[contains(@class, "col-3")]/div[@class = "item-stock"]/p/span[@class = "stocknumber"]/strong/text()'.format("QC")
            ).getall()
            ),
            "NS": self.calculate_stock_availability(
                response.xpath(
                    '//div[contains(@id, "stock_detail")]/div[@id = "prov-{0}"]/div[contains(@class, "item__avail__num {0}")]/div/div[contains(@class, "col-3")]/div[@class = "item-stock"]/p/span[@class = "stocknumber"]/strong/text()'.format("NS")
            ).getall()
            ),
            "BC": self.calculate_stock_availability(
                response.xpath(
                    '//div[contains(@id, "stock_detail")]/div[@id = "prov-{0}"]/div[contains(@class, "item__avail__num {0}")]/div/div[contains(@class, "col-3")]/div[@class = "item-stock"]/p/span[@class = "stocknumber"]/strong/text()'.format("BC")
            ).getall()
            )
        }

        yield {
            "item_name": item_name,
            "item_link": item_link,
            "item_rate": item_rate,
            "item_price": item_price,
            "stock_detail": stock_detail
        }
    
    def calculate_stock_availability(self, availability_list):
        
        if len(availability_list) == 0:
            return "0"

        more_than = False
        amount    = 0

        for num in availability_list:
            if num == "10+":
                more_than = True
                amount += 10
            else:
                amount += int(num)
        
        if more_than:
            return str(amount) + "+"
        
        return str(amount)


        






