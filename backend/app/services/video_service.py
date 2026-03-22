import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

VEHICLE_CLASSES = [2, 3, 5, 7]


def start_video_detection(source="video.mp4"):
    """
    source seçenekleri:

    1️⃣ Video dosyası:
        source="video.mp4"

    2️⃣ Webcam:
        source=0

    3️⃣ Telefon kamerası (IP Camera):
        source="http://192.168.1.5:8080/video"
    """

    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print("❌ Video açılamadı")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (640, 480))  # performans

        results = model(frame)

        vehicle_count = 0

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])

                if cls in VEHICLE_CLASSES:
                    vehicle_count += 1

                    x1, y1, x2, y2 = map(int, box.xyxy[0])

                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        cv2.putText(frame, f"Vehicles: {vehicle_count}",
                    (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    2)

        cv2.imshow("Traffic Detection", frame)

        # q ile çık
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()