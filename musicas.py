# -*- coding: utf-8 -*-
import scrapy
import json


class MusicasSpider(scrapy.Spider):
    name = 'a very hungry dude'
    allowed_domains = ['cifraclub.com.br']

    custom_settings = {
        'BOT_NAME': 'bolaazul',
        'CONCURRENT_REQUESTS': 2,
        'DOWNLOAD_MAXSIZE': 0
    }

    artistas = json.load(open('artistas.json', 'r'))

    start_urls = []

    for a in artistas:
        lista = a['links']

        for b in lista:
            start_urls.append('https://www.cifraclub.com.br' + b[0])

    def parse(self, response):
        links = []

        for link in response.css('ul.list-links.art_musics.alf.all > li > a.art_music-link'):
            links.append(link.xpath('@href').extract())

        return {
            'links': links
            }