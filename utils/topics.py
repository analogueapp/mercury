
import re
import os
import openai
from collections import defaultdict
from utils.db_config import topics_collection, topic_content_mapping_collection, cluster_results_collection
from dotenv import load_dotenv
import tensorflow_hub as hub
import sentencepiece as spm
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

load_dotenv()

openai.api_key = os.getenv("OPENAI_KEY")
use_lite = hub.load("https://tfhub.dev/google/universal-sentence-encoder-lite/2")

with tf.Session() as sess:
  spm_path = sess.run(use_lite(signature="spm_path"))

sp = spm.SentencePieceProcessor()
with tf.io.gfile.GFile(spm_path, mode="rb") as f:
  sp.LoadFromSerializedProto(f.read())
print("SentencePiece model loaded at {}.".format(spm_path))

def process_to_IDs_in_sparse_format(sp, sentences):
    # This function converts sentences to ids using SentencePiece
    ids = [sp.EncodeAsIds(x) for x in sentences]
    max_len = max(len(x) for x in ids)
    dense_shape=(len(ids), max_len)
    values=[item for sublist in ids for item in sublist]
    indices=[[row,col] for row in range(len(ids)) for col in range(len(ids[row]))]
    return (values, indices, dense_shape)

def get_embedding(texts):
    if isinstance(texts, str):
        texts = [texts]
    
    values, indices, dense_shape = process_to_IDs_in_sparse_format(sp_model, texts)
    embeddings = use_lite(values=values, indices=indices, dense_shape=dense_shape)
    
    return embeddings['default'].numpy()

def generate_topics(medium, title, specifier):    
    prompt_text = (f"List 15 genres or topics for the {medium} '{title}' {specifier}. " 
                   f"These topics should vary in specificity, such that they are useful to a recommender engine. "
                   f"Simply print a list with the titles of these topics. ")                   

    # Make the API call
    completion = openai.Completion.create(model="gpt-3.5-turbo-instruct", prompt=prompt_text, max_tokens=3800, temperature=0.6, n=1)
                
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