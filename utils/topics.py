import re
import os
import openai
from collections import defaultdict
from utils.db_config import topics_collection, topic_content_mapping_collection, cluster_results_collection
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()

openai.api_key = os.getenv("OPENAI_KEY")

class LazySentenceTransformer:
    def __init__(self, model_name):
        self.model_name = model_name
        self._model = None

    @property
    def model(self):
        if self._model is None:
            self._model = SentenceTransformer(self.model_name)
        return self._model

    def encode(self, texts):
        return self.model.encode(texts)
    
model = LazySentenceTransformer('all-MiniLM-L12-v2')

def get_embedding(texts):
    return model.encode(texts)

def generate_topics(medium, title, specifier):    
    prompt_text = (f"List 15 genres or topics for the {medium} '{title}' {specifier}. " 
                   f"These topics should vary in specificity, such that they are useful to a recommender engine. "
                   f"Simply print a list with the titles of these topics. ")                   

    # Make the API call
    completion = openai.Completion.create(model="gpt-3.5-turbo-instruct", prompt=prompt_text, max_tokens=3000, temperature=0.6, n=1)
                
    # Extracting the response and splitting into individual topics    
    raw_text = completion.choices[0].text.strip()    
    topics = re.findall(r'\d+\.\s*(.*?)(?=\n\d+|$)', raw_text)    
            
    # Strip trailing spaces around each parsed topic
    topics = [topic.strip() for topic in topics]

    return topics

def map_topics_to_contents():
    topic_to_contents = defaultdict(list)

    for record in topics_collection.find({}, {'content_id': 1, 'topics': 1}):
        content_id = record['content_id']
        for topic in record['topics']:
            topic_to_contents[topic].append(content_id)

    output_data = [{"topic": key, "contents": value} for key, value in topic_to_contents.items()]
    topic_content_mapping_collection.delete_many({})
    topic_content_mapping_collection.insert_many(output_data)

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

## For testing purposes
# if __name__ == "__main__":
#     generate_topics("book", "The Pearl", "by John Steinbeck")
