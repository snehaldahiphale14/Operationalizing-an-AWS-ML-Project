import base64
import logging
import json
import boto3

# import numpy
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

print("Loading Lambda function")

runtime = boto3.Session().client("sagemaker-runtime")
# Set this to the name of your MULTI-INSTANCE endpoint (printed by the notebook,
# or SageMaker AI > Inference > Endpoints).
endpoint_name = "pytorch-inference-2026-10-07-16-50-13-138"


def lambda_handler(event, context):

    # x=event['content']
    # aa=x.encode('ascii')
    # bs=base64.b64decode(aa)
    print("Context:::", context)
    print("EventType::", type(event))
    bs = event
    runtime = boto3.Session().client("sagemaker-runtime")

    response = runtime.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType="application/json",
        Accept="application/json",
        # Body=bytearray(x)
        Body=json.dumps(bs),
    )

    result = response["Body"].read().decode("utf-8")
    sss = json.loads(result)

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain", "Access-Control-Allow-Origin": "*"},
        "type-result": str(type(result)),
        "Content-Type-In": str(context),
        "body": json.dumps(sss),
        #'updated_result':str(updated_result)
    }
