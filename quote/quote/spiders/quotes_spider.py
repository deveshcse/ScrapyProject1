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
        all_div_quotes = response.css('div.quote')[0]
        title = all_div_quotes.css('span.text::text').extract()
        author = all_div_quotes.css('.author::text').extract()
        tag = all_div_quotes.css('.tags::text').extract()
        yield {
            'title': title,
            'author': author,
            'tag': tag
        }
        
