# Infrastructure as Code for Market Analysis
provider "aws" {
  region = "us-west-2"
}

# RDS PostgreSQL Instance for pre-aggregated market data
resource "aws_db_instance" "market_data_warehouse" {
  allocated_storage    = 20
  engine               = "postgres"
  engine_version       = "15.4"
  instance_class       = "db.t3.micro"
  db_name              = "market_analytics"
  username             = "admin"
  password             = "secure_placeholder_password"
  skip_final_snapshot  = true
  publicly_accessible  = false
}

# S3 Bucket for Power BI extracts and artifacts
resource "aws_s3_bucket" "powerbi_artifacts" {
  bucket = "restaurant-market-analysis-pbi-artifacts"
}
