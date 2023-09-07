import os
from pymongo import MongoClient

uri = os.getenv("MONGODB_URI")
client = MongoClient(uri)
db = client["mercury"]

env = os.getenv("FLASK_ENV")

collection_prefix=""
if env == "development":
    collection_prefix = "dev_"
else:
    collection_prefix = "prod_"

# MongoDB collections with environment-specific names
topics_collection = db[f"{collection_prefix}topics_storage"]
topic_book_mapping_collection = db[f"{collection_prefix}topic_book_mapping"]
embeddings_collection = db[f"{collection_prefix}topic_embedding_cache"]
cluster_results_collection = db[f"{collection_prefix}cluster_results"]
cleaned_topics_collection = db[f"{collection_prefix}cleaned_topics_storage"]

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
