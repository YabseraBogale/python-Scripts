import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quote-spdier'
    start_urls = ['http://debank.com/profile/0x0c1a3e4e1c3da4c89582dfa1afa87a1853d7f78f/history?chain=metis']
    def parse(self, response):
        QUOTE_SELECTOR = '.History_table__9zhFG'
        TEXT_SELECTOR = '.text::text'
        AUTHOR_SELECTOR = '.author::text'
        
        for quote in response.css(QUOTE_SELECTOR):
            yield {
                'text': quote.css(TEXT_SELECTOR).extract_first(),
                'author': quote.css(AUTHOR_SELECTOR).extract_first(),
            }