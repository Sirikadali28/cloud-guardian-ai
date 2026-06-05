def calculate_risk(event):

    score = 0

    if event.get("public_access"):
        score += 50

    if event.get("unencrypted"):
        score += 30

    if event.get("unused_security_group"):
        score += 20

    if score >= 70:
        level = "CRITICAL"
    elif score >= 40:
        level = "HIGH"
    else:
        level = "MEDIUM"

    return {
        "risk_score": score,
        "risk_level": level
    }