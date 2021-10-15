import json

import requests

 
def lambda_handler(event, context):

    r = requests.get('https://github.com') 

    print(r.status_code)

    print(r.headers['Date'])

    print(r.headers['server'])

    return {

        'statusCode': 200,

        'body': json.dumps('success')

    }