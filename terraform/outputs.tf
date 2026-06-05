output "kinesis_stream_name" {
  value = aws_kinesis_stream.events.name
}

output "sns_topic_arn" {
  value = aws_sns_topic.alerts.arn
}

output "bucket_name" {
  value = aws_s3_bucket.data_lake.bucket
}