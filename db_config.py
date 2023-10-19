import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("MONGODB_URI")
client = MongoClient(uri)
db = client["mercury"]

env = os.getenv("FLASK_ENV")

essential_prefix="prod"
if env == "development":
    collection_prefix = os.getenv("DEV_USER")

# MongoDB collections with environment-specific names
topics_collection = db["topics_storage"]
embeddings_collection = db["topic_embedding_cache"]
cluster_results_collection = db["cluster_results"]
cleaned_topics_collection = db["cleaned_topics_storage"]
essential_contents_collection = db[f"{essential_prefix}_essential_contents"]

def setup_database_indexes():
    # Creating indexes for topics_collection
    topics_collection.create_index("id")
    
    # Creating indexes for embeddings_collection
    embeddings_collection.create_index("topic")
    
    # Creating indexes for cluster_results_collection
    cluster_results_collection.create_index("cluster_name")
    cluster_results_collection.create_index("representative_topic.topic")
    
    # Creating indexes for cleaned_topics_collection
    cleaned_topics_collection.create_index("id")

setup_database_indexes()
