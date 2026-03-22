from sqlalchemy import Column, Integer, Float, String
from app.db.base import Base

class TrafficData(Base):
    __tablename__ = "traffic_data"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_count = Column(Integer)
    density_score = Column(Float)
    traffic_level = Column(String)
    weather = Column(String)

from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime

timestamp = Column(DateTime, default=datetime.utcnow)
