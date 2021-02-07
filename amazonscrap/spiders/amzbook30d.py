# -*- coding: utf-8 -*-
import scrapy
from amazonscrap.items import Amzbook30dItem

class Amzbook30dSpider(scrapy.Spider):
    name = 'amzbook30d'
    allowed_domains = ['https://www.amazon.com/']

    start_urls = ['https://www.amazon.com/Books-Last-30-days/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011']

    # def parse(self, response):
    #     all_pages = int(response.xpath('.//li[contains(@class, "a-disabled")]/text()').extract()[2])
    #     print (all_pages)
    #     for page in all_pages:

    #     next_page_url = response.xpath('.//li[contains(@class, "a-last")]/a/@href').extract_first()
    #     next_page_url = 'https://www.amazon.com' + next_page_url
    #     print(next_page_url)

    def parse(self, response):
        item = Amzbook30dItem()
    
        books = response.xpath('//div[contains(@class, "s-include-content-margin s-border-bottom s-latency-cf-section")]')
        
        for book in books:
            
            item['book_name'] = book.xpath('.//a[@class="a-link-normal a-text-normal"]/span/text()').extract_first()
            item['book_author'] = book.xpath('.//a[@class="a-size-base a-link-normal"]/text()').extract_first()
            item['book_published_date'] = book.xpath('.//span[@class="a-size-base a-color-secondary a-text-normal"]/text()').extract_first()
            item['book_rating'] = book.xpath('.//a[@class="a-link-normal"]/span/text()').extract_first()
            item['book_hardcover_price_int'] = book.xpath('.//span[@class="a-price-whole"]/text()').extract_first()
            item['book_audible_status'] = book.xpath('.//span[@class="a-color-secondary"]/text()').extract_first()

            yield item
        
        # next_page = response.xpath('//li[contains(@class, "a-last")]/a/@href').extract_first()
        # next_page = 'https://www.amazon.com' + next_page

        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     print(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)
