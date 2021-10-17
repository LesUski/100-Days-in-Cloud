<br />
<p align="center">
  <a href="https://github.com/CloudedThings/100-Days-in-Cloud">
    <img src="/images/aws-labs-logo.png" alt="Logo" width="260" height="228">
  </a>

  <h3 align="center">100 days in Cloud</h3>

  <p align="center">
    Build a real time data streaming system with Amazon Kinesis Data Streams
    <br />
    Lab 97
    <br />
  </p>
</p>

<details open="open">
  <summary><h2 style="display: inline-block">Lab Details</h2></summary>
  <ol>
    <li><a href="#services-covered">Services covered</a>
    <li><a href="#lab-description">Lab description</a></li>
      <ul>
        <li><a href="#lab-diagram">Lab diagram</a></li>
      </ul>
    </li>
    <li><a href="#lab-date">Lab date</a></li>
    <li><a href="#prerequisites">Prerequisites</a></li>    
    <li><a href="#lab-steps">Lab steps</a></li>
    <li><a href="#lab-files">Lab files</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

## Services Covered
* **Amazon Kinesis**
* **Amazon S3**
* **AWS Lambda**
* **IAM**

## Lab description
An application uploads text files to S3 Bucket. Whenever a file is uploaded to the bucket a Lambda function get triggered. Lambda function reads the content of the file and pushes the data to the Kinesis data stream. There are two consumers which consume the data from the stream.
* **Creating Lambda functions and setting up Triggers**
* **Creating Kinesis data stream**
* **Setting Lambda functions as consumers of Kinesis data stream**
* **Monitoring CloudWatch events in Logs**

## Lab diagram
![datastream_diagram](https://user-images.githubusercontent.com/70897432/134764974-edc82e95-69df-4c74-b801-5afa3aa038cd.png)

### Lab date
25-09-2021

### Prerequisites
* AWS account

### Lab source
[Whizlabs.com](https://play.whizlabs.com/site/task_details?lab_type=1&task_id=271&quest_id=35)

### Lab steps
1. In IAM create a ROle for Lambda functions, attach permissions policies
  * AmazonS3FullAccess
  * CloudWatchFullAccess
  * AmazonKinesisFullAccess
  Give it an adequate name, we will attach this Role to Lambda in next steps.
2. Create Kinesis Data Stream. Set Number of open shards to 1. After creation enable server-side encryption in Configuration.
3. Create a S3 Bucket. Enable Bucket Versioning and server-side encryption with Amazon S3 key. 
4. Create Lambda function called **"producer"**, select Node.js as runtime, as execution role use the one created in step 1. [producer.js](https://github.com/CloudedThings/100-Days-in-Cloud/blob/main/Labs/97%20-%20Build%20a%20real%20time%20data%20streaming%20system%20with%20Amazon%20Kinesis%20Data%20Streams/producer.js) reads the data from newly uploaded S3 object and sends that data to earlier created Kinesis data stream.
5. Create event notification in S3 Bucket created earlier, set the suffix for '.txt' type of objects. As event types choose 'All object create events' and as Destination choose the 'producer' Lambda function. This will trigger Lambda each time new object will be uploaded.
6. Create two consumer Lambda functions:
  * [consumer1](https://github.com/CloudedThings/100-Days-in-Cloud/blob/main/Labs/97%20-%20Build%20a%20real%20time%20data%20streaming%20system%20with%20Amazon%20Kinesis%20Data%20Streams/consumer1.js) - Node.js as runtime and attach existing role created earlier. This function will log to the console the received data. Add trigger and choose the created Kinesis stream.
  * [consumer2](https://github.com/CloudedThings/100-Days-in-Cloud/blob/main/Labs/97%20-%20Build%20a%20real%20time%20data%20streaming%20system%20with%20Amazon%20Kinesis%20Data%20Streams/consumer2.js) - similar to the first one, this one will log the data to the console. Ass Trigger choose kinesis stream.
7. Upload a text file to S3 Bucket. This will trigger the **producer** Lambda. To check the event logs go to CloudWatch and under Logs check if the producer logged it events. The consumer Lambdas should also log the events with the text from the data stream.
 

### Lab files
* producer.js - Lambda function triggered when uploading file into S3 Bucket, reads the data and sends it to the Kinesis data stream
* consumer1.js and consumer2.js - consumer Lambda functions that process Kinesis data stream

### Acknowledgements
* [whizlabs.com](https://www.whizlabs.com/)
