# -*- coding: utf-8 -*-
 
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
 
import scrapy

class IkeaItem(scrapy.Item):
  book_name = scrapy.Field()
  book_author = scrapy.Field()
  book_published_date = scrapy.Field()
  book_rating = scrapy.Field()
  book_hardcover_price_int = scrapy.Field()
  book_audible_status = scrapy.Field()

  #link = scrapy.Field()
 
class AmazonItem(scrapy.Item):
  # define the fields for your item here like:
  product_name = scrapy.Field()
  product_sale_price = scrapy.Field()
  product_category = scrapy.Field()
  product_original_price = scrapy.Field()
  product_availability = scrapy.Field()
