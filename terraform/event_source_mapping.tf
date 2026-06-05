resource "aws_lambda_event_source_mapping" "kinesis_trigger" {

  event_source_arn  = aws_kinesis_stream.events.arn
  function_name     = aws_lambda_function.compliance_engine.arn

  starting_position = "LATEST"

  batch_size = 10
}