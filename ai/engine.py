def detect_risk(sensor_data):
    accel_x = sensor_data.get("accel_x", 0)
    accel_y = sensor_data.get("accel_y", 0)
    accel_z = sensor_data.get("accel_z", 0)
    sos = sensor_data.get("sos_pressed", False)
    gps = sensor_data.get("gps", {})

    # Rule 1: SOS — always critical
    if sos:
        return {
            "risk_level": "CRITICAL",
            "reason": "SOS button pressed",
            "gps": gps
        }

    # Rule 2: Fall — sudden impact
    total_accel = (accel_x**2 + accel_y**2 + accel_z**2) ** 0.5
    if total_accel > 15:
        return {
            "risk_level": "HIGH",
            "reason": "Fall or impact detected",
            "gps": gps
        }

    # Rule 3: Struggle — abnormal motion
    if total_accel > 10:
        return {
            "risk_level": "MEDIUM",
            "reason": "Abnormal movement detected",
            "gps": gps
        }

    # Rule 4: Safe
    return {
        "risk_level": "SAFE",
        "reason": "Normal condition",
        "gps": gps
    }