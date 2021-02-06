import  scrapy
from amazonscrap.items import IkeaItem

class IkeaSpider(scrapy.Spider):
    name = 'ikea'

    allowed_domains = ['http://www.amazon.com/']

    start_urls = ['https://www.amazon.com/Books-Last-30-days/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011']
    
    def parse(self, response):
        item = IkeaItem()
        # for amazon s-include-content-margin s-border-bottom s-latency-cf-section
        books = response.xpath('//div[contains(@class, "s-include-content-margin s-border-bottom s-latency-cf-section")]')
        for book in books:
            item['book_name'] = book.xpath('.//a[@class="a-link-normal a-text-normal"]/span/text()').extract_first()
            item['book_author'] = book.xpath('.//a[@class="a-size-base a-link-normal"]/text()').extract_first()
            item['book_published_date'] = book.xpath('.//span[@class="a-size-base a-color-secondary a-text-normal"]/text()').extract_first()
            item['book_rating'] = book.xpath('.//a[@class="a-link-normal"]/span/text()').extract_first()
            item['book_hardcover_price_int'] = book.xpath('.//span[@class="a-price-whole"]/text()').extract_first()
            item['book_audible_status'] = book.xpath('.//span[@class="a-color-secondary"]/text()').extract_first()
            yield item
    
    # def parse(self, response):
    #     all_books = response.xpath('//article[@class="product_pod"]')
    #     for book in all_books:
    #         book_url = book.xpath('.//h3/a/@href').extract_first()
    #         if 'catalogue/' not in book_url:
    #             book_url = 'catalogue/' + book_url
    #         book_url = self.base_url + book_url
    #         yield scrapy.Request(book_url, callback=self.parse_book)
    #     next_page_partial_url = response.xpath(
    #         '//li[@class="next"]/a/@href').extract_first()
    #     if next_page_partial_url:
    #         if 'catalogue/' not in next_page_partial_url:
    #             next_page_partial_url = "catalogue/" + next_page_partial_url
    #         next_page_url = self.base_url + next_page_partial_url
    #         yield scrapy.Request(next_page_url, callback=self.parse)
    
    # def parse(self, response):
    #     for sel in response.xpath('.//a[contains(@class, "a-link-normal a-text-normal")]'):
    #         item = IkeaItem()
    #         item['link'] = sel.xpath('@href').extract()

    #         yield item

    
    # def parse(self, response):
        
    #     # extract data from response
    #     ranks = response.css("div.zg_itemImmersion").css("span.zg_rankNumber::text").extract()
    #     links = response.css("div.zg_itemImmersion").css("a.a-link-normal::attr(href)").extract()
        
    #     detail_links = []
        
    #     # filter product reviews link
    #     for link in links:
    #     	if 'product-reviews' not in link:
    #     		detail_links.append(link)
    #     for item in zip(ranks, detail_links):
	#         print item[0]
	#         print item[1]

    # def parse_keyword_response(self, response):
    #     products = response.xpath('//*[@data-asin]')

    #     for product in products:
    #         asin = product.xpath('@data-asin').extract_first()
    #         product_url = f"https://www.amazon.com/dp/{asin}"
    #         yield scrapy.Request(url=product_url, callback=self.parse_product_page, meta={'asin': asin})