

<br />

<p align="center">
  <a href="img/">
    <img src="img/lab55_diagram.jpg" alt="cloudofthings" width="551" height="389">
  </a>
  <h3 align="center">100 days in Cloud</h3>
<p align="center">
    ELB Network Load Balancer Challenge
    <br />
    Lab 54
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
* ![EC2](https://github.com/CloudedThings/100-Days-in-Cloud/blob/main/images/AmazonEC2.png) **EC2**
---

## Lab description

*This hands-on lab challenge will test your practical ability to configure a solution in a production-like AWS environment. You will be presented with a task and set of requirements that you must fulfill to pass the challenge.*

---

### Learning Objectives



* Create Target Groups and register target instances
* Configure Listeners
* Enable access logs for NLB
* Enable stickiness

### Lab date
07-11-2021

---

### Prerequisites
* AWS account

---

### Lab steps
1. Create UDP target group for DNS servers. Create a target group for dns servers that satisfies the following: Contains dns in its name, Uses port 53, Uses the UDP protocol.

   <img src="img/lab54_dnsTG.jpg" alt="dnstg" style="zoom:80%;" />

2. Create TCP target group for web servers. Create a target group for web servers that satisfies the following: Contains web in its name, Uses port 80, Uses the TCP protocol.

   <img src="img/lab54_webTG.jpg" alt="webTG" style="zoom:50%;" />

3. Register an Instance in the Dns Target Group. Register the dns-server instance in the dns target group using port 53. Register the instance named web-server in the web target group using port 80.

4. Add Listener for DNS Targets. Add a listener to the network-load-balancer that sends traffic to your dns target group. The listener must use port 53 and the UDP protocol.

   <img src="img/lab54_dns-listener.jpg" alt="dnslistener" style="zoom:80%;" />

5. Add Listener for Web Targets. Add a listener to the network-load-balancer that sends traffic to your web target group. The listener must use port 80 and the TCP protocol.

   <img src="img/lab54_web-listener.jpg" alt="weblistener" style="zoom:80%;" />

6. Enable Stickiness for the Web Target Group. Enable stickiness for the web target group. Navigate to the web target group and then go to *Edit attributes* and check in *Stickiness*.

   <img src="img/lab54_stickines.jpg" alt="stickiness" style="zoom:80%;" />

7. Enable access logs for the **network-load-balancer** and store the logs in Amazon S3. Navigate to *Load Balancers*, and in *Description* tag go to *Edit attributes*.

   <img src="img/lab54_accesslogs.jpg" alt="accesslogs" style="zoom:80%;" />

   

---

### Lab files
* 
---

### Acknowledgements
* [cloud academy](https://cloudacademy.com/lab-challenge/elb-network-load-balancer-challenge/)

