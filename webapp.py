from flask import Flask, request, render_template, redirect, url_for # Importing the Flask class from flask.py
from searcher import searcher  # Importing the searcher class from searcher.py

app = Flask(__name__) # Creating an instance of the Flask class

@app.route('/', methods=['GET']) # Defining the route for the home page
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST']) # Defining the route for the save page
def save_input():
    user_input = request.form['user_input']
    
    # Save user input to a file
    with open('user_input.txt', 'w') as file:
        file.write(user_input)

    # Create an instance of the searcher class and process the input
    search_instance = searcher('config.toml')
    search_instance.build_index() # Builds the index
    ranker = search_instance.load_ranker() # Loads the ranker
    query = search_instance.load_query()  # Loads the query
    search_instance.run_query(query, search_instance.build_index(), ranker)  # Outputs to output.file

    # Redirecting to the output page
    return redirect(url_for('show_output'))

@app.route('/output', methods=['GET']) # Defining the route for the output page
def show_output(): 
  with open('output.txt', 'r') as file:
            output_text = file.read()

    return render_template('output.html', output_text=output_text)

if __name__ == '__main__':
    app.run(debug=False)

    