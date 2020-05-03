import requests
from bs4 import BeautifulSoup, SoupStrainer
import concurrent.futures
from flask import Flask, request
from flask import jsonify
import time
from generic_methods import open_graph
from API_enrichment import *

app = Flask(__name__)

#landing page
@app.route('/')
def welcome():
    return 'Data Enrichment API'

#get method
@app.route('/get')
def Graph_data():
    start = time.time()
    URL = request.args.get('url')
    #sending request just once
    requested = requests.get(URL).text
    Data = open_graph(requested)
    Data = Enrich_test(URL, Data)
    end  = time.time()
    Data['response_time'] = '%s seconds'%(round(end-start, 2))
    return jsonify(Data)

if __name__ == '__main__':
    app.run(debug=True)

