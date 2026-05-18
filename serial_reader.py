import serial
import requests
import json
import time

SERIAL_PORT = "/dev/ttyUSB0"  # Linux — ECE will confirm exact port
BAUD_RATE = 9600
API_URL = "http://127.0.0.1:5000/analyze"

def read_serial():
    print("🔌 Connecting to Arduino...")
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print("✅ Connected!")

        while True:
            line = ser.readline().decode("utf-8").strip()
            if line:
                try:
                    sensor_data = json.loads(line)
                    print("📡 Received:", sensor_data)

                    response = requests.post(API_URL, json=sensor_data)
                    result = response.json()
                    print("🧠 Risk:", result["risk_level"], "-", result["reason"])

                    if result["risk_level"] in ["HIGH", "CRITICAL"]:
                        print("🚨 ALERT TRIGGERED!")

                except json.JSONDecodeError:
                    print("⚠️ Bad data:", line)

            time.sleep(0.5)

    except serial.SerialException as e:
        print("❌ Serial error:", e)

if __name__ == "__main__":
    read_serial()