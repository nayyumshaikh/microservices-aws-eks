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
  default = "shared"
}

variable "services" {
  type    = list(string)
  default = ["users", "orders"]
}

variable "github_repo" {
  type        = string
  description = "owner/repo, e.g. jane/microservices-aws-eks"
}

variable "create_oidc_provider" {
  type        = bool
  default     = true
  description = "AWS allows only one GitHub OIDC provider per account. Set false if it already exists."
}

variable "github_sub_pattern" {
  type        = string
  default     = ""
  description = "Override the OIDC subject match if the default doesn't work"
}