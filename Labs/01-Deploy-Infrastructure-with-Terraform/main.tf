provider "aws" {
  version = "2.69"

  region  = "us-west-2" # Oregon
}

data "aws_availability_zones" "available" {
  state = "available"
}

resource "aws_vpc" "web_vpc" {
  cidr_block           = "192.168.100.0/24"
  enable_dns_hostnames = true

  tags = {
    Name = "Web VPC"
  }
}

resource "aws_subnet" "subnet1" {
  vpc_id            = aws_vpc.web_vpc.id
  cidr_block        = cidrsubnet(aws_vpc.web_vpc.cidr_block, 8, 1)
  availability_zone = data.aws_availability_zones.available.names[0]
}

resource "aws_instance" "web" {
  ami = "ami-0528a5175983e7f28"
  instance_type = "t2.micro"
  subnet_id = aws_subnet.subnet1.id
  root_block_device {
    volume_size = "10"
  }
}