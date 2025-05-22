import sqlite3

conn = sqlite3.connect("devices.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS device_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mac TEXT,
    rssi INTEGER,
    timestamp REAL
)
''')

cursor.execute("INSERT INTO device_log (mac, rssi, timestamp) VALUES (?, ?, ?)",
               ("AA:BB:CC:DD:EE:FF", -45, 1716400000))
conn.commit()
conn.close()
print("Initialized devices.db with seed data.")
