resource "aws_s3_bucket" "data_lake" {
  bucket = "${var.project_name}-data-lake"

  tags = local.common_tags
}