import numpy as np
import json
import argparse
from db_config import embeddings_collection, cluster_results_collection, sections_collection
from models.utils import get_cluster_centers
from models.affinity import deploy_affinity
from models.knn import deploy_knn
from helpers.generate_topics import get_embedding
from dotenv import load_dotenv
import boto3

load_dotenv()

def load_sections():
    with open('sections.json', 'r') as f:
        sections = json.load(f)
    return sections

def cluster_topics():
    thresh = 75
    while embeddings_collection.count_documents({}) > 19000:
        condition = {"$expr": {"$gt": [{"$strLenCP": "$topic"}, thresh]}}
        embeddings_collection.delete_many(condition)
        thresh -= 1

    topic_embedding_cache = {entry['topic']: np.array(entry['embedding']) for entry in embeddings_collection.find({})}
    topic_embeddings = np.array(list(topic_embedding_cache.values()))

    # Save training data to S3
    np.save("topic_embeddings.npy", topic_embeddings)
    s3 = boto3.client('s3')
    s3.upload_file('topic_embeddings.npy', 'mercury-affinity-modeling', 'topic_embeddings.npy')
    s3_training_data_uri = f"s3://mercury-affinity-modeling/topic_embeddings.npy"

    predictor = deploy_affinity(s3_training_data_uri)
    clean_topics(predictor)

def clean_topics(predictor=None):
    # Fetch topics and their embeddings from MongoDB
    topic_embedding_cache = {entry['topic']: np.array(entry['embedding']) for entry in embeddings_collection.find({})}
    all_topics = list(topic_embedding_cache.keys())

    # Get cluster centers
    exemplars_indices, labels = get_cluster_centers()
    exemplars = [all_topics[index] for index in exemplars_indices]   

    save_clusters_to_db({label: [all_topics[i] for i, lbl in enumerate(labels) if lbl == label] for label in set(labels)}, exemplars)
    map_tags_to_topics(exemplars, exemplars_indices)

def save_clusters_to_db(cluster_to_topic, exemplars):    
    cluster_data = []
    
    for label, topics in sorted(cluster_to_topic.items()):
        cluster_entry = {}
        cluster_entry["cluster_name"] = f"Cluster {label}"
        cluster_entry["exemplar"] = exemplars[label]
        cluster_entry["topics"] = topics
        cluster_data.append(cluster_entry)
    
    # Save the data to MongoDB
    cluster_results_collection.delete_many({})
    cluster_results_collection.insert_many(cluster_data)

def map_tags_to_topics(exemplars, exemplar_indices):
    # Load sections and get embeddings for exemplars and topics
    sections = load_sections()
    tag_embeddings = [entry['embedding'] for entry in embeddings_collection.find({})]

    topic_embeddings = []
    labels = []
    label_mapping = {}  # Mapping from integer labels to string labels
    label_counter = 0
    for section_name, topics in sections.items():
        for topic_name in topics.keys():
            topic_embeddings.append(get_embedding(topic_name))
            labels.append(label_counter)
            label_mapping[label_counter] = f"{section_name}_{topic_name}"
            label_counter += 1

    # Convert topic_embeddings and labels to NumPy arrays
    topic_embeddings = np.array(topic_embeddings)
    labels = np.array(labels)
    exemplar_embeddings = np.array([tag_embeddings[i] for i in exemplar_indices])

    predictor = deploy_knn(topic_embeddings, labels)
    result = predictor.predict(exemplar_embeddings)

    predictor.delete_endpoint()  # Clean up

    # Organize results
    for i, record in enumerate(result):
        # Get the string label from the mapping using the predicted integer label
        section_name, topic_name = label_mapping[int(record.label['predicted_label'].float64_tensor.values[0])].split('_')
        # Add the exemplar to the corresponding topic
        sections[section_name][topic_name].setdefault('tags', []).append(exemplars[i])

    sections_data = []
    for section_name, topics in sections.items():
        for topic_name, topic_data in topics.items():
            entry = {
                "section": section_name,
                "topic": topic_name,
                "tags": topic_data.get('tags', [])
            }
            sections_data.append(entry)

    # Save the data to MongoDB
    sections_collection.delete_many({})
    sections_collection.insert_many(sections_data)


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