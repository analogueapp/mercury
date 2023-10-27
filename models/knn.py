import boto3
from sagemaker import Session, KNN
from models.utils import knn_endpoint_name, delete_existing_endpoint
from dotenv import load_dotenv
import os

load_dotenv()
role = os.getenv("SAGEMAKER_ROLE")

boto_session = boto3.Session()
sagemaker_session = Session(boto_session)

def deploy_knn(topic_embeddings, labels):    
    delete_existing_endpoint(knn_endpoint_name)     
    
    knn = KNN(role=role,
              train_instance_count=1,
              train_instance_type='ml.m5.xlarge',
              k=1,
              predictor_type='classifier',
              sample_size=topic_embeddings.shape[0],
              output_path='s3://mercury-affinity-modeling/models/',
              code_location='s3://mercury-affinity-modeling/cache')
        
    knn_record_set = knn.record_set(topic_embeddings, labels=labels)
    knn.fit(knn_record_set)
    
    # Deploy the model to an endpoint
    predictor = knn.deploy(instance_type='ml.m5.xlarge', initial_instance_count=1, endpoint_name=knn_endpoint_name)
    print(f"Model deployed at endpoint: {predictor.endpoint_name}")

    return predictor