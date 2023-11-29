# bash script to set up the environment for the project
#!/bin/bash

conda create -n py35 python=3.5
conda activate py35
pip install -r requirements.txt
. .venv/bin/activate
python web_crawler.py
python preprocessor.py

echo "Setup complete. Please run `python web_app.py` to start the web app."