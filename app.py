import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from flask import Flask, request, jsonify
from flask_cors import CORS

from dotenv import load_dotenv
import os

load_dotenv()

from apis.authors import fetch_author
from apis.batch import generate_and_store_topics
from apis.single import enrich_single
from apis.creators import get_creator_bio
from apis.descriptions import get_description

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


@app.route("/author")
def author_enrichment():
    name = request.args.get("name")
    work = request.args.get("work")
    enriched_author = fetch_author(name, work)

    return jsonify(creator=enriched_author)


@app.route("/creator")
def creator_enrichment():
    name = request.args.get("name")
    work = request.args.get("work")
    enriched_creator = get_creator_bio(name, work)

    return jsonify(creator=enriched_creator)


@app.route("/description")
def description_enrichment():
    work = request.args.get("work")
    creatorList = request.args.getlist("creators")
    enriched_description = get_description(work, creatorList)

    return jsonify(description=enriched_description)


@app.route("/topics")
def topic_enrichment():
    medium = request.args.get("medium")
    title = request.args.get("title")
    specifier = request.args.get("specifier")
    enriched_topics = enrich_single(medium, title, specifier)

    return jsonify(topics=enriched_topics)


@app.route("/batch_topics", methods=["POST"])
def batch_enrichment():
    data = request.get_json()
    batch = data.get("batch")
    if not batch:
        return jsonify({"error": "No batch data provided"}), 400

    generate_and_store_topics(batch)

    return jsonify({"message": "Successfully processed contents"}), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(port=port)