# Example of a string variable
variable network_cidr {
  default = "192.168.100.0/24"
}

# Example of a list variable
variable availability_zones {
  default = ["us-west-2a", "us-west-2b"]
}

# Example of an integer variable
variable instance_count {
  default = 2
}

# Example of a map variable
variable ami_ids {
  default = {
    "us-west-2" = "ami-0fb83677"
    "us-east-1" = "ami-97785bed"
  }
}
