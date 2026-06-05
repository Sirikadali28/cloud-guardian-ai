# Deployment Guide

## Prerequisites

- AWS Account
- AWS CLI
- Terraform >= 1.5
- Python 3.11+

## Step 1: Configure AWS

```bash
aws configure
```

Enter your AWS credentials when prompted.

## Step 2: Initialize Terraform

```bash
cd terraform
terraform init
```

## Step 3: Validate Configuration

```bash
terraform validate
```

## Step 4: Review Infrastructure Plan

```bash
terraform plan
```

Review the resources that will be created before proceeding.

## Step 5: Deploy Infrastructure

```bash
terraform apply
```

Type `yes` when prompted to confirm the deployment.

## Step 6: Verify Resources Created

Verify the following AWS resources are created in your account:

- ✅ S3 Bucket (data lake)
- ✅ Kinesis Data Stream (event streaming)
- ✅ Lambda Functions (compliance_engine, risk_scoring)
- ✅ SNS Topic (alerts)
- ✅ IAM Roles and Policies
- ✅ Glue Job (ETL pipeline)
- ✅ CloudWatch Log Groups

## Step 7: Test Event Processing

Upload sample events to test the pipeline:

```bash
# Sample event files are located in:
sample_data/cloudtrail_event.json
sample_data/securityhub_finding.json
sample_data/config_noncompliant.json
```

Verify the following in AWS Console:

- Lambda execution logs in CloudWatch
- SNS alerts in your email inbox
- S3 data lake contains findings
- Athena queries execute successfully

## Step 8: Run Unit Tests

```bash
pytest tests/ -v
```

## Cleanup (Destroy Infrastructure)

```bash
cd terraform
terraform destroy
```

Type `yes` to confirm deletion of all AWS resources.
