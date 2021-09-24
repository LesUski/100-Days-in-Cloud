import boto3
import json

def detect_labels(bucket, key, max_labels=10, min_confidence=90, region="REGION"):
        rekognition = boto3.client("rekognition", region)
        response = rekognition.detect_labels(
               Image={
                       "S3Object": {
                               "Bucket": bucket,
                               "Name": key,
                       }
               },
               MaxLabels=max_labels,
               MinConfidence=min_confidence,
        )
        return response['Labels']

def lambda_handler(event, context):
    results = ''
    mqtt = boto3.client('iot-data', region_name='REGION')

    bucket_name = 'esp32-rekognition_YOUR_ACCOUNT_ID'
    file_name = str(event['payload'])

    for label in detect_labels(bucket_name, file_name):
        if (float(label['Confidence']) > 90):
                results += (label['Name'] + ';')


    response = mqtt.publish(
            topic='esp32/sub/data',
            qos=0,
            payload=results
        )
 