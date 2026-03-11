from ultralytics import YOLO

model = YOLO("models/yolov8n.pt")


def detect_objects(frame):

    results = model(frame)

    detections = []

    for r in results:

        for box in r.boxes:

            cls = int(box.cls[0])

            label = model.names[cls]

            detections.append(label)

    return detections