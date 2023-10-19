import numpy as np
import argparse
from db_config import topics_collection, embeddings_collection, cleaned_topics_collection, cluster_results_collection
from models.utils import get_cluster_centers
from models.affinity import deploy_model
from dotenv import load_dotenv
import boto3

load_dotenv()

def cluster_topics():
    # Fetch topic embeddings from MongoDB
    topic_embedding_cache = {entry['topic']: np.array(entry['embedding']) for entry in embeddings_collection.find({})}
    topic_embeddings = np.array(list(topic_embedding_cache.values()))

    # Save training data to S3
    np.save("topic_embeddings.npy", topic_embeddings)
    s3 = boto3.client('s3')
    s3.upload_file('topic_embeddings.npy', 'mercury-affinity-modeling', 'topic_embeddings.npy')
    s3_training_data_uri = f"s3://mercury-affinity-modeling/topic_embeddings.npy"

    deploy_model(s3_training_data_uri)

def clean_topics():
    # Fetch topics and their embeddings from MongoDB
    topic_embedding_cache = {entry['topic']: np.array(entry['embedding']) for entry in embeddings_collection.find({})}
    all_topics = list(topic_embedding_cache.keys())

    # Fetch content IDs and their associated topics
    stored_data = list(topics_collection.find({}))

    # Get cluster centers
    exemplars_indices, labels = get_cluster_centers()
    exemplars = [all_topics[index] for index in exemplars_indices]

    topic_to_exemplar = {topic: exemplars[label] for topic, label in zip(all_topics, labels)}

    # Prepare data for MongoDB insertion
    cleaned_data = [
        {
            'content_id': content['content_id'], 
            'topics': [
                topic_to_exemplar[topic] for topic in content['topics']
            ]
        } 
        for content in stored_data
    ]
    
    # Save the cleaned topics into MongoDB
    cleaned_topics_collection.delete_many({})
    cleaned_topics_collection.insert_many(cleaned_data)    

    save_clusters_to_db({label: [all_topics[i] for i, lbl in enumerate(labels) if lbl == label] for label in set(labels)}, exemplars)

def save_clusters_to_db(cluster_to_topic, exemplars):
    cluster_data = []
    
    for label, topics in sorted(cluster_to_topic.items()):
        cluster_entry = {}
        cluster_entry["cluster_name"] = f"Cluster {label}"
        cluster_entry["exemplar"] = exemplars[label]
        cluster_entry["topics"] = topics
        cluster_data.append(cluster_entry)
    
    # Save the data to MongoDB
    cluster_results_collection.insert_many(cluster_data)

if __name__ == "__main__":    
    parser = argparse.ArgumentParser(description='Choose a batch process to run.')
    parser.add_argument('-p', '--process', type=str, help='process to run', required=True)
    
    args = parser.parse_args()
    
    if args.process == 'cluster':
        cluster_topics()
    elif args.process == 'clean':
        clean_topics()
    else:
        print(f"Invalid method: {args.process}. Available processes: 'cluster', 'clean'")