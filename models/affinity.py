import boto3
from sagemaker import Session
from sagemaker.sklearn import SKLearn
from sagemaker.serverless import ServerlessInferenceConfig
from models.utils import affinity_endpoint_name, delete_existing_endpoint, delete_existing_endpoint_config
from dotenv import load_dotenv
import os

load_dotenv()
role = os.getenv("SAGEMAKER_ROLE")

boto_session = boto3.Session()
sagemaker_session = Session(boto_session)

def deploy_model(training_data_uri):    
    delete_existing_endpoint(affinity_endpoint_name)
    delete_existing_endpoint_config(affinity_endpoint_name)
    
    sklearn_estimator = SKLearn(
        entry_point='train.py',
        role=role,
        source_dir='models/',
        instance_count=1,
        instance_type='ml.m5.4xlarge',
        framework_version='1.2-1'        
    )
    sklearn_estimator.fit({'train': training_data_uri})

    serverless_config = ServerlessInferenceConfig(
        memory_size_in_mb=1024, max_concurrency=5,
    )

    # Deploy the model
    predictor = sklearn_estimator.deploy(serverless_inference_config=serverless_config, endpoint_name=affinity_endpoint_name)

    print(f"Model deployed at endpoint: {predictor.endpoint_name}")    