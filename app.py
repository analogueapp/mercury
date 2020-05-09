from bs4 import BeautifulSoup, SoupStrainer
from sentry_sdk.integrations.flask import FlaskIntegration
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, request, Response
import json
import requests
import sentry_sdk

from utils.tag_parsers import main_generic
from utils.enrichment import enrich_test
from constants import sentry_dsn

#initializing sentry
sentry_sdk.init(dsn=sentry_dsn, integrations=[FlaskIntegration()])

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

        requested = requests.get(URL).text

        data_1 = pool.submit(main_generic, requested)
        data_2 = pool.submit(enrich_test, URL)

        yield json.dumps(data_1.result())
        yield json.dumps(data_2.result())

    return Response(streams())


if __name__ == "__main__":
    app.run()
