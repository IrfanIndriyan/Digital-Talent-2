# -*- coding: utf-8 -*-
import scrapy


class KompasSpider(scrapy.Spider):
    name = 'kompas'
    # allowed_domains = ['indeks.kompas.com/']
    start_urls = ['http://indeks.kompas.com//']

    """
	Indeks
	------
	Content url: response.css("h3.article__title > a::attr(href)").extract_first()
	Page: response.css("div.paging__item > a.paging__link--next::attr(href)").extract_first()
	
	Need form feature, can be used to:
	 * Select article catagory
	 * Date published

    Article
    -------
    Title: response.css("h1.read__title::text").extract_first()
    Author: response.css("div.read__author > a::text").extract_first()
	Content: respose.css("div.read__content > p::text").extract()

	Note. Beware with html tag <a></a> in content.
    """
    
    def parse(self, response):
        pass
