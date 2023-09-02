from pymongo import MongoClient

client = MongoClient("mongodb+srv://analogue:gumption@mercury.3pv3bqd.mongodb.net/?retryWrites=true&w=majority")  # Adjust as needed
db = client["mercury"]

# MongoDB collections
topics_collection = db.topics_storage
topic_book_mapping_collection = db.topic_book_mapping
embeddings_collection = db.topic_embedding_cache
cluster_results_collection = db.cluster_results
cleaned_topics_collection = db.cleaned_topics_storage

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