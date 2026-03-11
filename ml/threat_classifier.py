def classify_threat(features):

    score = 0

    score += features["person_count"] * 1
    score += features["vehicle_count"] * 2
    score += features["drone_detected"] * 5

    if score == 0:
        return "LOW"

    elif score <= 3:
        return "MEDIUM"

    elif score <= 6:
        return "HIGH"

    else:
        return "CRITICAL"