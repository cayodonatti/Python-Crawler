# -*- coding: utf-8 -*-
import scrapy
import string


class ArtistasSpider(scrapy.Spider):
    name = 'cifraclub'
    allowed_domains = ['cifraclub.com.br']

    letras = list(string.ascii_uppercase)
    start_urls = ['https://www.cifraclub.com.br/letra/' + letra + '/lista.html' for letra in letras]

    def parse(self, response):
        links = []

        for link in response.css('ul.g-1.g-fix.list-links.art-alf > li > a'):
            links.append(link.xpath('@href').extract())

        return {
            'links': links
            }
