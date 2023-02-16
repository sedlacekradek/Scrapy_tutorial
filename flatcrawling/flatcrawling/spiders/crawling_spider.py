from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CrawlingSpider(CrawlSpider):
    name = "stodulky"
    allow_domains = ["bydleni-stodulky.cz"]
    start_urls = ["https://www.bydleni-stodulky.cz/stodulky/cenik/"]
    rules = (
        Rule(LinkExtractor(allow="detail-bytu/"), callback="parse_item"),
    )

    def parse_item(self, response):
        yield {
            "jednotka": response.css(".float-right::text")[5].get(),
            "dispozice": response.css(".float-right::text")[6].get(),
            "podlaží": response.css(".float-right::text")[7].get(),
            "plocha": response.css(".float-right::text")[8].get(),
            "orientace": response.css(".float-right::text")[9].get(),
            "k nastěhování": response.css(".float-right::text")[10].get(),
            "cena": response.css(".float-right::text")[11].get().strip(),
            "stav": response.css(".text-uppercase span::text").get(),
            "pdf": response.css(".js-analytics-flat-file-download::attr(href)").get(),
            "plán": response.css(".js-lightgallery-classic a::attr(href)").get(),
            "zdroj": response.url,
        }


class CrawlingSpider2(CrawlSpider):
    name = "skvrnany"
    allow_domains = ["byty-skvrnany.cz"]
    start_urls = ["https://www.byty-skvrnany.cz/skvrnany/cenik/"]
    rules = (
        Rule(LinkExtractor(allow="detail-bytu/"), callback="parse_item"),
    )

    def parse_item(self, response):
        yield {
            "jednotka": response.css(".float-right::text")[5].get(),
            "dispozice": response.css(".float-right::text")[6].get(),
            "podlaží": response.css(".float-right::text")[7].get(),
            "plocha": response.css(".float-right::text")[8].get(),
            "orientace": response.css(".float-right::text")[9].get(),
            "k nastěhování": response.css(".float-right::text")[10].get(),
            "cena": response.css(".float-right::text")[11].get().strip(),
            "stav": response.css(".text-uppercase span::text").get(),
            "pdf": response.css(".js-analytics-flat-file-download::attr(href)").get(),
            "plán": response.css(".js-lightgallery-classic a::attr(href)").get(),
            "zdroj": response.url,
        }


class CrawlingSpider3(CrawlSpider):
    name = "knoviz"
    allow_domains = ["www.knoviz22.cz"]
    start_urls = ["https://www.knoviz22.cz/o-projektu"]
    rules = (
        Rule(LinkExtractor(allow="family", deny="rodinny"), callback="parse_item"),
    )

    def parse_item(self, response):
        yield {
            "jednotka": response.css("h3 strong::text").get().replace("Samostatný rodinný dům č.", ""),
            "dispozice":  response.xpath('//div[2]//p//text()').getall()[3].replace("typ domu:", "").replace("\xa0", ""),
            "podlaží": "-",
            "plocha": "".join(response.xpath('//div[2]//p//text()').getall()[8:10]).replace("\n", "").replace("\xa0m2\xa0", "").strip(),
            "orientace": "JV, SZ",
            "k nastěhování": "-",
            "cena": response.xpath('//div[2]//p//text()').getall()[-24].replace("\n", "").replace("\xa0", "").replace("cena:", ""),
            "stav": "volný",
            "pdf": response.css(".block-inline h4 a::attr(href)").get(),
            "plán": response.css(".block-inline h4 a::attr(href)").getall()[2],
            "zdroj": response.url,
        }