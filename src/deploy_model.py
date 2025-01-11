import sagemaker
from sagemaker.sklearn import SKLearn

def deploy_model(model_path, role, bucket_name, endpoint_name):
    """Deploys the model to a SageMaker endpoint."""
    session = sagemaker.Session()

    # Upload model artifacts to S3
    model_artifact = session.upload_data(model_path, bucket=bucket_name, key_prefix="model-artifacts")

    # Deploy the model
    sklearn = SKLearn(
        entry_point="train.py",
        role=role,
        instance_type="ml.m5.large",
        framework_version="0.23-1",
        py_version="py3",
        model_uri=model_artifact
    )
    predictor = sklearn.deploy(instance_type="ml.m5.large", endpoint_name=endpoint_name)
    return predictor