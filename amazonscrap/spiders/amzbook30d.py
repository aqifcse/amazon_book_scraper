# -*- coding: utf-8 -*-
import scrapy

class Amzbook30dSpider(scrapy.Spider):
    name = 'amzbook30d'
    allowed_domains = ['https://www.amazon.com']

    base_url = 'https://www.amazon.com/Books-Last-30-days/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011'
    total_pages = 75

    def start_requests(self):
        
        url_list = []
        
        url_list.append(self.base_url)

        for i in range(2, self.total_pages):
            url_list.append(self.base_url + "&page=" + str(i))

        for url in url_list:
            yield scrapy.Request(url = url, callback = self.parse)


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
        