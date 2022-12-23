from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from pcstock.spiders.cc_graphic_card import CCGraphicCardSpider
# from pcstock.spiders.bb_graphic_card import BBGraphicCardSpider
from pcstock.spiders.ne_graphic_card import NEGraphicCardSpider

process = CrawlerProcess(get_project_settings())
process.crawl(CCGraphicCardSpider)
# process.crawl(BBGraphicCardSpider)
process.crawl(NEGraphicCardSpider)
process.start()
