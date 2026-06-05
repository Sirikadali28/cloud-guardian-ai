resource "aws_kinesis_stream" "events" {
  name             = "${var.project_name}-events"
  shard_count      = 1
  retention_period = 24

  tags = local.common_tags
}