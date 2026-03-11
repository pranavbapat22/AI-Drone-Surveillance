import cv2
from cv.detect import detect_objects
from ml.features import extract_features
from ml.threat_classifier import classify_threat


def process_video(video_path):

    cap = cv2.VideoCapture(video_path)

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        detections = detect_objects(frame)

        features = extract_features(detections)

        threat = classify_threat(features)

        print("Detections:", detections)
        print("Threat Level:", threat)

        cv2.imshow("Drone Feed", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()