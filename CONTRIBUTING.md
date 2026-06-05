# Contributing to Cloud Guardian AI

Thank you for your interest in contributing to Cloud Guardian AI! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

This project adheres to the [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How to Contribute

### Reporting Bugs

Before creating a bug report, check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps which reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed after following the steps**
- **Explain which behavior you expected to see instead and why**
- **Include screenshots/logs if applicable**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the steps**
- **Describe the current behavior and expected behavior**
- **Explain why this enhancement would be useful**

### Pull Requests

- Fill in the required template
- Follow the Python and Terraform style guides
- Include appropriate test cases
- Update documentation as needed
- End all files with a newline

## Development Setup

### Prerequisites

- Python 3.11+
- Terraform >= 1.5
- AWS CLI configured
- Git

### Clone and Setup

```bash
# Clone the repository
git clone https://github.com/your-username/cloud-guardian-ai.git
cd cloud-guardian-ai

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r lambda/requirements.txt
pip install pytest pytest-cov boto3 moto  # For testing
```

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=lambda --cov-report=html

# Run specific test
pytest tests/test_risk_scoring.py::test_high_risk -v
```

### Code Style

#### Python

We follow PEP 8 style guide. Use tools to enforce it:

```bash
# Install linting tools
pip install flake8 black pylint

# Check code style
flake8 lambda/ tests/
black --check lambda/ tests/

# Auto-format (be careful!)
black lambda/ tests/
```

#### Terraform

```bash
# Format Terraform files
terraform fmt -recursive terraform/

# Validate
terraform validate -chdir=terraform

# Plan before apply (always!)
terraform plan -chdir=terraform
```

### Testing

- Write unit tests for new functions
- Use `pytest` for testing
- Mock AWS services using `moto` or `unittest.mock`
- Aim for >80% code coverage on new code

Example test:

```python
import pytest
from lambda.compliance_engine import evaluate_compliance

def test_evaluate_compliance_with_violations():
    """Test compliance evaluation with multiple violations."""
    event = {
        "public_access": True,
        "unencrypted": True,
    }
    findings = evaluate_compliance(event)
    
    assert len(findings) == 2
    assert findings[0]["severity"] == "HIGH"
    assert findings[1]["control"] == "ENCRYPTION_REQUIRED"

def test_evaluate_compliance_no_violations():
    """Test compliance evaluation with no violations."""
    event = {}
    findings = evaluate_compliance(event)
    
    assert len(findings) == 0
```

## Documentation

- Update README.md if your changes are user-visible
- Add docstrings to all new functions
- Update Deployment.md if deployment process changes
- Keep comments clear and concise

### Python Documentation Example

```python
def publish_alert(finding):
    """
    Publish a compliance finding to SNS topic for real-time alerts.
    
    This function sends critical findings to SNS for immediate notification
    to security teams.
    
    Args:
        finding (dict): Compliance finding with keys:
            - control (str): Control name
            - severity (str): One of HIGH, MEDIUM, LOW
            - message (str): Human-readable message
            - resource (str): AWS resource ID
            - timestamp (str): ISO format timestamp
            
    Returns:
        None
        
    Raises:
        Logs exceptions but doesn't raise to prevent blocking processing.
        
    Example:
        >>> finding = {
        ...     "control": "S3_PUBLIC_ACCESS",
        ...     "severity": "HIGH",
        ...     "message": "Public bucket detected",
        ...     "resource": "my-bucket",
        ...     "timestamp": "2026-06-05T08:00:00"
        ... }
        >>> publish_alert(finding)
    """
```

## Commit Messages

Use clear, descriptive commit messages:

```
Short (50 char or less) summary of changes

More detailed explanation of the changes if needed.
Wrap at 72 characters. Explain what and why, not how.

- Use bullets for lists
- Reference issues with #1234

Related to: #1234
```

Examples:

✅ Good:
```
Add unit tests for compliance engine

- Test evaluate_compliance with public_access flag
- Test evaluate_compliance with unencrypted flag
- Add mock SNS publishing tests

Fixes #42
```

❌ Bad:
```
fix bug
```

## Branch Naming

Use descriptive branch names:

- `feature/add-remediation` - New feature
- `fix/sns-topic-arn` - Bug fix
- `docs/update-readme` - Documentation
- `test/improve-coverage` - Tests
- `chore/upgrade-boto3` - Dependency updates

## Before Submitting

1. **Run tests locally**
   ```bash
   pytest tests/ -v
   ```

2. **Check code style**
   ```bash
   flake8 lambda/ tests/
   black --check lambda/ tests/
   ```

3. **Validate Terraform**
   ```bash
   terraform validate -chdir=terraform
   terraform fmt -check -recursive terraform/
   ```

4. **Update CHANGELOG**
   ```markdown
   ## [Unreleased]
   
   ### Added
   - Your new feature description
   ```

5. **Run the GitHub Actions workflow locally** (optional)
   ```bash
   # Using act: https://github.com/nektos/act
   act push
   ```

## Review Process

1. Submit your PR with clear description
2. Ensure CI/CD checks pass
3. Address review comments
4. Once approved, your PR will be merged

## License

By contributing to Cloud Guardian AI, you agree that your contributions will be licensed under the MIT License.

## Questions?

Feel free to open an issue for questions or discussions!

Thank you for contributing! 🚀
