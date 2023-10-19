import boto3
import numpy as np
from sagemaker import Session
from sagemaker.sklearn.model import SKLearnPredictor
from sagemaker.huggingface.model import HuggingFacePredictor
from dotenv import load_dotenv
import os

load_dotenv()

affinity_endpoint_name = "affinity-propagation-endpoint"

embedding_endpoint_name = "sbert-endpoint"
embedding_model_name = "sbert-model"

# Global Boto3 session
boto_session = boto3.Session()
sagemaker_session = Session(boto_session)

# Global predictors
affinity_predictor = SKLearnPredictor(
    endpoint_name=affinity_endpoint_name,
    sagemaker_session=sagemaker_session
)

embedding_predictor = HuggingFacePredictor(
    endpoint_name=embedding_endpoint_name,
    sagemaker_session=sagemaker_session
)

def get_cluster_centers():
    """Invoke the endpoint to get cluster_centers_indices_ and labels."""
    cluster_request = np.array([-999999])  # Some special value
    response = affinity_predictor.predict(cluster_request).item() 
    cluster_centers_indices = response['cluster_centers_indices']
    labels = response['labels']
    return cluster_centers_indices, labels

def delete_existing_model(model_name):
    try:
        sagemaker_session.delete_model(model_name)
        print(f"Deleted existing model: {model_name}")
    except:
        print(f"No existing model named {model_name} found.")

def delete_existing_endpoint(endpoint_name):
    try:
        sagemaker_session.delete_endpoint(endpoint_name)
        print(f"Deleted existing endpoint: {endpoint_name}")
    except:
        print(f"No existing endpoint named {endpoint_name} found.")

def delete_existing_endpoint_config(endpoint_config_name):
    try:
        sagemaker_session.delete_endpoint_config(endpoint_config_name)
        print(f"Deleted existing endpoint configuration: {endpoint_config_name}")
    except:
        print(f"No existing endpoint configuration named {endpoint_config_name} found.")