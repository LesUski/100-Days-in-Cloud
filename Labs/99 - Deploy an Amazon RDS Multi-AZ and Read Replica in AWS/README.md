<br />
<p align="center">
  <a href="https://github.com/CloudedThings/100-Days-in-Cloud">
    <img src="/images/aws-labs-logo.png" alt="Logo" width="260" height="228">
  </a>

  <h3 align="center">100 days in Cloud</h3>

  <p align="center">
    Deploy an Amazon RDS Multi-AZ and Read Replica in AWS 
    <br />
    Lab 99
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
* **RDS**
* **Route 53**

## Lab description
This lab exercises folowing concepts with use of AWS CLI commands:
* **Creating RDS Read Replicas**
* **Enabling Multi-AZ and backups**
* **Promoting a read replica**
* **Updating the RDS endpoint in Route 53**

## Lab diagram
![lab99diagram](https://user-images.githubusercontent.com/70897432/134534449-3ead68bb-1bde-42fe-8579-11ba9cb4bcff.png)


### Lab files
* AWS_CLI_commands.txt - contains used commands to perform project

### Lab date
23-09-2021

### Lab source
This lab is part of [A Cloud Guru catalog](https://acloudguru.com/hands-on-labs/deploying-an-amazon-rds-multi-az-and-read-replica)

### Lab steps
_All the ids for resources are temporary values specific for the lab_
* Enable Multi-AZ Deployment
```sh
   aws rds modify-db-instance --db-instance-identifier db-OBWWA4PQF2XPOBVZP7WQ6CUKGI --multi-az
   ```
* Create a Read Replica
```sh
   aws rds create-db-instance-read-replica --db-instance-identifier wordpress-rr   --source-db-instance-identifier wordpress
   ```
* Promote the Read Replica and Change the CNAME Records Set in Route 53 to the New Endpoint
```sh
    aws rds promote-read-replica \
    --db-instance-identifier wordpress-rr
    ```
* Check the hosted zone resource record sets
```sh
    aws route53 list-resource-record-sets --hosted-zone-id Z02351242NWTTQUT6NPRI
    ```
* Get Read Replicas endpoint
```sh
aws rds describe-db-instances --db-instance-identifier wordpress-rr
    ```
* Create 'change-name.json' then change the record set in Route 53 hosted zone to the new db
```sh
    aws route53 change-resource-record-sets --hosted-zone-id Z02351242NWTTQUT6NPRI --change-batch file://change-name.json
    ```

### Acknowledgements
* [A Cloud Guru](https://acloudguru.com/)

