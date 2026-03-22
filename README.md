# Smart Traffic Analysis System (YOLO + FastAPI + API)

## Overview

This project is a **real-time traffic analysis system** that uses **YOLO (You Only Look Once)** for vehicle detection and integrates external APIs (weather, maps) to provide **traffic density analysis and predictions**.

The system is designed with a **scalable microservice architecture** and can be extended for smart city applications.

---

## Features

* Real-time vehicle detection using YOLOv8
* Traffic density calculation
* Weather API integration
* Map-based visualization (frontend)
* FastAPI backend (high performance)
* Dockerized deployment
* Scalable architecture

---

## System Architecture

```
Camera → YOLO Detection → Vehicle Counter → Traffic Analyzer
       → External APIs (Weather)
       → Database → API → Frontend Dashboard
```

---

## Tech Stack

### Backend

* FastAPI
* Python
* PostgreSQL

### ML

* YOLOv8 (Ultralytics)
* OpenCV

### Frontend

* React

### DevOps

* Docker
* Nginx

---

## Project Structure

```
backend/     → API & business logic
ml/          → training & model files
frontend/    → UI dashboard
infra/       → deployment configs
scripts/     → helper scripts
```

---

## Installation

### 1. Clone the repo

```bash
git clone https://github.com/aysepayci/smart-traffic-yolo.git
cd smart-traffic-yolo
```

### 2. Setup environment

```bash
cp .env.example .env
```

### 3. Run with Docker

```bash
docker-compose up --build
```

---

##  API Endpoints

### Detect Vehicles

```
POST /detect
```

### Get Traffic Data

```
GET /traffic
```

### Get Analytics

```
GET /analytics
```

---

##  Running Tests

```bash
pytest backend/tests
```

---

##  Example Output

```json
{
  "vehicle_count": 23,
  "density_score": 0.76,
  "weather": "rainy"
}
```

---

##  Challenges & Solutions

| Problem             | Solution          |
| ------------------- | ----------------- |
| Low light detection | Data augmentation |
| API latency         | Caching           |
| High load           | Async processing  |

---

##  Future Improvements

* Multi-camera tracking (DeepSORT)
* Traffic prediction (LSTM)
* Edge deployment (Jetson Nano)
* Mobile app integration

---

