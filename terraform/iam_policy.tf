resource "aws_iam_role_policy" "lambda_policy" {
  name = "cloud-guardian-lambda-policy"
  role = aws_iam_role.lambda_role.id

  policy = jsonencode({
    Version = "2012-10-17"

    Statement = [

      {
        Effect = "Allow"

        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ]

        Resource = "*"
      },

      {
        Effect = "Allow"

        Action = [
          "sns:Publish"
        ]

        Resource = aws_sns_topic.alerts.arn
      },

      {
        Effect = "Allow"

        Action = [
          "s3:GetObject",
          "s3:PutObject",
          "s3:ListBucket"
        ]

        Resource = [
          aws_s3_bucket.data_lake.arn,
          "${aws_s3_bucket.data_lake.arn}/*"
        ]
      },

      {
        Effect = "Allow"

        Action = [
          "kinesis:GetRecords",
          "kinesis:GetShardIterator",
          "kinesis:DescribeStream",
          "kinesis:ListStreams"
        ]

        Resource = aws_kinesis_stream.events.arn
      }
    ]
  })
}