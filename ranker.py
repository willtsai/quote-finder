import json
import metapy

# function to build the index
def build_index(config_file):
    # create a new inverted index based on the config file
    idx = metapy.index.make_inverted_index(config_file)
    return idx

# function to load the ranker
def load_ranker(config_file):
    # create a new ranker based on the config file
    ranker = metapy.index.OkapiBM25()
    return ranker

# function to load the query
def load_query(query_file):
    # create a new query object based on the query file
    query = metapy.index.Document()
    query.content(query_file)
    return query

# function to run the query
def run_query(query, idx, ranker):
    N=5
    # use the ranker to rank the documents in the index for the given query
    results = ranker.score(idx, query, num_results=N)
    return results

# function to print the results
def print_results(results, quotes_map):
    # print the results
    quotes_dict = {}
    with open(quotes_map, 'r') as f:
        quotes_dict = json.load(f)
        f.close()
    for result in results:
        print(
            "quote_id: ", result[0] 
            , "score: ", result[1]
            , "\"" + quotes_dict[str(result[0])]['text'] + "\""
            , " --" + quotes_dict[str(result[0])]['author']
            )

if __name__ == '__main__':
    # ask user for input
    user_input = input("Enter your search terms: ")
    # paths
    quotes_map_path = 'goodreads/quotes_map.json'
    # index
    cfg = 'config.toml'
    idx = build_index(cfg)
    ranker = load_ranker(cfg)
    query = load_query(user_input)
    # results
    results = run_query(query, idx, ranker)
    print_results(results, quotes_map_path)