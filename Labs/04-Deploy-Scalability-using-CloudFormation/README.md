<br />

<p align="center">
  <a href="img/">
    <img src="img/lab04_diagram.jpg" alt="cloudofthings" width="521" height="410">
  </a>
  <h3 align="center">100 days in Cloud</h3>
<p align="center">
  Deploy a TODO app on ELB, ASG and DynamoDB table
    <br />
    Lab 4
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
* ![cloudformation](https://github.com/CloudedThings/100-Days-in-Cloud/blob/main/images/CloudFormation.png) **CloudFormation**

---

## Lab description

* *A business has tasked you with deploying a prototype of a new application. The business has given you the following requirements:*

- *Deploy [this Todo application](http://github.com/cloudacademy/dynamo-demo) in AWS*
- *Allow for simple scaling of the compute and database layers*
- *Use the following:*
  - *AWS EC2 to host the application*
  - *AWS ELB to load balance public traffic*
  - *AWS DynamoDB for the database*
- *Appropriately use public and private subnets*
- *Deployments should be easily repeatable*
- *Allow for the deployment of multiple environments (development, testing, and production)*
- *Allow for deployment into any AWS Region*
- *As this is a prototype, multi-availability zone redundancy is not required*

---

### Learning Objectives
:star: Create a template
:star: Create a stack

---

### Lab date
27-12-2021

---

### Prerequisites
AWS account

---

### Lab steps
1. Create a CLoudFormation template. This is the result: [template.json](template.json).

2. In CloudFormation dashboard create a stack by uploading that template. Then create a stack

   ![lab04_stack_creation](img/lab04_stack_creation.jpg)

3. When the stack creation completes go to Outputs and navigate to the address.
    ![lab04_stack_output](img/lab04_stack_output.jpg)

### Lab files
* [template.json](template.json)

---

### Acknowledgements
* [cloud academy](https://cloudacademy.com/lab/hands-cloudformation-deploy-scalability/?context_id=2654&context_resource=lp)

