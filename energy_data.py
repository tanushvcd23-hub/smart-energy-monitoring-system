from influxdb_client import InfluxDBClient
import random
import time

print("Sending data...")

while True:
    meter = random.choice(["M101", "M102", "M103"])

    voltage = round(random.uniform(210, 240), 2)
    current = round(random.uniform(3, 10), 2)
    power = round(voltage * current, 2)

    print(
        f"{meter} | V:{voltage} I:{current} P:{power}"
    )

    time.sleep(2)
