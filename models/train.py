import os
import io
import numpy as np
from sklearn.cluster import AffinityPropagation
import joblib

def train():
    # Load data from the location specified by SageMaker
    input_dir = os.environ['SM_CHANNEL_TRAIN']
    topic_embeddings = np.load(os.path.join(input_dir, 'topic_embeddings.npy'))    

    # Use Affinity Propagation for clustering
    clusterer = AffinityPropagation(max_iter=1000)
    clusterer.fit(topic_embeddings)

    # Save the trained model
    model_dir = os.environ['SM_MODEL_DIR']
    joblib.dump(clusterer, os.path.join(model_dir, 'affinity_model.pkl'))

def model_fn(model_dir):
    """Load the model from disk."""
    clusterer = joblib.load(os.path.join(model_dir, 'affinity_model.pkl'))
    return clusterer

def input_fn(request_body, request_content_type):
    if request_content_type == 'application/x-npy':        
        with io.BytesIO(request_body) as buffer:
            data = np.load(buffer, allow_pickle=True)
        if data.size == 1 and data[0] == -999999:
            return {"request": "get_cluster_centers"}
        else:
            return data
    else:
        raise ValueError(f"Unsupported content type: {request_content_type}")

def output_fn(prediction_output, accept):
    """Format prediction output."""
    if accept == 'application/x-npy':        
        with io.BytesIO() as buffer:
            if isinstance(prediction_output, dict):
                # If it's a dictionary, convert to a numpy array                
                np.save(buffer, np.array(prediction_output))
            else:
                # If it's already a numpy array, save directly
                np.save(buffer, prediction_output)
            return buffer.getvalue(), accept
    else:
        raise ValueError(f"Unsupported accept type: {accept}")


def predict_fn(input_data, model):
    if isinstance(input_data, dict) and input_data.get("request") == "get_cluster_centers":        
        return {
            'cluster_centers_indices': model.cluster_centers_indices_.tolist(),
            'labels': model.labels_.tolist()
        }
    return model.predict(input_data)



if __name__ == '__main__':
    train()
