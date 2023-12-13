import scrapy
import os
from scrapy.crawler import CrawlerProcess # CrawlerProcess is used to create a crawling process
from scrapy.utils.project import get_project_settings

# Spider class to handle the web crawling
class GoodreadsSpider(scrapy.Spider): 
    # the name of the spider
    name = 'Goodreadsquotes'
    # a list of domains that this spider is allowed to crawl
    allowed_domains = ['goodreads.com']
    #  a list of URLs where the spider will begin to crawl from
    start_urls = ['https://www.goodreads.com/quotes']

    # the method that will be called to handle the response downloaded for each of the requests made
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('div.quoteText::text').get().strip(),
                'author': quote.css('div.quoteText > span[class="authorOrTitle"]::text').get(),
            }
        next_page = response.css('a.next_page::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

# main function to run the crawler
if __name__ == '__main__':
    # Check if file already exists and deletes it before crawling again
    file_path = 'data/quotes.json'
    if os.path.exists(file_path):
        os.remove(file_path)
    # settings are used to customize the behaviour of all Scrapy components, including file format and directory
    process = CrawlerProcess(settings={ 
        'FEEDS': {
            'data/quotes.json': {
                'format': 'json',
                'overwrite': True,
            },
        },
        'FEED_EXPORT_ENCODING': 'utf8',
    })
    process.crawl(GoodreadsSpider)
    process.start()