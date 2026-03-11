def extract_features(detections):
    """
    Convert detected objects into numerical features
    """

    features = {
        "person_count": 0,
        "vehicle_count": 0,
        "drone_detected": 0
    }

    for obj in detections:

        if obj == "person":
            features["person_count"] += 1

        elif obj in ["truck", "car", "tank"]:
            features["vehicle_count"] += 1

        elif obj == "drone":
            features["drone_detected"] = 1

    return features