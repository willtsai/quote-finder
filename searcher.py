import json
import metapy
import nltk
from nltk.corpus import sentiwordnet as swn

# searcher class to handle the index, ranker, and query
class searcher:
    # constructor that takes in a config file and initializes the searcher
    def __init__(self, config_file):
        self.config_file = config_file
        nltk.download('sentiwordnet')
        nltk.download('wordnet')

    # function to build the index
    def build_index(self):
        # create a new inverted index based on the config file
        idx = metapy.index.make_inverted_index(self.config_file)
        return idx

    # function to load the ranker
    def load_ranker(self):
        # create a new ranker based on the config file
        ranker = metapy.index.OkapiBM25()
        return ranker

    # function to load the query
    def load_query(self, input_query):
        # create a new query object based on the query file
        query = metapy.index.Document()
        query.content(input_query)
        return query

    # function to run the query
    def run_query(self, query, idx, ranker, N=5):
        # use the ranker to rank the documents in the index for the given query
        results = ranker.score(idx, query, num_results=N)
        return results
    
    # function to mine the input for sentiment
    def sentiment(self, phrase):
        words = phrase.split()
        query = set()
        query_string = ""
        for word in words:
            query.add(word)
            for senti_synset in list(swn.senti_synsets(word)):
                query.add(senti_synset.synset.name().split('.')[0])
        for word in query:
            query_string += word + " "
        query_string = query_string.strip()
        return query_string

    # function to print the results
    def results_to_string(self, results):
        quotes_map = 'quotes/quotes_map.json'
        quotes_dict = {}
        results_string = ""
        with open(quotes_map, 'r') as f:
            quotes_dict = json.load(f)
            f.close()
        for result in results:
            results_string += " \"" + quotes_dict[str(result[0])]['text'] + "\" --" + quotes_dict[str(result[0])]['author'] + "\n"
        return results_string