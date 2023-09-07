from sentence_transformers import util
from utils.db_config import cluster_results_collection
from utils.topics import get_embedding, update_representative_data_with_topic, find_closest_representative_topic, generate_book_topics

def enrich_single_book(title, authors):
    threshold=0.46
    representative_data = list(cluster_results_collection.find({}))
    book_topics = generate_book_topics(title, authors)    

    enriched_topics = []
    directly_matched_original_topics = []

    direct_matches = [cluster for cluster in representative_data if any(topic.lower() in [r_topic.lower() for r_topic in cluster.get("related_topics", [])] for topic in book_topics)]    
    for match in direct_matches:
        if match["cluster_name"] == "Unique":
            matched_topics = [topic for topic in book_topics if topic.lower() in [r_topic.lower() for r_topic in match["related_topics"]]]
            enriched_topics.extend(matched_topics)
            directly_matched_original_topics.extend(matched_topics)
        else:
            enriched_topics.append(match["representative_topic"]["topic"])
            directly_matched_original_topics.extend([topic for topic in book_topics if topic.lower() in [r_topic.lower() for r_topic in match["related_topics"]]])
    
    remaining_topics = list(set(book_topics) - set(directly_matched_original_topics))
    
    for topic in remaining_topics:        
        topic_embedding = get_embedding(topic)
        matched_representative = find_closest_representative_topic(topic_embedding, representative_data)        
        similarity_score = util.cos_sim(topic_embedding, get_embedding(matched_representative)).item()

        if similarity_score >= threshold:
            enriched_topics.append(matched_representative)
            cluster_name = [cluster["cluster_name"] for cluster in representative_data if cluster.get("representative_topic", {}).get("topic") == matched_representative][0]
            update_representative_data_with_topic(representative_data, cluster_name, topic)
    
    return enriched_topics
