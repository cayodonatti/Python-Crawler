# -*- coding: utf-8 -*-
import scrapy
import json


class CifrasSpider(scrapy.Spider):
    name = 'Macaco de bola verde'
    allowed_domains = ['cifraclub.com.br']

    
    musicas = json.load(open('musicas.json', 'r'))

    start_urls = []
    
    
    for a in musicas:
        lista = a['links']

        for b in lista:
            start_urls.append('https://www.cifraclub.com.br' + b[0])
    

    def parse(self, response):
        links = []

        music_name = response.css('div.g-1.g-fix.cifra > div.g-side-ad > h1.t1').xpath('string(.)').extract()
        artist_name = response.css('div.g-1.g-fix.cifra > div.g-side-ad > h2.t3').xpath('string(.)').extract()

        for link in response.css('div.cifra_cnt.g-fix.cifra-mono > pre > b'):
            links.append(link.xpath('string(.)').extract())

        return {
            "url": response.url,
            'music_name': music_name,
            'artist_name': artist_name,
            'chords': links
            }