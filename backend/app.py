from flask import Flask, request, jsonify
from cv.detect import detect_objects
from ml.features import extract_features
from ml.threat_classifier import classify_threat

app = Flask(__name__)


@app.route("/")
def home():

    return {
        "message": "AI Drone Surveillance Backend Running"
    }


@app.route("/detect", methods=["POST"])
def detect():

    file = request.files["image"]

    import numpy as np
    import cv2

    file_bytes = np.frombuffer(file.read(), np.uint8)
    frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    detections = detect_objects(frame)

    features = extract_features(detections)

    threat = classify_threat(features)

    return jsonify({
        "detections": detections,
        "threat_level": threat
    })


if __name__ == "__main__":

    app.run(debug=True)