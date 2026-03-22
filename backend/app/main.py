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

from sqlalchemy import func

@app.get("/analytics")
def get_analytics():
    db = SessionLocal()

    total_records = db.query(TrafficData).count()
    avg_density = db.query(func.avg(TrafficData.density_score)).scalar()

    high_traffic = db.query(TrafficData).filter(
        TrafficData.traffic_level == "high"
    ).count()

    db.close()

    return {
        "total_records": total_records,
        "average_density": round(avg_density or 0, 2),
        "high_traffic_count": high_traffic
    }

from sqlalchemy import extract

@app.get("/analytics/hourly")
def hourly_analysis():
    db = SessionLocal()

    data = db.query(
        extract('hour', TrafficData.timestamp).label('hour'),
        func.avg(TrafficData.density_score)
    ).group_by('hour').all()

    db.close()

    return [{"hour": int(h), "avg_density": float(d)} for h, d in data]

from fastapi import FastAPI
from backend.traffic import analyze_traffic

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API çalışıyor"}

@app.get("/traffic")
def get_traffic():
    data = analyze_traffic()
    return data