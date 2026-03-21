from fastapi import FastAPI, File, UploadFile
from app.services.yolo_service import detect_vehicles
from app.services.traffic_service import calculate_density
from app.services.api_service import get_weather
import shutil
import os
from app.db.base import Base
from app.db.session import engine
from app.services.traffic_service import calculate_density, save_to_db

Base.metadata.create_all(bind=engine)

app = FastAPI()

UPLOAD_DIR = "temp"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def root():
    return {"message": "Smart Traffic API running 🚀"}




@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    yolo_result = detect_vehicles(file_path)

    vehicle_count = yolo_result["vehicle_count"]

    density = calculate_density(vehicle_count)
    weather = get_weather()

    # 💾 DB'ye kaydet
    save_to_db(vehicle_count, density, weather)

    return {
        "vehicle_count": vehicle_count,
        "density": density,
        "weather": weather,
        "detections": yolo_result["detections"]
    }

from app.db.session import SessionLocal
from app.models.traffic import TrafficData

@app.get("/records")
def get_records():
    db = SessionLocal()
    data = db.query(TrafficData).all()
    db.close()

    return data