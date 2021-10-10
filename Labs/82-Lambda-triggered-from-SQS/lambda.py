import json

import boto3

def lambda_handler(event, context):

    sqs_msg = json.loads(event['Records'][0]['body'])

    print("SQS Message : ", sqs_msg)

    

    bucket_name = "mysqslambda2"

    try:

        s3Client = boto3.client("s3", region_name= "us-east-1")

        Response = s3Client.put_object(Bucket= bucket_name, Key= "Message.json", Body= json.dumps(sqs_msg))

        print("S3 upload success !")

        return {

            "status" : 200,

            "body" : "S3 upload success"

        }

    except Exception as e:

        print("Client connection to S3 failed because ", e)

        return{

            "status" : 500,

            "body" : "S3 upload failed"

        }