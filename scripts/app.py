import requests
from bs4 import BeautifulSoup, SoupStrainer
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, request
from flask import jsonify
import time
from generic_methods import open_graph
from API_enrichment import *

app = Flask(__name__)

# landing page
@app.route("/")
def welcome():
    return "Data Enrichment API"


# get method
@app.route("/get")
def Graph_data():
    start = time.time()

    pool = ThreadPoolExecutor(max_workers=2)

    URL = request.args.get("url")
    # sending request just once
    requested = requests.get(URL).text

    data_1 = pool.submit(open_graph, requested)
    data_2 = pool.submit(Enrich_test, URL)

    data_1.result().update(data_2.result())

    end = time.time()
    data_1.result()["response_time"] = "%s seconds" % (round(end - start, 2))
    return jsonify(
            data_1.result()
        )


if __name__ == "__main__":
    app.run(debug=True)
