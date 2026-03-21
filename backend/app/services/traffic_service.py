def calculate_density(vehicle_count, road_capacity=50):
    density = vehicle_count / road_capacity

    if density < 0.3:
        level = "low"
    elif density < 0.7:
        level = "medium"
    else:
        level = "high"

    return {
        "density_score": round(density, 2),
        "traffic_level": level
    }

from app.db.session import SessionLocal
from app.models.traffic import TrafficData

def save_to_db(vehicle_count, density, weather):
    db = SessionLocal()

    record = TrafficData(
        vehicle_count=vehicle_count,
        density_score=density["density_score"],
        traffic_level=density["traffic_level"],
        weather=weather
    )

    db.add(record)
    db.commit()
    db.close()