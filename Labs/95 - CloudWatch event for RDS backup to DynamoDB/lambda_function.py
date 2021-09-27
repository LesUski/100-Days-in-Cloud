import json
import pymysql
import boto3


RDS_endpoint = "myrdsinstance.cdegnvsebaim.us-east-1.rds.amazonaws.com"
UserName = "mydatabaseuser"
Password = "mydatabasepassword"
DatabaseName = "StudentDB"

DynamoDB_Table_Name = "RDS_Backup_Table"


def lambda_handler(event, context):
    try:
        header = []
        row_json = []
        table_json = {}
        connectionString = pymysql.connect(RDS_endpoint, user= UserName, passwd= Password, db= DatabaseName)
        pointer = connectionString.cursor()
        pointer.execute('SELECT * FROM students')
        
        table_rows = pointer.fetchall()
        print(table_rows)
        
        #Client connection to DynamoDB
        try:
            dynamodbConnection = boto3.resource("dynamodb", region_name = "us-east-1")
            dynamodbClient = dynamodbConnection.Table(DynamoDB_Table_Name)
            
            #Put item to DynamoDB Table
            try:
                for r in table_rows:
                    item_response = dynamodbClient.put_item(
                        Item = {
                            'studentId' : str(r[0]),
                            'studentName' : r[1],
                            'Course' : r[2],
                            'Semester' : r[3]
                        }
                    )
                return {"Status" : 200, "Message" : "Successfully took RDS Backup to DynamoDB"}
            except Exception as e:
                print("Insert Item to DynamoDB Table failed because ", e)
        except Exception as e:
            print("Client connection to DynamoDB Failed because ", e)
    except Exception as e:
        print("RDS Table connection failed because ", e)