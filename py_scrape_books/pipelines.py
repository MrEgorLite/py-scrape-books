# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from py_scrape_books.spiders.books import BooksSpider


class PyScrapeBooksPipeline:
    def process_item(self, item: dict, spider: BooksSpider) -> dict:
        return item
