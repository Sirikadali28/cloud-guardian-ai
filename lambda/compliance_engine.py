"""
Cloud Guardian AI - Compliance Engine
Evaluates AWS security events against compliance rules and triggers alerts.
"""

import json
import logging
import boto3
import os
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

sns = boto3.client("sns")

# Get SNS topic ARN from environment variable (set by Terraform)
SNS_TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN")

if not SNS_TOPIC_ARN:
    logger.warning("SNS_TOPIC_ARN environment variable not set. Alerts will not be published.")

def publish_alert(finding):
    """
    Publish a compliance finding to SNS.
    
    Args:
        finding (dict): Compliance finding with control, severity, message
        
    Raises:
        Logs error if SNS publish fails, does not raise exception
    """
    if not SNS_TOPIC_ARN:
        logger.warning(f"SNS not configured. Finding not published: {finding}")
        return
        
    try:
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject=f"Cloud Guardian Alert - {finding['severity']}",
            Message=json.dumps(finding, indent=2)
        )
        logger.info(f"Alert published for {finding['control']}")

    except Exception as e:
        logger.error(f"SNS publish failed: {str(e)}")


def evaluate_compliance(event):
    """
    Evaluate security compliance against event payload.
    
    Checks for:
    - Public S3 access (S3_PUBLIC_ACCESS)
    - Unencrypted resources (ENCRYPTION_REQUIRED)
    - Unused security groups (SECURITY_GROUP_REVIEW)
    
    Args:
        event (dict): AWS event containing resource metadata
        
    Returns:
        list: Compliance findings with control, severity, and message
        
    Example:
        >>> event = {"public_access": True}
        >>> findings = evaluate_compliance(event)
        >>> findings[0]['control']
        'S3_PUBLIC_ACCESS'
    """
    findings = []

    if event.get("public_access"):
        findings.append({
            "control": "S3_PUBLIC_ACCESS",
            "severity": "HIGH",
            "message": "Public resource detected"
        })

    if event.get("unencrypted"):
        findings.append({
            "control": "ENCRYPTION_REQUIRED",
            "severity": "HIGH",
            "message": "Unencrypted resource detected"
        })

    if event.get("unused_security_group"):
        findings.append({
            "control": "SECURITY_GROUP_REVIEW",
            "severity": "MEDIUM",
            "message": "Unused security group detected"
        })

    return findings


def lambda_handler(event, context):
    """
    AWS Lambda handler for Kinesis event processing.
    
    Processes Kinesis records, evaluates compliance, scores risks, and publishes alerts.
    
    Args:
        event (dict): Kinesis event with Records containing base64-encoded data
        context (LambdaContext): Lambda runtime context
        
    Returns:
        dict: Response with statusCode and list of findings processed
        
    Example Kinesis event:
        {
            "Records": [
                {
                    "kinesis": {
                        "data": "base64-encoded-json-payload"
                    }
                }
            ]
        }
    """
    logger.info("Cloud Guardian processing started")

    results = []

    records = event.get("Records", [])

    for record in records:

        try:

            payload = json.loads(
                record["kinesis"]["data"]
            )

            findings = evaluate_compliance(payload)

            for finding in findings:

                finding["resource"] = payload.get(
                    "resource_id",
                    "unknown"
                )

                finding["timestamp"] = (
                    datetime.utcnow().isoformat()
                )

                publish_alert(finding)

                results.append(finding)

        except Exception as e:

            logger.error(
                f"Record processing failed: {str(e)}"
            )

    logger.info(f"Processing completed. {len(results)} findings generated")
    
    return {
        "statusCode": 200,
        "findings": results
    }