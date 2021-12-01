import boto3
from PIL import Image
from io import BytesIO
import json
import urllib

upload_bucket_name = "uploads-calabs-xxxxxx"
resize_bucket_name = "resized-calabs-xxxxxx"

size = 500, 500

s3 = boto3.resource('s3')

def handler(event, context):
    for record in event['Records']:
        print(f'--- processing event record: {record} ---')
        message = json.loads(record['Sns']['Message'])

        for s3_record in message['Records']:
            print(f'--- processing s3 record: {s3_record} ---')
            key = urllib.parse.unquote_plus(s3_record['s3']['object']['key'])
            
            print(f'--- {key} image was uploaded to {upload_bucket_name} ---')
            
            upload_file = BytesIO()
            s3.Bucket(upload_bucket_name).download_fileobj(key, upload_file)
                
            print(f'--- downloaded {key} image from {upload_bucket_name} bucket to in memory file ---')
                
            image = Image.open(upload_file)
            image = image.resize(size)
            resize_file = BytesIO()
            image.save(resize_file, format='JPEG')
            
            print(f'--- resized {key} image to {size} ---')
            
            s3.Object(resize_bucket_name, key).put(Body=resize_file.getvalue())
            
            print(f'--- uploaded {key} file to {resize_bucket_name} bucket ---')


