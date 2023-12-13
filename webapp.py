from flask import Flask, request, render_template, redirect, url_for
from searcher import searcher
from flask import session

app = Flask(__name__)

# Defining the route for the home page
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Defining the route for the save page
@app.route('/save', methods=['POST'])
def save_input(): 
    user_input = str(request.form['user_input'])
    cfg = 'config.toml'
    search_instance = searcher(cfg)
    print("searcher instance created...")
    idx = search_instance.build_index()
    print("Index built...")
    ranker = search_instance.load_ranker()
    print("Ranker loaded...")
    user_input = search_instance.sentiment(user_input)
    print("Processing input: ", user_input)
    query = search_instance.load_query(user_input)
    print("Query loaded...")
    print(query.content())
    print("Running query...")
    results = search_instance.run_query(query, idx, ranker, N=10)
    results_string = search_instance.results_to_string(results)
    print("Results string: ", results_string)
    return render_template('output.html', output_text=results_string.split('\n'))

# main function to run the web app
if __name__ == '__main__':
   app.run(threaded=False)