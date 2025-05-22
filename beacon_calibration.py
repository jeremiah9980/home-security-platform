import time, math
from bluepy.btle import Scanner

print("Calibrating RSSI values...")
scanner = Scanner()

beacon_mac = input("Enter target beacon MAC: ")
readings = []
print("Collecting RSSI... (10 sec)")

start_time = time.time()
while time.time() - start_time < 10:
    devices = scanner.scan(1.0)
    for dev in devices:
        if dev.addr.lower() == beacon_mac.lower():
            readings.append(dev.rssi)
            print(f"RSSI: {dev.rssi} dBm")

if readings:
    avg_rssi = sum(readings) / len(readings)
    print(f"\nCalibrated RSSI: {avg_rssi:.2f} dBm")
else:
    print("No readings found for given MAC.")