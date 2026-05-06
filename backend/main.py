from fastapi import FastAPI
from backend.traffic import analyze_traffic
from ml.detect import detect_vehicles

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API çalışıyor"}

@app.get("/traffic")
def get_traffic():
    data = analyze_traffic()
    return data

@app.get("/vehicles")
def get_vehicles():
    data = detect_vehicles()
    return data