variable "region" {
  type = string
}

variable "instance_type" {
  type = string
}
variable "key_name" {
  type = string
}

variable "availability_zones" {
  type = list(string)
}

variable "workstation_ip" {
  type = string
}

variable "amis" {
  type = map(any)
  default = {
    "eu-north-1" : "ami-08b0de3847e24ff84"
  }
}