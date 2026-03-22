from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_vehicles(frame):
    results = model(frame)

    vehicle_count = 0

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])

            if cls in [2, 3, 5, 7]:  # car, motorcycle, bus, truck
                vehicle_count += 1

    return vehicle_count