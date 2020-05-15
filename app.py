from bs4 import BeautifulSoup, SoupStrainer
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from flask import Flask, request, jsonify
import requests

from utils.tag_parsers import main_generic
from utils.enrichment import enrich_test
from constants import sentry_key, sentry_org, sentry_project

#initializing sentry
sentry_sdk.init(
    dsn=f'https://{sentry_key}@{sentry_org}.ingest.sentry.io/{sentry_project}',
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Data Enrichment API"

@app.route("/get")
def Graph_data():
 
    URL = request.args.get("url")

    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    
    return jsonify(get_data)

@app.route("/enrich")
def enrichment():

    URL = request.args.get("url")

    enriched_data = enrich_test(URL)

    return jsonify(enriched_data)


if __name__ == "__main__":
    app.run()