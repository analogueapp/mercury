import boto3
from sagemaker import Session
from sagemaker.huggingface.model import HuggingFaceModel
from models.utils import embedding_endpoint_name, embedding_model_name, delete_existing_model, delete_existing_endpoint, delete_existing_endpoint_config
from dotenv import load_dotenv
import os

load_dotenv()
role = os.getenv("SAGEMAKER_ROLE")

boto_session = boto3.Session()
sagemaker_session = Session(boto_session)

hub = {
  'HF_MODEL_ID':'sentence-transformers/all-MiniLM-L12-v2',
  'HF_TASK':'feature-extraction',
}

def deploy_model():
    delete_existing_model(embedding_model_name)
    delete_existing_endpoint(embedding_endpoint_name)
    delete_existing_endpoint_config(embedding_endpoint_name)

    huggingface_model = HuggingFaceModel(
        env=hub,
        role=role,        
        transformers_version="4.26",
        pytorch_version="1.13",        
        py_version='py39',
        name=embedding_model_name
    )

    predictor = huggingface_model.deploy(
        initial_instance_count=1,
        endpoint_name=embedding_endpoint_name,
        instance_type="ml.c5.large"
    )

    print(f"Model deployed at endpoint: {predictor.endpoint_name}")


if __name__ == "__main__":
    deploy_model()