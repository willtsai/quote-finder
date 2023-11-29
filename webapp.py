from flask import Flask, request, render_template, redirect, url_for # Importing the Flask class from flask.py
from searcher import searcher  # Importing the searcher class from searcher.py
from flask import session # Importing the session class from flask.py

app = Flask(__name__) # Creating an instance of the Flask class

@app.route('/', methods=['GET']) # Defining the route for the home page
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST']) # Defining the route for the save page
def save_input(): 
    user_input = str(request.form['user_input']) # Getting the user input from the form
    cfg = 'config.toml' # The path to the config file
    search_instance = searcher(cfg) # Create an instance of the searcher class and process the input
    print("searcher instance created...")
    idx = search_instance.build_index() # Builds the index
    print("Index built...")
    ranker = search_instance.load_ranker() # Loads the ranker
    print("Ranker loaded...")
    user_input = search_instance.sentiment(user_input) # Processes the input
    print("Processing input: ", user_input)
    query = search_instance.load_query(user_input)  # Loads the query
    print("Query loaded...")
    print(query.content())
    print("Running query...")
    results = search_instance.run_query(query, idx, ranker)  # Runs the query
    results_string = search_instance.get_results_string(results) # Gets the results as a string
    print("Results string: ", results_string)
    return render_template('output.html', output_text=results_string)

if __name__ == '__main__':  
   app.run() # Runs the app