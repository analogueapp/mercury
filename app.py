from bs4 import BeautifulSoup, SoupStrainer
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from flask import Flask, request, jsonify
import requests
import logging

from dotenv import load_dotenv
import os

load_dotenv()

from utils.tag_parsers import main_generic
from utils.enrichment import enrich_test

sentry_key = os.getenv("SENTRY_KEY")
sentry_org = os.getenv("SENTRY_ORG")
sentry_project = os.getenv("SENTRY_PROJECT")

# initializing sentry
sentry_sdk.init(
    dsn=f"https://{sentry_key}@{sentry_org}.ingest.sentry.io/{sentry_project}",
    integrations=[FlaskIntegration()],
)

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Data Enrichment API"


@app.route("/get")
def Graph_data():

    URL = request.args.get("url")

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
        }
        requested = requests.get(URL, headers=headers, timeout=10)
        if requested.status_code != 200:
            return jsonify(error="URL failed to load")

    except Exception as e:
        logging.error(f"Error loading page: {e}")
        return jsonify(error="URL failed to load")

    get_data = main_generic(requested.text, URL)

    return jsonify(get_data)


@app.route("/enrich")
def enrichment():

    URL = request.args.get("url")

    enriched_data = enrich_test(URL)

    return jsonify(enriched_data)


if __name__ == "__main__":
    app.run()
