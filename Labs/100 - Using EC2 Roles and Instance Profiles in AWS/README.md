<br />
<p align="center">
  <a href="https://github.com/CloudedThings/100-Days-in-Cloud">
    <img src="/images/aws-labs-logo.png" alt="Logo" width="260" height="228">
  </a>

  <h3 align="center">100 days in Cloud</h3>

  <p align="center">
    Using EC2 Roles and Instance Profiles in AWS 
    <br />
    Lab 100
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
    <li><a href="#lab-files">Lab files</a></li>
    <li><a href="#lab-date">Lab date</a></li>
    <li><a href="#lab-source">Lab source</a></li>    
    <li><a href="#lab-steps">Lab steps</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

## Services Covered
* **IAM**
* **EC2**

## Lab description
This lab excercies folowing concepts with use of AWS CLI commands:
* Practice usage of AWS Identity and Access Management roles for Amazon Elastic Compute Cloud (EC2).
* Create and assign IAM roles
* Create and attach IAM policy
* Attaching Roles to Instances
* Getting access to S3 Buckets
* Practise on AWS CLI usage

## Lab diagram
<p align="center">![lab_diagram_Lab_-_Using_EC2_Roles_and_Instance_Profiles 001](https://user-images.githubusercontent.com/70897432/134418386-1c7fbf47-490c-4ffe-b78f-b13a312725d8.png)</p>

### Lab files
* AWS_CLI_commands.txt - contains used commands to perform project
* IAM_trust_policy_for_EC2.json - trust policy for EC2
* dev_s3_read_access.json - IAM policy granting acces to S3 Get and List actions

### Lab date
22-09-2021

### Lab source
This lab is part of A Cloud Guru catalog
https://learn.acloud.guru/handson/2eb1d816-31b5-4a2c-959e-b4e7140df731

### Lab steps
Taken from [lab source](https://learn.acloud.guru/handson/2eb1d816-31b5-4a2c-959e-b4e7140df731)
_Create a Trust Policy and Role Using the AWS CLI
Obtain the labreferences.txt file from an S3 bucket provisioned with the lab.
Log in to the bastion host and set the AWS CLI region and output type.
Create an IAM trust policy for an EC2 role.
Create an IAM role called DEV_ROLE.
Create an IAM policy DevS3ReadAccess defining read-only access permissions to an S3 bucket.

Create Instance Profile and Attach Role to an EC2 Instance
Attach DevS3ReadAccess policy to the DEV role.
Create the instance profile DEV_PROFILE and add the DEV_ROLE to it via the AWS CLI.
Attach the DEV_PROFILE role to an instance.

Test S3 Permissions via the AWS CLI
Verify the instance is assuming the DEV_ROLE role.
List the buckets in the account.
Attempt to view the files in the s3bucketdev bucket.

Create an IAM Policy and Role Using the AWS Management Console
Navigate to IAM > Policies.
Create an IAM policy ProdS3ReadAccess
Create a PROD_ROLE role.

Attach IAM Role to an EC2 Instance Using the AWS Management Console
Navigate to EC2 > Instances.
Attach the role to the Web Server instance.
In the terminal, as PROD_ROLE, list the buckets.
Attempt to view the files in the s3bucketprod bucket.
Attempt to view the files in the s3bucketsecret bucket._

### Acknowledgements
* [A Cloud Guru](https://acloudguru.com/)
