from lambda.risk_scoring import calculate_risk

def test_high_risk():

    event = {
        "public_access": True,
        "unencrypted": True,
        "unused_security_group": True
    }

    result = calculate_risk(event)

    assert result["risk_level"] == "CRITICAL"