# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field


class WikipediaItem(Item):

    title = Field()
    url = Field()
