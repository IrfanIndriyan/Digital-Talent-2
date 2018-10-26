# -*- coding: utf-8 -*-
import scrapy
import string

class KompasSpider(scrapy.Spider):
    """
    """
    name = 'kompas'
    # allowed_domains = ['indeks.kompas.com']
    
    # use this variable to select news catagory
    catagory = ""
    
    # use this varible to specify published date
    date = ""
    
    # generate link
    # default catagory is news
    # default date is today
    if catagory or date != '':
        if catagory != '' & date == '':
            start_urls = ['http://indeks.kompas.com/%s/' % (catagory)]
        elif catagory == '' & date != '':
            start_urls = ['http://indeks.kompas.com/news/%s/' % (date)]
        else:
            start_urls = ['http://indeks.kompas.com/%s/%s/' % (catagory, date)]
    else:
        # default link
        start_urls = ['http://indeks.kompas.com/']

    def parse(self, response):
        """
        Indeks
        ------
        article list: response.css("div.article__list")

        article link: response.css("h3.article__title > a::attr(href)").extract_first()
        page: response.css("div.paging__item > a.paging__link--next::attr(href)").extract_first()
        """
        articles = response.css("h3.article__title > a::attr(href)").extract()

        for article in articles:
            yield scrapy.Request(url=article, callback=self.parse_article)

        # Get the next page link
        # Note. there might be some issue here,
        #       the "next" and "first" has the same tag and class
        #       Still, there is a different:
        #           * data-ci-pagination: the number of page (1,..., the last page(in number))
        #           * rel: start, next, prev
        #           * text(content): prev, next, first, last
        next_page = response.css("div.paging__item > a.paging__link--next::attr(href)").extract_first()

        if next_page is not None:
             yield scrapy.Request(next_page, callback=self.parse)

    def parse_article(self, response):
        """
        Article
        -------
        title: response.css("h1.read__title::text").extract_first()
        author: response.css("div.read__author > a::text").extract_first()
        time: response.css("div.read__time::text").extract_first()
        content: response.css("div.read__content > p")
        
        Note.
        - time format: identity - DD/MM/YYYY, hh:mm time_zone
        - extracting content ::text
        """
        title = response.css("h1.read__title::text").extract_first()
        author = response.css("div.read__author > a::text").extract_first()

        article = response.css("div.read__content > p")
        content = ""

        for paragraf in article:
            p = paragraf.css("::text").extract()
            if p is not None or "Baca juga: " not in p :
                content += "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in p]).strip()
        
        yield {
            "title": title,
            "author": author,
            "content": content
        }
