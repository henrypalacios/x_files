from typing import Generator

import scrapy
from scrapy.http import Response


class CiaSpider(scrapy.Spider):
    name = 'cia'
    allowed_domains = ['www.cia.gov']
    start_urls = ['https://www.cia.gov/library/readingroom/historical-collections']

    custom_settings = {
        'FEEDS': {
            'cia.json': {
            'format': 'json',
            'encoding': 'utf8',
            'store_empty': False,
            'indent': 4}
        }
    }

    def parse(self, response: Response) -> Generator[Generator, None, None]:
        links_declassified = response.xpath('//a[starts-with(@href,"collection") and (parent::h3 | parent::h2)]/@href').getall()

        for link in links_declassified:
            yield response.follow(link, callback=self._document, 
                                    cb_kwargs={'url':response.urljoin(link)})

    def _document(self, response: Response, **kwargs: dict) -> Generator[dict, None, None]:
        link = kwargs['url']
        title = response.xpath('//h1[@class="documentFirstHeading"]/text()').get()
        paragraphs = response.xpath('//div[@class="field-item even"]//p[string-length(text()) > 3 and not(@class)]/text()').getall()
        img =  response.xpath('//div[@class="field-item even"]//a[not(@class) and @target="_blank"]/img/@src').get()

        yield {
            'url': link,
            'title': title,
            'body': paragraphs,
            'img': img
        }