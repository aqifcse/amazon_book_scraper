# -*- coding: utf-8 -*-
import scrapy
from amazonscrap.items import AmazonItem

class AmazonProductSpider(scrapy.Spider):
  name = "AmazonDeals"
  allowed_domains = ["amazon.com"]
  
  #Use working product URL below
  start_urls = [
     "http://www.amazon.com/dp/B0046UR4F4", "http://www.amazon.com/dp/B00JGTVU5A",
     "http://www.amazon.com/dp/B00O9A48N2", "http://www.amazon.com/dp/B00UZKG8QU",
     "https://www.amazon.com/Ambitious-Girl-Meena-Harris/dp/0316229695/ref=sr_1_2?dchild=1&qid=1612351002&refinements=p_n_publication_date%3A1250226011&s=books&sr=1-2",
     ]
 
  def parse(self, response):
    items = AmazonItem()
    title = response.xpath('//h1[@id="title"]/span/text()').extract()
    sale_price = response.xpath('//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()').extract()
    category = response.xpath('//a[@class="a-link-normal a-color-tertiary"]/text()').extract()
    availability = response.xpath('//div[@id="availability"]//text()').extract()
    items['product_name'] = ''.join(title).strip()
    items['product_sale_price'] = ''.join(sale_price).strip()
    items['product_category'] = ','.join(map(lambda x: x.strip(), category)).strip()
    items['product_availability'] = ''.join(availability).strip()
    yield items


# import scrapy
# from scrapy.exceptions import CloseSpider
# from scrapy.spider import BaseSpider
# from scrapy.http import Request
# from jabong.items import product

# class spider(BaseSpider):
#     name = "jabong"
#     allowed_domains = ["jabong.com"]
#     start_urls = [
#     "http://www.jabong.com/women/clothing/tops-tees-shirts/tops/?page=1&limit=52&sortField=popularity&sortBy=desc",
# ]
#     page = 1

#     def parse(self, response):
#         products = response.xpath('//*[@id="catalog-product"]/section[2]/div')
#         if not products:
#             raise CloseSpider("No more products!")

#         for p in products:
#             item = product()
#             item['price'] = p.xpath('a/div/div[2]/span[@class="standard-price"]/text()').extract()
#             item['title'] = p.xpath('a/div/div[1]/text()').extract()
#             if item['title']:
#                 yield item

#         self.page += 1
#         yield Request(url="http://www.jabong.com/women/clothing/tops-tees-shirts/tops/?page=%d&limit=52&sortField=popularity&sortBy=desc" % self.page,
#                   callback=self.parse, 
#                   dont_filter=True)  
