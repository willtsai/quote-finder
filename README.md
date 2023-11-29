# Sentiment-based search for famous quotes

CS 410: Text Information Systems, University of Illinois Urbana-Champaign, Fall 2023 

## Authors

**Team: Lunar-Tsai**
- Manuel Suarez Lunar | [manuel6@illinois.edu](manuel6@illinois.edu)
- Wei-Lun (Will) Tsai | [wltsai2@illinois.edu](wltsai2@illinois.edu) --> team captain

## Overview

Our team project will be focused on the development of a unique search engine / text retrieval tool specifically tailored for literature and quote enthusiasts. Leveraging the vast repository of quotes available on Goodreads.com, our text retrieval tool will use a web crawler to sift through the website's quotes content. Unlike traditional search engines, ours will be sentiment-centric; users will input a particular sentiment or emotion, and our system will return a ranked list of famous quotes resonating with that sentiment. Additionally, in parallel to the core functionality of the search engine, we would also like to introduce an add-on feature enhancing the user's experience. By capitalizing on the same sentiment input, this feature will produce a ranked list of authors whose body of work predominantly aligns with the specified emotion or sentiment. This will not only allow users to discover quotes but also introduce them to authors who resonate with their current feelings, enabling a deeper exploration of literature in tune with their emotional state. And finally, we would also build a web interface where the user can submit the inputs for both search functionalities.

## Setup Instructions

1. If you are running this on an Apple Silicon Mac (e.g. M1, M2 chips), adjust your Conda config:

    ```bash
    conda config --env --set subdir osx-64
    ```

2. Create a Python 3.5 Conda environment:

    ```bash
    conda create -n py35
    ```

3. Setup your Conda command line prompt:

    ```bash
    export CONDA_DIR=conda info | grep -i 'base environment' && source $CONDA_DIR/etc/profile.d/conda.sh
    ```

4. Install and activate the Python 3.5 Conda environment:

    ```bash
    conda activate py35 && conda install python=3.5
    ```

5. Install the project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Run the web crawler and preprocessor to prepare the quotes data:

    ```bash
    python web_crawler.py && python preprocessor.py
    ```

7. Create and activate a Flask environment for the web application:

    ```bash
    python -m venv .venv && . .venv/bin/activate
    ```

8. Run the web app:

    ```bash
    python webapp.py
    ```

9. Navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in a web browser to interact with the Quote Finder web application.