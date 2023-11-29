# bash script to set up the environment for the project
#!/bin/bash

# setup conda python 3.5 env for metapy
# conda update -n base -c defaults conda
conda create -n py35
conda activate py35
conda install python=3.5

# detect if using arm64
if [[ $(uname -m) == 'arm64' ]]; then
    conda config --env --set subdir osx-64
else
    echo "Using x86_64 architecture"
fi

# install dependencies
pip install -r requirements.txt

# crawl and preprocess data
python web_crawler.py
python preprocessor.py

# activate flask env for webapp
. .venv/bin/activate

echo "Setup complete. Please run \`python webapp.py\` to start the web app."