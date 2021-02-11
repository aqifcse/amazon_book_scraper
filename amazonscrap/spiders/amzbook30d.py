# page-by-page
# -*- coding: utf-8 -*-
import scrapy

class Amzbook30dSpider(scrapy.Spider):
    name = 'amzbook30d'
    allowed_domains = ['https://www.amazon.com']

    #base_url = 'https://www.amazon.com/Books-Last-30-days/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011'

    def start_requests(self):

        url_list = [f'https://www.amazon.com/Books-Last-30-days/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011&page={i}' for i in range(0, 75)]

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



# book-by-book
# import scrapy

# class Amzbook30dSpider(scrapy.Spider):
#     name = 'amzbook30d'
#     allowed_domains = ['amazon.com']
#     start_urls = ['https://www.amazon.com/Books-Last-30-days/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011/']     # '/' must me included :(
#     base_url = 'https://www.amazon.com/Books-Last-30-days/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011/'         # '/' must be included  :(
    
#     def parse(self, response):
#         all_books = response.xpath('//div[@class="s-include-content-margin s-border-bottom s-latency-cf-section"]')

#         for book in all_books:
#             book_url = book.xpath('.//h2/a/@href').extract_first()
#             yield scrapy.Request(url = response.urljoin(book_url), callback=self.parse_book)
        

#         next_page_partial_url = response.xpath('//li[@class="a-last"]/a/@href').extract_first()
#         if next_page_partial_url:
#             next_page_url = response.urljoin(next_page_partial_url)

#             yield scrapy.Request(url = next_page_url, callback = self.parse)

#         else: print("I am Done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    
        
#     def parse_book(self, response):

#         title               = response.xpath('//h1[@class="a-spacing-none a-text-normal"]/span/text()').extract_first()
#         author              = response.xpath('//a[@class="a-link-normal contributorNameID"]/text()').extract_first()
#         published_date      = response.xpath('//span[@class="a-size-large a-color-secondary"]/text()').extract_first()
#         rating              = response.xpath('//span[@class="acrCustomerReviewText"]/text()').extract_first()
#         hardcover_price_int = response.xpath('//span[@class="a-size-base a-color-price a-color-price"]/text()').extract_first()
#         audible_status      = response.xpath('//span[@class="a-size-medium a-color-success"]/text()').extract_first()

#         yield {
#             'title' :           title, 
#             'author' :          author, 
#             'published_date':   published_date, 
#             'rating' :          rating, 
#             'price' :           hardcover_price_int, 
#             'status' :          audible_status, 
#         }
        