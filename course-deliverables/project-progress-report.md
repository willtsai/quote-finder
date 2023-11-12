# CS 410 Project Proposal, Fall 2023 

## Team Info 

- Manuel Suarez Lunar | [manuel6@illinois.edu](manuel6@illinois.edu)
- Wei-Lun (Will) Tsai | [wltsai2@illinois.edu](wltsai2@illinois.edu) --> team captain 
- Code repository | [quote-finder](https://github.com/willtsai/quote-finder)

## Summary

@Will (overall architecture)

## Progress Update

So far, we have built a web crawler that uses the Scrapy python library to crawl Goodreads.com and extract all the quotes available in the website onto a JSON file, a tokenizer to create a bag of words representation of the quotes, an index to store our bag of words data and a ranker to provide a list of results in response to a user query.

### Web crawler

For our web crawler, we used the Scrapy library. We wrote a script that creates a Scrapy spider that will start at the Goodreads quotes page, extract quotes, the author’s name, and tags for each quote, and then follow the “next” link to crawl subsequent pages. Lastly, it outputs the quotes to a JSON file that’s picked up by the preprocessor script.

### Preprocessor

@Will

### Indexer and Ranker

@Will

## Next Steps

In the following weeks we’ll be focusing on creating the sentiment analyzer script and integrating its output into our index so that we can store sentiments tags to each quote. Then we’ll work on creating the web application that will communicate between our python scripts and the web interface (website). Then we’ll create the web interface that will be responsible for allowing the user to submit their desired input and then view a ranked list of quotes and authors based on their sentiment. Finally, we’ll move our application to a public cloud provider (e.g., Azure) to host our application in a 24/7 and seamless manner.

### Sentiment Analyzer

@Will

### Web Application (API)

@Will

### User Interface

For the web interface, we’ll use standard HTML code to configure the visuals of the website and connect that to the our web app (Flask).