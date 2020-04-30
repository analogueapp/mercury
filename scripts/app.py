import requests
from bs4 import BeautifulSoup, SoupStrainer
import concurrent.futures
from flask import Flask, request
from flask import jsonify
from generic_methods import open_graph

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Data Enrichment API'

@app.route('/get')
def Graph_data():
    URL = request.args.get('url')
    requested = requests.get(URL).text
    Data = open_graph(requested)
    return Data

if __name__ == '__main__':
    app.run(debug=True)

