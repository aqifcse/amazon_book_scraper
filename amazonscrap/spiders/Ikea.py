import  scrapy
from amazonscrap.items import IkeaItem

class IkeaSpider(scrapy.Spider):
    name = 'ikea'

    allowed_domains = ['http://www.amazon.com/']

    start_urls = ['https://www.amazon.com/Books-Last-30-days/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011']

    def parse(self, response):
        for sel in response.xpath('.//a[contains(@class, "a-link-normal a-text-normal")]'):
            item = IkeaItem()
            item['link'] = sel.xpath('@href').extract()

            yield item

    
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