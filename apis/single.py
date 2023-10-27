import numpy as np
from db_config import cluster_results_collection
from helpers.generate_topics import get_embedding, generate_topics
from models.utils import affinity_predictor

def enrich_single(medium, title, specifier):    
    clusters = list(cluster_results_collection.find({}))
    content_topics = generate_topics(medium, title, specifier)
    if not content_topics or len(content_topics) == 0:
        return []

    topic_embeddings = [get_embedding(topic) for topic in content_topics]
    
    # Use SageMaker hosted model to predict in batch
    cluster_labels = affinity_predictor.predict(np.array(topic_embeddings))
    
    enriched_topics = [clusters[label]["exemplar"] for label in cluster_labels]
    
    return enriched_topics