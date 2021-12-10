provider "aws" {
  version = "< 2"

  region  = "us-west-2" # Oregon
}

resource "aws_vpc" "web_vpc" {
  cidr_block           = "192.168.100.0/24"
  enable_dns_hostnames = true

  tags {
    Name = "Web VPC"
  }
}

resource "aws_subnet" "web_subnet" {
  # Use the count meta-parameter to create multiple copies
  count             = 2
  vpc_id            = "${aws_vpc.web_vpc.id}"
  # cidrsubnet function splits a cidr block into subnets
  cidr_block        = "${cidrsubnet(var.network_cidr, 1, count.index)}"
  # element retrieves a list element at a given index
  availability_zone = "${element(var.availability_zones, count.index)}"

  tags {
    Name = "Web Subnet ${count.index + 1}"
  }
}

resource "aws_instance" "web" {
  count         = "${var.instance_count}"
  # lookup returns a map value for a given key
  ami           = "${lookup(var.ami_ids, "us-west-2")}"
  instance_type = "t2.micro"
  # Use the subnet ids as an array and evenly distribute instances
  subnet_id     = "${element(aws_subnet.web_subnet.*.id, count.index % length(aws_subnet.web_subnet.*.id))}"

  tags {
    Name = "Web Server ${count.index + 1}"
  }
}
