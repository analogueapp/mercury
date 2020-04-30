import requests
from bs4 import BeautifulSoup, SoupStrainer
import concurrent.futures
from flask import Flask, request
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Data Enrichment API'

if __name__ == '__main__':
    app.run(debug=True)

