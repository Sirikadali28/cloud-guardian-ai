resource "aws_lambda_function" "compliance_engine" {

  filename      = "../lambda/compliance.zip"
  function_name = "cloud-guardian-compliance"

  role    = aws_iam_role.lambda_role.arn
  handler = "compliance_engine.lambda_handler"
  runtime = "python3.11"

  environment {
    variables = {
      SNS_TOPIC_ARN = aws_sns_topic.alerts.arn
    }
  }
}