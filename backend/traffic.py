from ml.detect import detect_vehicles
import cv2

def analyze_traffic():
    cap = cv2.VideoCapture("traffic.mp4")

    ret, frame = cap.read()
    if not ret:
        return {"error": "No frame"}

    vehicle_count = detect_vehicles(frame)

    density = vehicle_count / 20
    density = min(density, 1.0)

    return {
        "vehicle_count": vehicle_count,
        "density_score": density
    }