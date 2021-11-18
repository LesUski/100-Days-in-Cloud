variable "s3_name" {
    type = string
}

variable "bucket" {
    type = string
}

variable "table_name" {
    type = string
}

variable "amis" {
    type = map(any)
    default = {
        "us-west-2": "ami-00be885d550dcee43" 
    }
}

variable "instance_type" {
    type = string
}

variable "region" {
    type = string
}