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
from utils.enrichment import enrich
from utils.request import send_request, handle_params
from utils.search import search
from utils.get_twitter import get_twitter
from utils.get_main import get_main
from apis.google_books import fetch_authors
from apis.batch import generate_and_store_topics
from apis.single import enrich_single_book
from apis.goodreads import get_goodreads_isbn

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
    params_string = handle_params(all_params)

    if "twitter.com" in params_string:
        return get_twitter(params_string)

    request_object = send_request(all_params)

    if isinstance(request_object, dict):
        return jsonify(request_object)

    get_data = get_main(request_object, params_string)

    return jsonify(get_data)


@app.route("/enrich")
def enrichment():
    URL = request.args.get("url")

    enriched_data = enrich(URL)

    return jsonify(enriched_data)


@app.route("/authors")
def authors_enrichment():
    isbn = request.args.get("isbn")
    enriched_authors = fetch_authors(isbn)

    return jsonify(authors=enriched_authors)


@app.route("/topics")
def topic_enrichment():
    title = request.args.get("title")
    authors = request.args.get("authors")
    enriched_topics = enrich_single_book(title, authors)

    return jsonify(topics=enriched_topics)

@app.route("/batch_topics", methods=["POST"])
def batch_enrichment():
    data = request.get_json()
    books = data.get("books")
    if not books:
        return jsonify({"error": "No books data provided"}), 400
    
    generate_and_store_topics(books)
    
    return jsonify({"message": "Successfully processed books"}), 200

@app.route("/goodreads/isbn")
def goodreads_isbn_endpoint():
    goodreads_id = request.args.get("id")
    isbn_data = get_goodreads_isbn(goodreads_id)

    return jsonify(isbn_data)


@app.route("/api/search")
def search_endpoint():
    query = request.args.get("query")
    medium = request.args.get("medium")

    results = search(query, medium)

    return jsonify(results)


if __name__ == "__main__":
    app.run()
