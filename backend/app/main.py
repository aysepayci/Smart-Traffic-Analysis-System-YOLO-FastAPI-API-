from fastapi import FastAPI, File, UploadFile
from app.services.yolo_service import detect_vehicles
import shutil
import os

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

    result = detect_vehicles(file_path)

    return result