import requests
from bs4 import BeautifulSoup, SoupStrainer
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, request, Response
import json
import time
from generic_methods import main_generic
from enrichment import enrich_test

app = Flask(__name__)

# landing page
@app.route("/")
def welcome():
    return "Data Enrichment API"


# get method
@app.route("/get")
def Graph_data():

    URL = request.args.get("url")

    def streams():

        pool = ThreadPoolExecutor(max_workers=2)

        # sending request just once
        requested = requests.get(URL).text

        data_1 = pool.submit(main_generic, requested)
        data_2 = pool.submit(enrich_test, URL)

        yield json.dumps(data_1.result())
        yield json.dumps(data_2.result())

    return Response(streams())


if __name__ == "__main__":
    app.run(debug=True)
