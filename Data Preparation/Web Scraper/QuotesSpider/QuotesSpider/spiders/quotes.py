# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
	name = 'quotes'
	# allowed_domains = ['http://quotes.toscrape.com/']
	start_urls = ['http://quotes.toscrape.com/']

	def parse(self, response):
		quotes_ = response.css("div.quote")
		
		for quote in quotes_:
			yield {
				"quote": quote.css("span.text::text").extract_first(),
				"author": quote.css("small.author::text").extract_first(),
				"tags": quote.css("a.tag::text").extract()
			}

		next_url = response.css("li.next > a::attr(href)").extract_first()

		if next_url is not None:
			next_page = response.urljoin(next_url)
			yield scrapy.Request(next_page, callback=self.parse)