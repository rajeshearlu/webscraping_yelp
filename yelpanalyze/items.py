# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YelpanalyzeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	Name = scrapy.Field()
	#City = scrapy.Field()
	Overallrating = scrapy.Field()
	NumberReviews = scrapy.Field()
	PriceRange = scrapy.Field()
	Category = scrapy.Field()
	#Address = scrapy.Field()
	#Phonenumber = scrapy.Field()
	#userlocation = scrapy.Field()
	#userrating = scrapy.Field()
	#userlanguage = scrapy.Field()
	Delivery = scrapy.Field()	
    #pass
