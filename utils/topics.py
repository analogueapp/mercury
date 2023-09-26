
import re
import os
import openai
import numpy as np
from sklearn.metrics import pairwise_distances_argmin_min
from utils.db_config import topics_collection, topic_book_mapping_collection, cluster_results_collection
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_KEY")
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def get_embedding(texts):
    """Get the embeddings for a list of texts using Sentence Transformers."""
    return model.encode(texts)

def generate_book_topics(title, authors):
    # Convert the list of authors into a comma-separated string
    author_string = ", ".join(authors)
    
    # Construct the prompt with specific delimiters for better extraction
    prompt_text = (f"List 20 genres or topics for '{title}' by {author_string}. "
               f"Avoid overly specific or overly general labels. For example, use 'Detective Stories' instead of "
               f"'John Smith's London Mysteries' or just 'Fiction'.")

    # Make the API call
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",        
        messages=[{"role": "user", "content": prompt_text}],        
        n=1,
        temperature=0.6  # lower temperature to make output more deterministic
    )    
    
    # Extracting the response and splitting into individual topics    
    raw_text = response.choices[0].message.content.strip()
    topics = re.findall(r'\d+\.\s*(.*?)(?=\n\d+|$)', raw_text)
    
    # Extract the token usage from the response
    tokens_used = response['usage']
    return topics

def map_topics_to_books():
    # Create a dictionary to map each topic to a list of book IDs
    topic_to_books = {}

    # Fetch all the records from the MongoDB topics collection
    stored_data = list(topics_collection.find({}))

    # Iterate over each book record
    for record in stored_data:
        book_id = record['content_id']
        topics = record['topics']  # Assuming 'topics' is the key for the list of topics in MongoDB

        for topic in topics:
            if topic not in topic_to_books:
                topic_to_books[topic] = []
            topic_to_books[topic].append(book_id)

    # Convert the dictionary to the desired output format
    output_data = [{"topic": key, "books": value} for key, value in topic_to_books.items()]

    # Clear out any existing data in the collection to ensure a fresh mapping is created
    topic_book_mapping_collection.delete_many({})

    # Insert the new mapping into the MongoDB collection
    topic_book_mapping_collection.insert_many(output_data)

def save_clusters_to_db(cluster_to_topic, representative_topics, topic_to_embedding):
    cluster_data = []
    
    for label, topics in sorted(cluster_to_topic.items()):
        cluster_entry = {}
        if label == -1:
            cluster_entry["cluster_name"] = "Unique"
        else:
            cluster_entry["cluster_name"] = f"Cluster {label}"
            cluster_entry["representative_topic"] = {
                "topic": representative_topics[label],
                "embedding": topic_to_embedding[representative_topics[label]].tolist()
            }
        cluster_entry["related_topics"] = topics
        cluster_data.append(cluster_entry)
    
    # Save the data to MongoDB
    cluster_results_collection.insert_many(cluster_data)

def get_representative_topic_by_embedding(cluster, topic_to_embedding):
    cluster_embeddings = [topic_to_embedding[topic] for topic in cluster]
    centroid = np.mean(cluster_embeddings, axis=0).reshape(1, -1)
    closest_topic_index, _ = pairwise_distances_argmin_min(centroid, cluster_embeddings)
    return cluster[closest_topic_index[0]]

def find_closest_representative_topic(topic_embedding, representative_data):
    """Find the closest representative topic for a given topic embedding."""
    min_distance = float('inf')
    closest_topic = None
    for cluster_entry in representative_data:
        if "representative_topic" in cluster_entry:
            rep_topic_embedding = np.array(cluster_entry["representative_topic"]["embedding"])
            distance = np.linalg.norm(rep_topic_embedding - topic_embedding)
            if distance < min_distance:
                min_distance = distance
                closest_topic = cluster_entry["representative_topic"]["topic"]
    return closest_topic

def update_representative_data_with_topic(representative_data, cluster_name, novel_topic):
    for cluster in representative_data:
        if cluster["cluster_name"] == cluster_name:
            cluster["related_topics"].append(novel_topic)
            # Update in MongoDB
            cluster_results_collection.update_one({"cluster_name": cluster_name}, {"$push": {"related_topics": novel_topic}})
            break