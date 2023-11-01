import json
import metapy

def tokenize(doc):
    tok = metapy.analyzers.ICUTokenizer(suppress_tags=True)
    tok = metapy.analyzers.LowercaseFilter(tok)
    # tok = metapy.analyzers.LengthFilter(tok, min=2, max=5)
    # tok = metapy.analyzers.Porter2Filter(tok)
    ana = metapy.analyzers.NGramWordAnalyzer(3, tok)
    trigrams = ana.analyze(doc)
    
    tok.set_content(doc.content())
    tokens, counts = [], []
    for token, count in trigrams.items():
        counts.append(count)
        tokens.append(token)
    return tokens, counts

# document loader function that takes in a json file 
# and returns a dict of metapy document objects
def parse_quotes(json_file):
    quote_id = 0
    quotes_raw = json.loads(json_file)
    quotes = {}
    for quote in quotes_raw:
        quote_id += 1
        quote_txt = quote['text'].replace('\n', '')
        quote_txt = quote_txt.replace('\u201c', '')
        quote_txt = quote_txt.replace('\u201d', '')
        author = quote['author'].replace(',','')
        author = author.replace('\n','')
        quotes[quote_id] = {"author": quote['author'], "text": quote_txt}
        quotes[quote_id] = {"author": author, "text": quote_txt}
    return quotes

if __name__ == '__main__':
    quotes_raw_path = 'data/quotes_raw.json'
    with open(quotes_raw_path, 'r') as f:
        quotes_raw_json = f.read()
    quotes = parse_quotes(quotes_raw_json)
    for quote_id, quote in quotes.items():
        doc = metapy.index.Document()
        doc.content(quote['text'])
        tokens = tokenize(doc)
        print(quote_id, quote['author'], quote['text'], tokens)