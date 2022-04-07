import boto3
import json

runtime= boto3.client('runtime.sagemaker')


def lambda_handler(event, context):

    payload = event.get("data")

    response = runtime.invoke_endpoint(EndpointName='cc-fraud',
                                       ContentType='text/csv',
                                       Body=payload)

    result = json.loads(response['Body'].read().decode())

    return result