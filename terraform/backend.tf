terraform {
  backend "s3" {
    bucket         = "test-terraform-state-animal-shelter"
    key            = "terraform.tfstate"
    region         = "us-east-1"
  }
}
