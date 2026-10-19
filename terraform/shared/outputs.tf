output "github_ci_role_arn" {
  value = aws_iam_role.github_ci.arn
}

output "ecr_repository_urls" {
  value = { for k, r in aws_ecr_repository.service : k => r.repository_url }
}