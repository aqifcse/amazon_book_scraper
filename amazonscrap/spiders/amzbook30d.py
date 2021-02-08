# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import Rule
from scrapy.linkextractors import LinkExtractor
#from amazonscrap.items import Amzbook30dItem

class Amzbook30dSpider(scrapy.Spider):
    name = 'amzbook30d'
    allowed_domains = ['https://www.amazon.com']

    start_urls = ['https://www.amazon.com/Books-Last-30-days/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011']

    def parse(self, response):
    
        books = response.xpath('//div[contains(@class, "s-include-content-margin s-border-bottom s-latency-cf-section")]')

        for book in books:
            
            title               = book.xpath('.//a[@class="a-link-normal a-text-normal"]/span/text()').extract_first()
            author              = book.xpath('.//a[@class="a-size-base a-link-normal"]/text()').extract_first()
            published_date      = book.xpath('.//span[@class="a-size-base a-color-secondary a-text-normal"]/text()').extract_first()
            rating              = book.xpath('.//a[@class="a-link-normal"]/span/text()').extract_first()
            hardcover_price_int = book.xpath('.//span[@class="a-price-whole"]/text()').extract_first()
            audible_status      = book.xpath('.//span[@class="a-color-secondary"]/text()').extract_first()

            yield {
                'title' :           title, 
                'author' :          author, 
                'published_date':   published_date, 
                'rating' :          rating, 
                'price' :           hardcover_price_int, 
                'status' :          audible_status, 
            }
        next_page = response.xpath('//li[@class="a-last"]/a/@href').extract_first()
        if next_page:
            next_page_url = 'https://www.amazon.com' + response.xpath('//li[@class="a-last"]/a/@href').extract_first() + '/index.html'
            self.start_urls.append(next_page_url)
            yield scrapy.Request(next_page_url, callback = self.parse)