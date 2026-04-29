provider "aws" {
  region = var.region
}

# 1. Create VPC
resource "aws_vpc" "main_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = { Name = "DevOps-VPC" }
}

# 2. Create Internet Gateway
resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.main_vpc.id
}

# 3. Create Subnet
resource "aws_subnet" "main_subnet" {
  vpc_id                  = aws_vpc.main_vpc.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "us-east-1a"
  tags = { Name = "DevOps-Subnet" }
}

# 3a. Create Route Table
resource "aws_route_table" "main_rt" {
  vpc_id = aws_vpc.main_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw.id
  }

  tags = { Name = "DevOps-RouteTable" }
}

# 3b. Associate Subnet with Route Table
resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.main_subnet.id
  route_table_id = aws_route_table.main_rt.id
}

# 4. Create Security Group
resource "aws_security_group" "devops_sg" {
  name        = "devops_sg"
  vpc_id      = aws_vpc.main_vpc.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Allow SSH from anywhere
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Allow Web traffic
  }

  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Allow Jenkins traffic
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"] # Allow all outbound
  }
}

# 5. Create EC2 Instance
resource "aws_instance" "devops_vm" {
  ami           = var.ami_id
  instance_type = var.instance_type
  subnet_id     = aws_subnet.main_subnet.id
  vpc_security_group_ids = [aws_security_group.devops_sg.id]
  key_name      = var.key_name

  user_data = <<-EOF
              #!/bin/bash
              sudo apt update
              sudo apt install -y docker.io
              sudo systemctl start docker
              sudo systemctl enable docker
              sudo docker run -d -p 80:80 yuvadharshinim/my-portfolio:latest
              EOF

  tags = { Name = "DevOps-Server" }
}
