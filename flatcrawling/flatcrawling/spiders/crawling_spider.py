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