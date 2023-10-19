from db_config import topics_collection, embeddings_collection
from helpers.generate_topics import get_embedding, generate_topics

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
        embeddings = [get_embedding(topic) for topic in topics_to_embed]
        bulk_data = [{'topic': topic, 'embedding': embedding} for topic, embedding in zip(topics_to_embed, embeddings)]
        embeddings_collection.insert_many(bulk_data)
