variable "region" {
  type    = string
  default = "ap-south-1"
}

variable "project" {
  type    = string
  default = "microservices"
}

variable "environment" {
  type    = string
  default = "dev"
}

variable "kubernetes_version" {
  type        = string
  default     = "1.33"
  description = "Check supported versions with: aws eks describe-cluster-versions"
}