import json
import os
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
        quote_txt = quote['text'].replace('\n', '')
        quote_txt = quote_txt.replace('\u201c', '')
        quote_txt = quote_txt.replace('\u201d', '')
        author = quote['author'].replace(',','')
        author = author.replace('\n','')
        author = author.replace('    ', '')
        author = author.replace('  ', ' ')
        quotes[quote_id] = {"author": quote['author'], "text": quote_txt}
        quotes[quote_id] = {"author": author, "text": quote_txt}
        quote_id += 1
    return quotes

if __name__ == '__main__':
    quotes_raw_path = 'data/quotes.json'
    quotes_map_path = 'sentiment/quotes_map.json'
    quotes_path = 'sentiment/quotes.dat'
    # read quotes.json
    with open(quotes_raw_path, 'r') as f:
        quotes_raw_json = f.read()
        f.close()
    quotes = parse_quotes(quotes_raw_json)
    # write quotes to quotes_map.json
    with open(quotes_map_path, 'w') as f:
        json.dump(quotes, f)
        f.close()
    #clear quotes.dat
    open(quotes_path, 'w').close()
    # write quotes to quotes.dat
    for quote_id, quote in quotes.items():
        author = quote['author'].strip()
        text = quote['text'].strip()
        print('processing quote: \"', text, '\"', ' --', author)
        doc = metapy.index.Document()
        doc.content(quote['text'])
        tokens = tokenize(doc)
        with open(quotes_path, 'a') as f:
            f.write(text + '\n')
            f.close()
    print('done processing quotes, saved to', quotes_path, 'and', quotes_map_path)
    # recusively delete idx directory to force rebuild since data has changed
    print('cleared `./idx` since data has changed...')
    os.system('rm -rf idx')