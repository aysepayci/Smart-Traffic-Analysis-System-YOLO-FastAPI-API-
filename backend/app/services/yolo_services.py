from ultralytics import YOLO

# COCO pretrained model
model = YOLO("yolov8n.pt")

# COCO class IDs (vehicles)
VEHICLE_CLASSES = [2, 3, 5, 7]  # car, motorcycle, bus, truck


def detect_vehicles(image_path):
    results = model(image_path)

    vehicle_count = 0
    detections = []

    for r in results:
        boxes = r.boxes

        for box in boxes:
            cls = int(box.cls[0])

            if cls in VEHICLE_CLASSES:
                vehicle_count += 1

                detections.append({
                    "class": int(cls),
                    "confidence": float(box.conf[0])
                })

    return {
        "vehicle_count": vehicle_count,
        "detections": detections
    }