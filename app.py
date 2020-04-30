import requests
from bs4 import BeautifulSoup, SoupStrainer
import concurrent.futures
from flask import Flask, request
from flask import jsonify
from open_graph import request_and_filter

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Data Enrichment API'

@app.route('/get')
def Graph_data():
    URL = request.args.get('url')
    Data = request_and_filter(URL)
    return Data

if __name__ == '__main__':
    app.run(debug=True)

