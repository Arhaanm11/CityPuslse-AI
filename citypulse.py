# CityPulse AI - Version 2.0
# Major update: AI congestion prediction and emergency vehicle priority

def collect_traffic_data(sensor_id, vehicle_count):
    print("Sensor", sensor_id, "reported", vehicle_count, "vehicles")

def display_traffic_status(status):
    print("Traffic Status:", status)

def predict_congestion(vehicle_count, threshold=50):
    if vehicle_count >= threshold:
        prediction = "High Congestion"
    else:
        prediction = "Normal Traffic"

    print("AI Prediction:", prediction)
    return prediction

def prioritize_emergency_vehicle(lane, emergency_vehicle):
    if emergency_vehicle:
        print("Emergency vehicle detected in lane", lane)
        print("Priority signal activated for lane", lane)
    else:
        print("Normal signal operation")
