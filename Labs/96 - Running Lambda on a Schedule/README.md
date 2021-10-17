<br />
<p align="center">
  <a href="https://github.com/CloudedThings/100-Days-in-Cloud">
    <img src="/images/aws-labs-logo.png" alt="Logo" width="260" height="228">
  </a>

  <h3 align="center">100 days in Cloud</h3>

  <p align="center">
    Running Lambda on a schedule
    <br />
    Lab 96
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
* **EC2**
* **Lambda**
* **IAM**
* **CloudWatch Events**

## Lab description
Purpose of this lab is to create an CloudWatch Event Rule that will trigger the Lambda function on a schedule. Lambda will check the status of an instance in the same region, and then change it. If instance is running it'll be stopped and vice versa.
* **Creating Lambda functions**
* **Creating CloudWatch Event Rules**
* **Checking EC2 Instance status with Lambda function**

## Lab diagram
![lab97diagram](https://user-images.githubusercontent.com/70897432/134799976-5b8c50d2-c6b1-4cd1-b017-df20f3dcaf18.png)


### Lab date
26-09-2021

### Prerequisites
* AWS account

### Lab source
[Whizlabs.com](https://play.whizlabs.com/site/task_details?lab_type=1&task_id=132&quest_id=36)

### Lab steps
1. Create an EC2 Instance of type 2.micro, with attached Security Group with allowed Ingress rules for SSH, HTTP and HTTPS.
2. In IAM create role for Lambda Service with permissions to "Allow" wide action on resources set up in [policy](https://github.com/CloudedThings/100-Days-in-Cloud/blob/main/Labs/96%20-%20Running%20Lambda%20on%20a%20Schedule/lambda_role.json).
3. Create [Lambda function](https://github.com/CloudedThings/100-Days-in-Cloud/blob/main/Labs/96%20-%20Running%20Lambda%20on%20a%20Schedule/lambda_func.py) with Python as runtime and attach the above mentioned Role to it. This function will check status of Instances and change it accordingly, if it's running it will stop the instance and so on.
4. In CloudWatch create a Rule in Events with either fixed rate or a CRON job. Add the Lambda function as target, this will trigger function.
5. Edit created Lambda Configuration and set the Timeout to 1 minute. 
 
### Lab files
* lambda_role.json - policy attached to the Lambda execution Role, giving it wide permission on EC2
* lambda_func.py - Lambda function that will check instance status and change it accordingly

### Acknowledgements
* [whizlabs.com](https://www.whizlabs.com/)
