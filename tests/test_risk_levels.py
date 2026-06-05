from lambda.risk_scoring import calculate_risk

def test_critical_risk():

    event = {
        "public_access": True,
        "unencrypted": True,
        "securityhub_critical": True
    }

    result = calculate_risk(event)

    assert result["risk_level"] == "CRITICAL"


def test_low_risk():

    event = {}

    result = calculate_risk(event)

    assert result["risk_level"] == "LOW"