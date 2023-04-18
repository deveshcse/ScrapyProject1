import scrapy
from scrapy.spiders import Spider
from ..items import QuoteItem


class QuoteSpyder(Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
        items = QuoteItem()

        all_div_quotes = response.css('div.quote')
        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items
        next_page = response.css('li.next a::attr(href)').get()
        print(next_page)
        if next_page is not None:

            yield response.follow(next_page, callback=self.parse)

        
