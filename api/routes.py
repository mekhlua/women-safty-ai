from flask import Blueprint, request, jsonify
from ai.engine import detect_risk
from api.models import db, Alert

api = Blueprint("api", __name__)

@api.route("/analyze", methods=["POST"])
def analyze():
    sensor_data = request.get_json()
    if not sensor_data:
        return jsonify({"error": "No data provided"}), 400

    result = detect_risk(sensor_data)

    # Save to DB
    alert = Alert(
        risk_level=result["risk_level"],
        reason=result["reason"],
        lat=result["gps"].get("lat"),
        long=result["gps"].get("long")
    )
    db.session.add(alert)
    db.session.commit()

    return jsonify(result), 200

@api.route("/history", methods=["GET"])
def history():
    alerts = Alert.query.order_by(Alert.timestamp.desc()).all()
    return jsonify([{
        "id": a.id,
        "risk_level": a.risk_level,
        "reason": a.reason,
        "gps": {"lat": a.lat, "long": a.long},
        "timestamp": a.timestamp
    } for a in alerts]), 200

@api.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "running"}), 200