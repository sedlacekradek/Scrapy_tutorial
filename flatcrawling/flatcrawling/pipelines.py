# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


def convert_price(price: str) -> str:
    """
    Converts price string from e.g. '5 580 000 Kč' to '5.58 mil. Kč'

    :param price: string of price value to be converted
    :return: string in format "x.xx mil. Kč"
    """
    price = int((price[:-2]).replace(" ", ""))
    price = str(round(price / 1000000, 2)) + " mil. Kč"
    return price


class StodulkyPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if "mil" not in adapter["cena"]:
            adapter['cena'] = convert_price(adapter["cena"])
        adapter['plocha'] = adapter['plocha'].replace("M", "m2")
        return item


class SkvrnanyPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if "mil" not in adapter["cena"]:
            adapter['cena'] = convert_price(adapter["cena"])
        adapter['plocha'] = adapter['plocha'].replace("M", "m2")
        return item


class KnovizPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        # clean html
        adapter['cena'] = adapter['cena'].replace("\n", "").replace("\xa0", "").replace("cena:", "")
        adapter['jednotka'] = adapter['jednotka'].replace("Samostatný rodinný dům č.", "")
        adapter['dispozice'] = adapter['dispozice'].replace("typ domu:", "").replace("\xa0", "")
        return item
