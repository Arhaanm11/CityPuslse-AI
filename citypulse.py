# CityPulse AI - Version 1.1
# Feature: basic traffic monitoring with traffic alert

def collect_traffic_data(sensor_id, vehicle_count):
    print("Sensor", sensor_id, "reported", vehicle_count, "vehicles")

def display_traffic_status(status):
    print("Traffic Status:", status)

def traffic_alert(vehicle_count):
    if vehicle_count > 50:
        print("Alert: Heavy Traffic Detected")
    else:
        print("Traffic Level: Normal")
