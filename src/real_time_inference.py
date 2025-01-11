import boto3
import json

def invoke_endpoint(endpoint_name, payload):
    """Sends requests to the deployed endpoint for predictions."""
    runtime = boto3.client('sagemaker-runtime')
    response = runtime.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType='application/json',
        Body=json.dumps(payload)
    )
    response_body = response['Body'].read().decode('utf-8')
    return json.loads(response_body)
