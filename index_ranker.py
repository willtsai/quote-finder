import json
import metapy

class index_ranker:
    # constructor
    def __init__(self, config_file):
        self.config_file = config_file

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
    def load_query(self, query_file):
        # create a new query object based on the query file
        query = metapy.index.Document()
        query.content(query_file)
        return query

    # function to run the query
    def run_query(self, query, idx, ranker):
        N=5
        # use the ranker to rank the documents in the index for the given query
        results = ranker.score(idx, query, num_results=N)
        return results

    # function to print the results
    def print_results(self, results, quotes_map):
        # print the results
        print("\nHere are the top %d results:\n" % len(results))
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

## this code will go into the web app (API)
# if __name__ == '__main__':
#     # paths
#     quotes_map_path = 'sentiment/quotes_map.json'
#     # load index and ranker
#     cfg = 'config.toml'
#     controller = index_ranker(cfg)
#     idx = controller.build_index()
#     ranker = controller.load_ranker()

#     # terminal console interface
#     while True:
#         user_input = input("Enter your search terms (\"Q\" to quit): ")
#         if user_input in ['Q', 'q']:
#             print("Goodbye!")
#             break
#         query = controller.load_query(user_input)
#         # results
#         results = controller.run_query(query, idx, ranker)
#         controller.print_results(results, quotes_map_path)
#         print("\n*************************************\n")