<br />
<p align="center">
  <a href="#list-of-labs">
    <img src="/images/aws-labs-logo.png" alt="Logo" width="260" height="228">
  </a>

  <h3 align="center">100 days in Cloud</h3>

  <p align="center">
    One lab a day with AWS cloud services. 
    <br />
    <br />
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#paid-AWS-learning-options">Paid AWS learning options</a></li>
        <li><a href="#recommended-prerequisites">Recommended prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#list-of-labs">List of labs</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<img src="/images/AmazonWebservices_Logo.png" alt="Logo" width="200" height="100">
Idea is to cover as many branches of AWS in different labs, some in Management Console, some through AWS CLI. AWS features over 200 services so there’s lots to lab on.

### Built With

* [AWS CLI](https://aws.amazon.com/cli/)
* [Python](https://aws.amazon.com/developer/language/python/)
* [AWS CloudFormation Templates](https://aws.amazon.com/cloudformation/resources/templates/)



<!-- GETTING STARTED -->
## Getting Started

To get started with AWS you'll either create a new [Free Tier](https://aws.amazon.com/free/) account or start
one of the paid services that offer labs and sandboxes. You’ll find some examples in <a href="#Paid AWS learning options">Paid AWS learning options</a> section.
The advantage of the paid services is that you’ll get the labs with clear instructions, in some cases guidance and a sandbox, that is provided AWS account where you can deploy services without worrying about additional costs.


### Paid AWS learning options

Here’s a list of services used as a source of labs:
* [A Cloud Guru](https://acloudguru.com/browse-training?type=lab) - paid with some free options
* [WhizLabs](https://play.whizlabs.com/) - paid with some free options
* [Udemy course Ultimate AWS Certified Developer Associate 2021](https://www.udemy.com/course/aws-certified-developer-associate-dva-c01/?src=sac&kw=Ultimate+AWS+Certified+Developer+Associate+2021) - paid

And some free ones:
* [AWS Hands-On repository](https://aws.amazon.com/getting-started/hands-on/) - free
* ['Be a better dev' YouTube channel](https://www.youtube.com/c/BeABetterDev) - free

### Recommended prerequisites

1. Install [Visual Studio Code](https://code.visualstudio.com/download) for writing JSON,YAML files or Lambda functions
2. Install AWS Command Line Interface [from here](https://awscli.amazonaws.com/AWSCLIV2.msi) for command line labs
   * verify the installation by running this command in Command Prompt or Terminal:
    ```sh
   aws --version
   ```
   * configure you're AWS CLI with your credentials, here's more [info](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)
    ```sh
   aws configure
   ```

## List of labs

List of Labs in the repository (will be growing as time passes towards the end of 2021) in countdown order:
* [Day 100 - Using EC2 Roles and Instance Profiles in AWS](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/100%20-%20Using%20EC2%20Roles%20and%20Instance%20Profiles%20in%20AWS)
* [Day 99 - Deploy an Amazon RDS Multi-AZ and Read Replica in AWS](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/99%20-%20Deploy%20an%20Amazon%20RDS%20Multi-AZ%20and%20Read%20Replica%20in%20AWS)
* [Day 98 - AWS IoT - ESP32-CAM and Rekognition](https://github.com/CloudedThings/100-Days-in-Cloud/tree/main/Labs/98%20-%20AWS%20IoT%20-%20ESP32-CAM%20and%20Rekognition)


## License

Distributed under the MIT License.



<!-- CONTACT -->
## Contact

Leszek Ucinski [![LinkedIn][linkedin-shield]][linkedin-url]

Project Link: [https://github.com/CloudedThings/100-Days-in-Cloud](https://github.com/CloudedThings/100-Days-in-Cloud)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [A Cloud Guru](https://acloudguru.com/)
* [Whizlabs](https://www.whizlabs.com/)
* [Udemy](https://www.udemy.com/)
* [Be A Better Dev](https://www.youtube.com/c/BeABetterDev)
* [AWS](https://aws.amazon.com/training/self-paced-labs/)

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/leszekucinski/
