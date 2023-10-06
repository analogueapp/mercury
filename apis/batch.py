import numpy as np
from collections import defaultdict
from utils.db_config import topics_collection, embeddings_collection, cleaned_topics_collection, model_collection, collection_prefix, fs
from utils.topics import get_embedding, generate_topics, save_clusters_to_db, map_topics_to_contents
from sklearn.cluster import AffinityPropagation
import joblib
import io
import datetime

def generate_and_store_topics(batch):
    batch_data = []
    unique_batch_topics = set()
    
    for content in batch:
        topics = generate_topics(content['medium'], content['title'], content['specifier'])
        batch_data.append({'content_id': content['id'], 'topics': topics})
        unique_batch_topics.update(topics)
    
    topics_collection.insert_many(batch_data)
    
    seen_topics = {doc['topic'] for doc in embeddings_collection.find({}, {'_id': 0, 'topic': 1})}
    topics_to_embed = list(unique_batch_topics - seen_topics)
    
    if topics_to_embed:
        embeddings = get_embedding(topics_to_embed)
        bulk_data = [{'topic': topic, 'embedding': embedding.tolist()} for topic, embedding in zip(topics_to_embed, embeddings)]
        embeddings_collection.insert_many(bulk_data)


def clean_and_cluster_topics():
    # Fetch topics and embeddings from MongoDB
    stored_data = list(topics_collection.find({}))
    topic_embedding_cache = {entry['topic']: np.array(entry['embedding']) for entry in embeddings_collection.find({})}

    all_topics = list(topic_embedding_cache.keys())
    topic_embeddings = np.array([topic_embedding_cache[topic] for topic in all_topics])

    # Use Affinity Propagation for clustering
    clusterer = AffinityPropagation(random_state=42, max_iter=500)
    labels = clusterer.fit_predict(topic_embeddings)
    exemplars = [all_topics[index] for index in clusterer.cluster_centers_indices_]

    cluster_to_topic = defaultdict(list)
    for i, label in enumerate(labels):
        cluster_to_topic[label].append(all_topics[i])
    
    save_clusters_to_db(cluster_to_topic, exemplars)

    buffer = io.BytesIO()
    joblib.dump(clusterer, buffer)
    buffer.seek(0)
    model_id = fs.put(buffer.getvalue())
    metadata = {
        "model_id": model_id,  # Store the model_id in the metadata
        "model_type": "affinity_propagation",
        "environment": collection_prefix,
        "date_created": datetime.datetime.utcnow()
    }
    model_collection.insert_one(metadata)

    topic_to_label = {topic: label for topic, label in zip(all_topics, labels)}

    # Prepare data for MongoDB insertion
    cleaned_data = [
        {
            'content_id': content['content_id'], 
            'topics': [
                exemplars[topic_to_label[topic]] for topic in content['topics']
            ]
        } 
        for content in stored_data
    ]
    
    # Save the cleaned topics into MongoDB
    cleaned_topics_collection.delete_many({})
    cleaned_topics_collection.insert_many(cleaned_data)

if __name__ == "__main__":
    map_topics_to_contents()
    clean_and_cluster_topics()
