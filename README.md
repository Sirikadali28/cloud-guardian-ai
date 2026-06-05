# Cloud Guardian AI

**Serverless AWS Compliance & Risk Monitoring Platform**

> A production-grade, fully serverless cloud security platform that continuously monitors AWS infrastructure, evaluates compliance violations, scores risks, and delivers real-time security intelligence — built entirely on AWS-native services.

---

## Architecture

![Cloud Guardian AI Architecture](architecture/architecture.png)

---

## Overview

Cloud Guardian AI ingests security and operational events from multiple AWS sources, evaluates them against compliance rules, computes risk severity scores, dispatches alerts, persists findings to a centralized data lake, and surfaces actionable insights through live dashboards — all without managing a single server.

---

## Key Features

| Feature | Description |
|---|---|
| Real-time ingestion | Streams AWS events via Amazon Kinesis Data Streams |
| Compliance evaluation | Automated rule checks via AWS Lambda |
| Risk scoring | Severity-based compliance scoring engine |
| Instant alerts | SNS-based email and SMS notifications |
| Data lake | Centralized JSON / Parquet findings storage on S3 |
| ETL pipeline | AWS Glue cataloging and transformation |
| SQL analytics | Athena-powered ad-hoc security queries |
| Dashboards | QuickSight compliance and risk trend visualizations |
| Infrastructure as Code | Fully reproducible Terraform deployment |

---

## Architecture Flow

```
CloudTrail  ──┐
AWS Config  ──┤──▶  Kinesis Streams  ──▶  Lambda Engine  ──┬──▶  SNS Alerts
Security Hub──┤                                             ├──▶  S3 Data Lake  ──▶  Glue ETL  ──▶  Athena  ──▶  QuickSight
VPC Flow Logs─┘                                             └──▶  Risk Scoring Engine
```

1. **Ingest** — CloudTrail, AWS Config, Security Hub, and VPC Flow Logs emit events continuously.
2. **Stream** — Amazon Kinesis Data Streams buffers and fans out events in real time.
3. **Evaluate** — AWS Lambda applies compliance rules against each event.
4. **Score** — The Risk Scoring Engine calculates compliance severity for each finding.
5. **Alert** — Critical findings trigger SNS notifications via email and SMS.
6. **Store** — All findings are persisted to Amazon S3 in JSON / Parquet format.
7. **Catalog** — AWS Glue crawls and catalogs the S3 data lake.
8. **Analyse** — Athena runs SQL analytics over the cataloged findings.
9. **Visualise** — QuickSight renders live compliance dashboards and risk trends.

---

## AWS Services

| Service | Purpose |
|---|---|
| Amazon Kinesis | Real-time event streaming |
| AWS Lambda | Compliance evaluation engine |
| Amazon SNS | Alert notifications (email / SMS) |
| Amazon S3 | Data lake — JSON / Parquet storage |
| AWS Glue | ETL pipeline and Data Catalog |
| Amazon Athena | Serverless SQL analytics |
| Amazon QuickSight | Compliance dashboards |
| AWS Config | Resource compliance monitoring |
| AWS CloudTrail | API activity and audit logging |
| AWS Security Hub | Aggregated security findings |
| VPC Flow Logs | Network traffic visibility |
| Terraform | Infrastructure as Code |

---
## AWS Infrastructure Screenshots

### Lambda Functions
![Lambda Functions](screenshots/lambda-functions.png)

### Lambda Compliance Engine
![Lambda Code](screenshots/lambda-code.png)

### S3 Data Lake
![S3 Buckets](screenshots/s3-buckets.png)

### IAM Security Role
![IAM Role](screenshots/iam-role.png)

### CloudWatch Monitoring
![CloudWatch Dashboard](screenshots/cloudwatch-dashboard.png)

### CloudWatch Logs
![CloudWatch Logs](screenshots/cloudwatch-logs.png)

### Glue Crawler
![Glue Crawler](screenshots/glue-crawler.png)

### Glue Database
![Glue Database](screenshots/glue-database.png)

### Athena Query Editor
![Athena Editor](screenshots/athena-editor.png)

### Athena Results
![Athena Results](screenshots/athena-query-results.png)
## Project Structure

```text
Cloud-guardian-ai/
│
├── architecture/          # Architecture diagrams
├── athena/                # Saved queries and views
├── glue/                  # ETL job scripts
├── lambda/                # Compliance evaluation functions
├── sample_data/           # Sample event payloads for testing
├── terraform/             # IaC — all AWS resources
├── tests/                 # Unit and integration tests
└── .github/               # CI/CD workflows
```

---

## Sample Compliance Checks

- **Public S3 Bucket Detection** — flags buckets with public ACLs or bucket policies
- **Missing Encryption Detection** — identifies unencrypted S3 objects and EBS volumes
- **Security Group Review** — detects overly permissive inbound rules (0.0.0.0/0)
- **Security Hub Critical Findings** — surfaces CRITICAL severity findings automatically
- **Compliance Violation Monitoring** — continuous Config rule evaluation and alerting

---

## Athena Analytics Examples

**Findings by severity:**
```sql
SELECT   severity,
         COUNT(*) AS total_findings
FROM     cloud_guardian_findings
GROUP BY severity
ORDER BY total_findings DESC;
```

**Top compliance issues:**
```sql
SELECT   issue,
         COUNT(*) AS occurrences
FROM     cloud_guardian_findings
GROUP BY issue
ORDER BY occurrences DESC;
```

---

## Security Dashboard Insights

- **Compliance Violations** — breakdown by rule and resource type
- **Risk Distribution** — severity heatmap across the environment
- **Critical Findings** — real-time feed of high-priority issues
- **Resource Security Trends** — compliance posture over time
- **Alert History** — SNS notification log and response tracking

---

## Deployment

### Prerequisites

- AWS account with appropriate IAM permissions
- [Terraform](https://developer.hashicorp.com/terraform/downloads) >= 1.5
- Python 3.11+
- [AWS CLI](https://aws.amazon.com/cli/) configured (`aws configure`)

### Deploy

```bash
# Clone the repository
git clone https://github.com/<your-org>/cloud-guardian-ai.git
cd cloud-guardian-ai

# Initialise and deploy infrastructure
terraform init
terraform plan
terraform apply
```

> **Note:** Review `terraform/variables.tf` to customise region, bucket names, and SNS endpoints before applying.

---

## Future Enhancements

- [ ] Automated remediation workflows (Lambda + Systems Manager)
- [ ] Multi-account AWS monitoring via AWS Organizations
- [ ] Expanded Security Hub integration (CIS, PCI-DSS benchmarks)
- [ ] Machine learning-based anomaly detection
- [ ] Cost optimization recommendations alongside security findings

---

## Author

**Siri**

Cloud Guardian AI demonstrates a modern, fully serverless approach to cloud compliance monitoring, risk assessment, security analytics, and operational visibility on AWS.

---

<div align="center">

![AWS](https://img.shields.io/badge/AWS-Serverless-FF9900?style=flat-square&logo=amazonaws&logoColor=white)
![Terraform](https://img.shields.io/badge/IaC-Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

</div>
