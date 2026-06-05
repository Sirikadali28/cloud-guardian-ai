# Changelog

All notable changes to Cloud Guardian AI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-06-05

### Added

- Initial release of Cloud Guardian AI
- Serverless AWS compliance monitoring platform
- Real-time event processing with Amazon Kinesis
- AWS Lambda compliance evaluation engine
- Automated risk scoring system
- SNS-based alert notifications (email/SMS)
- S3 data lake for findings storage (JSON/Parquet)
- AWS Glue ETL pipeline for data cataloging
- Amazon Athena for SQL analytics over findings
- Terraform Infrastructure as Code for reproducible deployment
- GitHub Actions CI/CD workflow
- Sample test data for AWS services
- Comprehensive README and deployment guide

### Features

- [x] Public S3 bucket detection
- [x] Unencrypted resource detection
- [x] Security group overly permissive rule detection
- [x] Real-time compliance evaluation
- [x] Risk severity scoring (CRITICAL/HIGH/MEDIUM/LOW)
- [x] Automated alerts via SNS
- [x] Centralized findings storage
- [x] Data lake ETL pipeline

### Security

- Uses IAM roles with least privilege access
- Environment variable configuration (no hardcoded credentials)
- Supports AWS Secrets Manager integration

### Documentation

- Architecture diagram included
- Step-by-step deployment guide
- Sample Athena SQL queries
- Contributing guidelines
- Security reporting instructions

## [Unreleased]

### Planned for v1.1

- [ ] Automated remediation workflows (Lambda + Systems Manager)
- [ ] Multi-account AWS monitoring via AWS Organizations
- [ ] Expanded Security Hub integration (CIS, PCI-DSS, HIPAA benchmarks)
- [ ] Machine learning-based anomaly detection
- [ ] Cost optimization recommendations alongside security findings
- [ ] Custom rule builder UI
- [ ] Slack/Teams webhook integrations
- [ ] Database backend for findings (RDS/DynamoDB)
- [ ] QuickSight dashboard templates
- [ ] Mobile app for alert monitoring

### Planned for v1.2

- [ ] AWS Config rule auto-remediation
- [ ] CloudFormation template auto-generation
- [ ] SaaS hosting option
- [ ] API for third-party integrations

---

## Migration Guides

### Upgrading from v0.x to v1.0

No prior versions exist. This is the initial release.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute improvements.

---

## Security

See [SECURITY.md](SECURITY.md) for security reporting instructions.
