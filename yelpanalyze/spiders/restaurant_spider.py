# -*- coding: utf-8 -*-
import scrapy
from yelpanalyze.items import YelpanalyzeItem

class yelpanalyze_spider(scrapy.Spider):
    name = "restaurant_spider"
    allowed_domains = ["yelp.com"]
    start_urls = ['https://www.yelp.com/search?find_desc=Restaurants&find_loc=San+Francisco,+CA&start=' + str(n) for n in range(0,1000,10)]
    

    def parse(self, response):
                  #URL for each restaurant
                  each_restaurant = response.xpath('//a[contains(@class, "photo-box-link__373c0__1AvT5")]/@href').extract()
                  restaurant = ['https://www.yelp.com' + i for i in each_restaurant]

                  for url in restaurant:
                              yield scrapy.Request(url, callback = self.parse_rest)
                              
                              
      


    def parse_rest(self, response):
      
                  Name = response.xpath('//h1[contains(@class, "biz-page-title embossed-text-white")]/text()').extract()[0].strip()
                  Overallrating = float(response.xpath('//div[contains(@class,"biz-rating biz-rating-very-large clearfix")]//@title').extract()[0].split()[0])
                  NumberReviews = int(response.xpath('//span[contains(@class,"review-count rating-qualifier")]/text()').extract()[0].split()[0])
                  PriceRange = response.xpath('//span[contains(@class,"business-attribute price-range")]/text()').extract()[0].strip()
                  Category = response.xpath('//span[contains(@class,"category-str-list")]/a/text()').extract()[0]
                  #Delivery = response.xpath('//*[@id="super-container"]/div/div/div[2]/div[2]/div[4]/ul/li/div/dl[6]/dd/text()').extract()[0].strip()
                  
                  key = response.xpath('//div[contains(@class,"short-def-list")]//dt/text()').extract()
                  key = [x.strip() for x in key]
                  value = response.xpath('//div[contains(@class,"short-def-list")]//dd/text()').extract()
                  value =  [x.strip() for x in value]
                  
                  attributes = dict(zip(key,value))
                  
                  #Delivery = attributes['Delivery']
                  Delivery = (attributes['Delivery'] if 'Delivery' in attributes.keys() else 'N/A')

                  
                  item = YelpanalyzeItem()
                  item['Name'] = Name
                  item['Overallrating'] = Overallrating
                  item['NumberReviews'] = NumberReviews
                  item['PriceRange'] = PriceRange
                  item['Category'] = Category
                  item['Delivery'] = Delivery
                  
                  
                  yield item
