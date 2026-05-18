import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from ai.engine import detect_risk

# Test 1: SOS button pressed
def test_sos():
    data = {
        "accel_x": 0.1,
        "accel_y": 0.0,
        "accel_z": 9.8,
        "sos_pressed": True,
        "gps": {"lat": 23.02, "long": 72.57}
    }
    result = detect_risk(data)
    assert result["risk_level"] == "CRITICAL"
    print("✅ Test 1 passed:", result)

# Test 2: Fall detected
def test_fall():
    data = {
        "accel_x": 15.0,
        "accel_y": -8.0,
        "accel_z": 3.0,
        "sos_pressed": False,
        "gps": {"lat": 23.02, "long": 72.57}
    }
    result = detect_risk(data)
    assert result["risk_level"] == "HIGH"
    print("✅ Test 2 passed:", result)
# Test 3: Struggle
def test_struggle():
    data = {
        "accel_x": 8.0,  # bumped up
        "accel_y": -6.0,
        "accel_z": 3.0,
        "sos_pressed": False,
        "gps": {"lat": 23.02, "long": 72.57}
    }
    result = detect_risk(data)
    assert result["risk_level"] == "MEDIUM"
    print("✅ Test 3 passed:", result)

# Test 4: Safe
def test_safe():
    data = {
        "accel_x": 0.1,
        "accel_y": 0.2,
        "accel_z": 9.8,
        "sos_pressed": False,
        "gps": {"lat": 23.02, "long": 72.57}
    }
    result = detect_risk(data)
    assert result["risk_level"] == "SAFE"
    print("✅ Test 4 passed:", result)


test_sos()
test_fall()
test_struggle()
test_safe()