import argparse
import json
import random
import threading
import time
from datetime import datetime

import numpy as np
import paho.mqtt.client as mqtt

# --------------------------------------------------
# Configuration
# --------------------------------------------------

BROKER = "localhost"
PORT = 1883
TRUCK_ID = "truck01"

TOPIC_TEMP = f"logibridge/trucks/{TRUCK_ID}/temperature"
TOPIC_VIB = f"logibridge/trucks/{TRUCK_ID}/vibration"
TOPIC_DOOR = f"logibridge/trucks/{TRUCK_ID}/door"

TEMP_MEAN = 4.0
TEMP_STD = 0.3

VIB_MEAN = 0.45
VIB_STD = 0.05

ANOMALY_VIB_MEAN = 1.2
ANOMALY_VIB_STD = 0.15

TEMP_DRIFT = 0.08

# --------------------------------------------------
# MQTT Client
# --------------------------------------------------

client = mqtt.Client()

try:
    client.connect(BROKER, PORT, 60)
    print(f"Connected to MQTT Broker at {BROKER}:{PORT}")
except Exception as e:
    print("Failed to connect to MQTT Broker")
    print(e)
    exit()

client.loop_start()

# --------------------------------------------------
# Helper Function
# --------------------------------------------------


def current_time():
    return datetime.now().isoformat()


# --------------------------------------------------
# Temperature Sensor (1 Hz)
# --------------------------------------------------

def publish_temperature(mode):
    drift = 0.0

    while True:

        if mode in ["temp_drift", "combined"]:
            drift += TEMP_DRIFT

        temperature = np.random.normal(TEMP_MEAN + drift, TEMP_STD)

        payload = {
            "truck_id": TRUCK_ID,
            "timestamp": current_time(),
            "temperature": round(float(temperature), 2)
        }

        client.publish(TOPIC_TEMP, json.dumps(payload))
        print("Temperature:", payload)

        time.sleep(1)


# --------------------------------------------------
# Vibration Sensor (0.5 Hz)
# --------------------------------------------------

def publish_vibration(mode):

    while True:

        if mode in ["vibration", "combined"]:
            vibration = np.random.normal(
                ANOMALY_VIB_MEAN,
                ANOMALY_VIB_STD
            )
        else:
            vibration = np.random.normal(
                VIB_MEAN,
                VIB_STD
            )

        payload = {
            "truck_id": TRUCK_ID,
            "timestamp": current_time(),
            "vibration_rms": round(float(vibration), 3)
        }

        client.publish(TOPIC_VIB, json.dumps(payload))
        print("Vibration:", payload)

        time.sleep(2)


# --------------------------------------------------
# Door Sensor (Random Events)
# --------------------------------------------------

def publish_door():

    state = "CLOSE"

    while True:

        wait_time = random.randint(20, 60)
        time.sleep(wait_time)

        state = "OPEN" if state == "CLOSE" else "CLOSE"

        payload = {
            "truck_id": TRUCK_ID,
            "timestamp": current_time(),
            "event": state
        }

        client.publish(TOPIC_DOOR, json.dumps(payload))
        print("Door:", payload)


# --------------------------------------------------
# Main
# --------------------------------------------------

def main():

    parser = argparse.ArgumentParser(
        description="Cold Chain Sensor Simulator"
    )

    parser.add_argument(
        "--anomaly",
        choices=[
            "none",
            "temp_drift",
            "vibration",
            "combined"
        ],
        default="none",
        help="Select anomaly mode"
    )

    args = parser.parse_args()

    print("\n--------------------------------")
    print("LogiBridge Cold Chain Simulator")
    print("--------------------------------")
    print(f"Truck ID : {TRUCK_ID}")
    print(f"Mode     : {args.anomaly}")
    print("--------------------------------\n")

    temperature_thread = threading.Thread(
        target=publish_temperature,
        args=(args.anomaly,),
        daemon=True
    )

    vibration_thread = threading.Thread(
        target=publish_vibration,
        args=(args.anomaly,),
        daemon=True
    )

    door_thread = threading.Thread(
        target=publish_door,
        daemon=True
    )

    temperature_thread.start()
    vibration_thread.start()
    door_thread.start()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopping simulator...")
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()
