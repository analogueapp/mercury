from bs4 import BeautifulSoup, SoupStrainer
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from flask import Flask, request, jsonify
import requests

from dotenv import load_dotenv
import os
load_dotenv()

from utils.tag_parsers import main_generic
from utils.enrichment import enrich_test

sentry_key = os.getenv('SENTRY_KEY')
sentry_org = os.getenv('SENTRY_ORG')
sentry_project = os.getenv('SENTRY_PROJECT')

spotify_client_id = os.getenv('SPOTIFY_CLIENT_ID')
spotify_client_skey = os.getenv('SPOTIFY_CLIENT_SKEY')
wikipedia_url = os.getenv('WIKIPEDIA_URL')

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