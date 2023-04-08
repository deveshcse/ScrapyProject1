import scrapy
from scrapy.spiders import Spider

class QuoteSpyder(Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
        # title = response.css('title::text').extract()
        # yield {'titletext': title}
        
