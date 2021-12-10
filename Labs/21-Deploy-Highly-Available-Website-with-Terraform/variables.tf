variable network_cidr {
  default = "192.168.100.0/24"
}

variable availability_zones {
  default = ["us-west-2a", "us-west-2b"]
}

variable instance_count {
  default = 2
}

variable ami_ids {
default = {
    "us-west-2" = "ami-0fb83677"
    "us-east-1" = "ami-97785bed"
  }
}
