<br />
<p align="center">
  <a href="https://github.com/CloudedThings/100-Days-in-Cloud">
    <img src="/images/aws-labs-logo.png" alt="Logo" width="260" height="228">
  </a>

  <h3 align="center">100 days in Cloud</h3>

  <p align="center">
    AWS IoT - ESP32-CAM and Rekognition 
    <br />
    Lab 98
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
* **IAM**
* **S3**
* **IoT Core**
* **AWS Lambda**
* **AWS Rekognition**

## Lab description
In this lab an ESP32 with camera will connect to IoT Core, subsribe to a topic, obtain presign url to S3 object for an upload, then upload the picture to S3. Two Rules in IoT Core will trigger two Lambda functions, one that will generate mentioned presigned url, second will get the S3 object and send it to rekognition and publish the result to IoT topic
* **Creating Things, Roles, attaching certificates and policies**
* **Creating S3 buckets**
* **Changing CORS configuration of S3 buckets**
* **Creating Lambda function and giving them neccessary permissions**
* **Creating presigned urls for S3 objects**

## Lab diagram
![image](https://user-images.githubusercontent.com/70897432/134690420-f7120a4b-d96d-4fa4-8984-79f2d106a937.png)


### Lab date
24-09-2021

### Prerequisites
* ESP32-CAM (Ai-Thinker ESP32-S in this project)
* FTDI cable for connecting device throug USB
* AWS account
* Visual Studio Code with PlatformIO IDE extension installed or Arduino IDE 
* [POSTMAN](https://www.postman.com/downloads/) to make API calls

### Lab source
[The Internet of Things on AWS – Official Blog](https://aws.amazon.com/blogs/iot/creating-object-recognition-with-espressif-esp32/)

### Lab steps
1. Create a thing in IoT Core, either in Console or through CLI
2. Get your IoT device data endpoint (AWS IoT Core -> Settings) or through CLI
```sh
    aws iot describe-endpoint --region <YOUR REGION>
```
3. Reformat you certificates with " and \n, it's time consuming but neccessary for the device to connect. It'll look like that:
```sh
  "-----BEGIN CERTIFICATE-----\n"
  "MIIDQTCCAimgAwIBAgITBmyfz5m/jAo54vB4ikPmljZbyjANBgkqhkiG9w0BAQsF\n"
  "ADA5MQswCQYDVQQGEwJVUzEPMA0GA1UEChMGQW1hem9uMRkwFwYDVQQDExBBbWF6\n"
  "b24gUm9vdCBDQSAxMB4XDTE1MDUyNjAwMDAwMFoXDTM4MDExNzAwMDAwMFowOTEL\n"
```
4. Create a policy for the device, [policy.json](https://github.com/CloudedThings/100-Days-in-Cloud/blob/main/Labs/98%20-%20AWS%20IoT%20-%20ESP32-CAM%20and%20Rekognition/thing_policy.json)
```sh
{
  ...
      {
        "Effect": "Allow",
        "Action": "iot:Connect",
        "Resource": "arn:aws:iot:eu-central-1:797321539388:client/ESP32-cam"
      },
      {
        "Effect": "Allow",
        "Action": "iot:Subscribe",
        "Resource": "arn:aws:iot:eu-central-1:797321539388:topicfilter/esp32/sub/data"
      },
    ...
  }
```
5. Create S3 Bucket 
  * under permissions add bucket policy allowing "s3:getObject" and "s3:PutObject" for your IAM User
  * add CORS configuration 
      ```sh
        [
          {
              "AllowedHeaders": [
                  "*"
              ],
              "AllowedMethods": [
                  "GET",
                  "PUT",
                  "POST",
                  "DELETE"
              ],
              "AllowedOrigins": [
                  "*"
              ],
              "ExposeHeaders": []
          }
      ]
      ```
6. Create two Lambda functions:
  * one to generate presigned url in S3 called [esp32-request-url.py](https://github.com/CloudedThings/100-Days-in-Cloud/blob/main/Labs/98%20-%20AWS%20IoT%20-%20ESP32-CAM%20and%20Rekognition/esp32-request-rekognition.py) and change it's policy and allow publishing in IoT and getting objects from S3 [esp32-request-url-policy.json]()
  * second called [esp32-request-rekognition.py](https://github.com/CloudedThings/100-Days-in-Cloud/blob/main/Labs/98%20-%20AWS%20IoT%20-%20ESP32-CAM%20and%20Rekognition/esp32-request-rekognition.py) will get the object from S3 when triggered by IoT Rule and send it to Rekognition, then it'll publish result to topic 'esp32/sub/data'
7. Create two Rules in IoT Core:
  * one with querry statement: 
  ```sh
  SELECT * FROM 'esp32/pub/url'
  ```
  and action to send message to esp32-request-url Lambda function
  * second with querry statement:
  ```sh
  SELECT * FROM 'esp32/pub/data'
  ```
  action will be send message to esp32-request-rekognition Lambda function
9. Test if your permissions allow for posting to topics and if Lambda generate url and response from Rekognition (you can use Postman for API calls and sending pictures)
10. The AWS part is complete. Since this is an AWS Challenge I won't be going in to the details of programming ESP32 here. Please refer to [Nathan Glovers GitHub page](https://github.com/t04glovern/aws-esp32-cam) for more details.

### Lab files
* thing_policy.json - policy granting ESP32-Cam neccessary allowed actions in IoT Core
* esp32-request-rekognition.py - Lambda function code to generate presigned url in S3
* esp32-request-url-policy.json - execution policy for Lambda function
* esp32-request-rekognition.py - Lambda function trigerred by IoT set on topic, gets picture from S3, sends it to Rekognition
* esp32-request-url-policy.json - execution policy for Lambda function
* esp32-request-rekognition-policy.json

### Acknowledgements
* [Nathan Glover](https://github.com/t04glovern/aws-esp32-cam)
* [The Internet of Things on AWS – Official Blog](https://aws.amazon.com/blogs/iot/creating-object-recognition-with-espressif-esp32/)
