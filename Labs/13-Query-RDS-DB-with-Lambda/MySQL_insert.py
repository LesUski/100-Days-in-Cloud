import json
import pymysql


RDS_endpoint = "myrdsinstance.cdegnvsebaim.us-east-1.rds.amazonaws.com"
UserName = "mydatabaseuser"
Password = "mydatabasepassword"
DatabaseName = "StudentDB"

connectionString = pymysql.connect(RDS_endpoint, user= UserName, passwd= Password, db= DatabaseName)

def lambda_handler(event, context):
    header = []
    row_json = []
    table_json = {}
    pointer = connectionString.cursor()
    pointer.execute("INSERT INTO students(studentName, Course, Semester) VALUES ('Elizabeth', 'Art', 'first')")
    connectionString.commit()
    connectionString.close()
    return("Insertion Success")
    