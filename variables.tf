variable "region" {
  default = "us-east-1"
}

variable "instance_type" {
  default = "t3.micro" 
}

variable "ami_id" {
  description = "Latest Ubuntu 22.04 AMI for us-east-1"
  default     = "ami-0c7217cdde317cfec" 
}

variable "key_name" {
  description = "The name of your AWS SSH key pair"
  default     = "my-terraform-key"
}
