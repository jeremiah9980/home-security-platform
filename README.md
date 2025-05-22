# Smart Home Security Platform

This platform uses Raspberry Pi, wireless beacons, Ring cameras, and AI to detect and alert you to the presence of known/unknown devices and people.

## Features
- BLE/Wi-Fi device detection with Wireshark
- Real-time dashboard (React)
- Flask backend API with SQLite
- Cloud sync to AWS S3
- Beacon calibration and signal analysis

## Getting Started

```bash
# Setup backend database
python db_init.py

# Run all services
docker-compose up --build
```

## API
- `GET /api/devices` – List devices with last seen timestamps.

## License
MIT
