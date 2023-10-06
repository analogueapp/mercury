from utils.db_config import cluster_results_collection, model_collection, collection_prefix, fs
from utils.topics import get_embedding, generate_topics
import joblib
import io

# Load the Affinity Propagation model from MongoDB
def load_model_from_db():
    model_metadata = model_collection.find_one({"environment": collection_prefix})
    if model_metadata:
        model_id = model_metadata["model_id"]  # Use the model_id from the metadata
        model_data = fs.get(model_id).read()
        buffer = io.BytesIO(model_data)
        model = joblib.load(buffer)
        return model
    else:
        raise Exception("Model not found in database")

def enrich_single(medium, title, specifier):
    affinity_model = load_model_from_db()
    clusters = list(cluster_results_collection.find({}))
    content_topics = generate_topics(medium, title, specifier)    

    enriched_topics = []

    for topic in content_topics:    
        topic_embedding = get_embedding(topic)
        cluster_label = affinity_model.predict(topic_embedding.reshape(1, -1))[0]
        exemplar = clusters[cluster_label]["exemplar"]
        enriched_topics.append(exemplar)
    
    return enriched_topics