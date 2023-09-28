import numpy as np
from collections import defaultdict
from utils.db_config import topics_collection, embeddings_collection, cleaned_topics_collection
from utils.topics import get_embedding, get_representative_topic_by_embedding, generate_topics, save_clusters_to_db, map_topics_to_contents
import hdbscan

def generate_and_store_topics(batch):
    # Initialize an empty list for batch data
    batch_data = []
    
    # Fetch topics for each content and store in the batch data
    for content in batch:
        topics = generate_topics(content['medium'], content['title'], content['specifier'])
        batch_data.append({'content_id': content['id'], 'topics': topics})
    
    # Insert the batch data into MongoDB
    topics_collection.insert_many(batch_data)
    
    # Fetch unique topics from the entire batch
    unique_batch_topics = set(topic for content in batch_data for topic in content['topics'])
    
    # Query MongoDB to find out which topics we've already cached embeddings for
    seen_topics = {doc['topic'] for doc in embeddings_collection.find({}, {'_id': 0, 'topic': 1})}
    topics_to_embed = [topic for topic in unique_batch_topics if topic not in seen_topics]
    
    embeddings = get_embedding(topics_to_embed)
    # Insert new topic embeddings into MongoDB
    for topic, embedding in zip(topics_to_embed, embeddings):
        embeddings_collection.insert_one({'topic': topic, 'embedding': embedding.tolist()})  # Convert numpy array to list

def clean_and_cluster_topics():
    # Fetch topics and embeddings from MongoDB
    stored_data = list(topics_collection.find({}))
    topic_embedding_cache = {entry['topic']: np.array(entry['embedding']) for entry in embeddings_collection.find({})}

    all_topics = list(topic_embedding_cache.keys())
    topic_embeddings = np.array([topic_embedding_cache[topic] for topic in all_topics])

    clusterer = hdbscan.HDBSCAN(min_samples=2, metric='euclidean', cluster_selection_method='eom')
    labels = clusterer.fit_predict(topic_embeddings)

    cluster_to_topic = defaultdict(list)
    for i, label in enumerate(labels):
        cluster_to_topic[label].append(all_topics[i])

    topic_to_embedding = {topic: embedding for topic, embedding in zip(all_topics, topic_embeddings)}
    representative_topics = {}
    for label, topics in cluster_to_topic.items():
        representative_topics[label] = get_representative_topic_by_embedding(topics, topic_to_embedding)

    save_clusters_to_db(cluster_to_topic, representative_topics, topic_to_embedding)

    topic_to_label = {topic: label for topic, label in zip(all_topics, labels)}

    # Prepare data for MongoDB insertion
    cleaned_data = [
        {
            'content_id': content['content_id'], 
            'topics': [
                representative_topics[topic_to_label[topic]] if topic_to_label[topic] != -1 else topic 
                for topic in content['topics']
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
