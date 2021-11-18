

<br />

<p align="center">
  <a href="img/">
    <img src="img/lab43_diagram.jpg" alt="cloudofthings" width="471" height="322">
  </a>
  <h3 align="center">100 days in Cloud</h3>
<p align="center">
    Using Terraform with remote state and lock create EC2 Instance 
    <br />
    Lab 43
    <br/>
  </p>





</p>

<details open="open">
  <summary><h2 style="display: inline-block">Lab Details</h2></summary>
  <ol>
    <li><a href="#services-covered">Services covered</a>
    <li><a href="#lab-description">Lab description</a></li>
    </li>
    <li><a href="#lab-date">Lab date</a></li>
    <li><a href="#prerequisites">Prerequisites</a></li>    
    <li><a href="#lab-steps">Lab steps</a></li>
    <li><a href="#lab-files">Lab files</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

---

## Services Covered
* ![Terraform](https://github.com/CloudedThings/100-Days-in-Cloud/blob/main/images/terraform.png) **Terraform**
---

## Lab description

In this challenge I need to create a S3 bucket and a DynamoDB for remote state and lock backend setup for Terraform. As resources an EC2 Instance will be created.

## Project structure
```
├── main.tf
├── terraform.tfvars
└── variables.tf
```

---

### Learning Objectives
* Create Terraform template to launch resources
* Create  EC2 instance
* Create remote backend on S3 and lock featuring DynamoDB
* Use variables in the template

### Lab date
18-11-2021

---

### Prerequisites
* AWS account
* Terraform installed


---

### Lab steps
1. Set up the S3 remote state backend by creating a S3 bucket and DynamoDB table. Create unique bucket name by running:

   ``` 
   S3NAME="terraformstate$(date | md5sum | head -c 8)" 
   ```

   THen create bucket:

   ```
   aws s3api create-bucket \
       --bucket $S3NAME \
       --region us-west-2 \
       --create-bucket-configuration \
       LocationConstraint=us-west-2
   ```

   Add encryption:

   ```
   aws s3api put-bucket-encryption \
       --bucket $S3NAME \
       --server-side-encryption-configuration={\"Rules\":[{\"ApplyServerSideEncryptionByDefault\":{\"SSEAlgorithm\":\"AES256\"}}]}
   ```

   Enable versioning:

   ```
   aws s3api put-bucket-versioning --bucket $S3NAME --versioning-configuration Status=Enabled
   ```

   Create table:

   ```
   aws dynamodb create-table \
       --table-name terraform-state-lock \
       --attribute-definitions \
           AttributeName=LockID,AttributeType=S \
       --key-schema \
           AttributeName=LockID,KeyType=HASH \
       --region us-west-2 \
       --provisioned-throughput \
           ReadCapacityUnits=20,WriteCapacityUnits=20
   ```

   Set environment variable for table:

   ```
   TABLE=$(aws dynamodb list-tables --region us-west-2 --query "TableNames[]" --output text)
   ```

   Check the environment variables values:

   ```
   echo "Use Bucket: $S3NAME and Table: $TABLE"
   ```

   

2. Create main.tf and variables.tf. In main.tf use the following code:

   ```
   terraform {
     required_providers {
       aws = {
         source  = "hashicorp/aws"
         version = "3.7"
       }
     }
     backend "s3" {
       bucket = "<<REPLACE_ME_$S3NAME>>"
       key    = "<<PATH_TO>>/terraform.tfstate"
       region = "us-west-2"
       dynamodb_table = "$TABLE"
       encrypt        = true
     }
   }
   
   provider "aws" {
     region = "us-west-2"
   }
   
   resource "aws_instance" "cloudacademylabs" {
       ami = var.amis[var.region]
       instance_type = var.instance_type
   
       tags = {
           Name = "cloudacademylabs"
       }
   }
   ```

   Variables.tf:

   ```
   variable "bucket" {
       type = string
   }
   
   variable "amis" {
       type = map(any)
       default = {
           "us-west-2": "ami-00be885d550dcee43" 
       }
   }
   
   variable "instance_type" {
       type = string
   }
   
   variable "region" {
       type = string
   }
   ```

   And then in terraform.tfvars you'll specify the requirements for region, instance_type.

3. Apply the set-up:

   ```
   terraform init
   terraform apply
   ```

### Lab files
* [main.tf](main.tf)
* [variables.tf](main.tf)
---

### Acknowledgements
* [cloudacademy](https://cloudacademy.com/lab-challenge/deploy-ec2-terraform-aws-challenge/?context_resource=lp&context_id=2377)

