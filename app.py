from bs4 import BeautifulSoup, SoupStrainer
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import logging

from dotenv import load_dotenv
import os

load_dotenv()

from utils.tag_parsers import main_generic
from utils.enrichment import enrich_test
from utils.request import send_request, handle_params
from utils.search import search

sentry_key = os.getenv("SENTRY_KEY")
sentry_org = os.getenv("SENTRY_ORG")
sentry_project = os.getenv("SENTRY_PROJECT")

if os.getenv("FLASK_ENV") != "development":
    sentry_sdk.init(
        dsn=f"https://{sentry_key}@{sentry_org}.ingest.sentry.io/{sentry_project}",
        integrations=[FlaskIntegration()],
    )

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route("/")
def welcome():
    return "Data Enrichment API"


@app.route("/get")
def Graph_data():

    all_params = dict(request.args)

    request_object = send_request(all_params)

    if isinstance(request_object, dict):
        return jsonify(request_object)

    get_data = main_generic(request_object, handle_params(all_params))

    return jsonify(get_data)


@app.route("/enrich")
def enrichment():

    URL = request.args.get("url")

    enriched_data = enrich_test(URL)

    return jsonify(enriched_data)


@app.route("/api/search")
def search_endpoint():

    query = request.args.get("query")
    medium = request.args.get("medium")
    medium_id = request.args.get("id")

    results = search(query, medium, medium_id)

    return jsonify(results)


if __name__ == "__main__":
    app.run()
