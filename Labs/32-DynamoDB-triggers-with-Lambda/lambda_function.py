import json
import boto3
DDB = boto3.resource("dynamodb").Table("CloudAcademyLabs")
def lambda_handler(event, context):
    records = event["Records"]
    print("Received %s records" % len(records))
    for record in records:
        print(record)
        # if new record or update
        if record["eventName"].upper() in {"INSERT", "MODIFY"}:
            # primary key
            record_id = record["dynamodb"]["Keys"]["Id"]["S"]
            # init local vars
            old_email = old_is_personal = new_email = new_is_personal = None
            # new and old images
            old_image = record["dynamodb"].get("OldImage") or {}
            new_image = record["dynamodb"].get("NewImage") or {}
            # old values (optional, only on update)
            if "Email" in old_image:
                old_email = old_image["Email"]["S"]
            if "IsPersonalEmail" in old_image:
                old_is_personal = old_image["IsPersonalEmail"]["BOOL"]
            # new values
            if "Email" in new_image:
                new_email = new_image["Email"]["S"]
                new_is_personal = is_personal_email(new_email)
            # avoid recursion on update and write only if strictly needed
            if old_email != new_email and old_is_personal != new_is_personal:
                update_record(record_id, new_is_personal)
    print("Processed %s records" % len(records))
def update_record(record_id, is_personal):
    print("Updating %s: IsPersonalEmail=%s" % (record_id, is_personal))
    DDB.update_item(
        Key={"Id": record_id},
        UpdateExpression="SET IsPersonalEmail = :val",
        ExpressionAttributeValues={":val": is_personal or False},
    )
def is_personal_email(email):
    domains = {"gmail.com", "outlook.com", "hotmail.com"}
    return any(email.endswith(domain) for domain in domains)
