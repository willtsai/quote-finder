import scrapy
from scrapy.crawler import CrawlerProcess # CrawlerProcess is used to create a crawling process
from scrapy.utils.project import get_project_settings

class GoodreadsSpider(scrapy.Spider): 
    name = 'Goodreadsquotes' # the name of the spider
    allowed_domains = ['goodreads.com'] # a list of domains that this spider is allowed to crawl
    start_urls = ['https://www.goodreads.com/quotes'] #  a list of URLs where the spider will begin to crawl from

    def parse(self, response): # the method that will be called to handle the response downloaded for each of the requests made
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('div.quoteText::text').get().strip(),
                'author': quote.css('div.quoteText > span[class="authorOrTitle"]::text').get(),
            }
        next_page = response.css('a.next_page::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

if __name__ == '__main__':
    process = CrawlerProcess(settings={ # settings are used to customize the behaviour of all Scrapy components, including file format and directory
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