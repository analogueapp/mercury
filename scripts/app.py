import requests
from bs4 import BeautifulSoup, SoupStrainer
import concurrent.futures
from flask import Flask, request
from flask import jsonify
import time
from generic_methods import open_graph
from API_enrichment import *

app = Flask(__name__)

APIs =['www.goodreads.com']

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
    site_name = URL.split('/')[2]
    if site_name in APIs:
        if site_name == 'www.goodreads.com':
            Data =  (fetch_goodreads(Data["ks:isbn"], Data))
    end  = time.time()
    Data['response_time'] = '%s seconds'%(round(end-start, 2))
    return Data

if __name__ == '__main__':
    app.run(debug=True)

