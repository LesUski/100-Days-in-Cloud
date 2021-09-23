Using EC2 Roles and Instance Profiles in AWS
Date: 2021-09-22

This lab is part of A Cloud Guru catalog
https://learn.acloud.guru/handson/2eb1d816-31b5-4a2c-959e-b4e7140df731

![lab_diagram_Lab_-_Using_EC2_Roles_and_Instance_Profiles 001](https://user-images.githubusercontent.com/70897432/134418386-1c7fbf47-490c-4ffe-b78f-b13a312725d8.png)


Create a Trust Policy and Role Using the AWS CLI
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
Attempt to view the files in the s3bucketsecret bucket.
