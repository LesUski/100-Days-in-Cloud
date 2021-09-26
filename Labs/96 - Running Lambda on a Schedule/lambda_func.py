import json
import boto3

def lambda_handler(event, context):
    region = 'us-east-1'
    client = boto3.client("ec2", region_name=region)
    status = client.describe_instance_status(IncludeAllInstances = True)   

    for i in status["InstanceStatuses"]:       
        instaId = list(i["InstanceId"].split(" "))
        if i["InstanceState"]["Name"] == "running":
            print("Instances status : ", i["InstanceState"]["Name"])
            client.stop_instances(InstanceIds=instaId)
            print("Stopping the instance",i["InstanceId"])           
        elif i["InstanceState"]["Name"] == "stopped":
            print("Instances status : ", i["InstanceState"]["Name"])
            client.start_instances(InstanceIds=instaId)
            print("Starting the instance",i["InstanceId"])           
        else:
            print("Please wait for the instance to be in stopped or running state")
        print("\n")
    return {
        'statusCode': 200,
    }