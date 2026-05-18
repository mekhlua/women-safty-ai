# Smart Women Safety System — AI Backend

AI-powered risk detection backend for the Smart Women Safety System project.
Built by the CSE team at Adama Science and Technology University.

## Project Overview
This backend receives simulated sensor data (motion, sound, GPS) from the ECE hardware team,
analyzes it using a rule-based AI engine, and exposes a REST API for the SE website team.

## Team
- Mekhluqat Abdulwehab (CSE) — AI Engine & Backend
- Sumeya Akmel (CSE) — Flask API & Integration

## Folder Structure
  
women-safty-ai/
├── ai/
│   └── engine.py        # Rule-based risk detection logic
├── api/
│   ├── models.py        # Database models
│   └── routes.py        # Flask API endpoints
├── data/
│   └── sample_input.json
├── tests/
│   └── test_engine.py
├── app.py               # Flask entry point
├── serial_reader.py     # Arduino serial data reader
└── requirements.txt

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /analyze | Analyze sensor data, returns risk level |
| GET | /history | Get all past alerts |
| GET | /health | Check if server is running |

## Sample Request
```json
POST /analyze
{
  "accel_x": 15.0,
  "accel_y": -8.0,
  "accel_z": 3.0,
  "sos_pressed": false,
  "gps": { "lat": 23.02, "long": 72.57 }
}
```

## Sample Response
```json
{
  "risk_level": "HIGH",
  "reason": "Fall or impact detected",
  "gps": { "lat": 23.02, "long": 72.57 }
}
```

## Risk Levels
| Level | Trigger |
|-------|---------|
| CRITICAL | SOS button pressed |
| HIGH | Fall or sudden impact detected |
| MEDIUM | Abnormal movement detected |
| SAFE | Normal condition |