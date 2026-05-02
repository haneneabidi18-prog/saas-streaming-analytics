import pandas as pd
import random
from datetime import datetime, timedelta

countries = ["France", "Morocco", "Senegal", "Tunisia", "Ivory Coast", "Cameroon"]
platforms = ["Mobile", "Web", "Smart TV", "Android TV", "iOS", "STB"]
contents = ["Series A", "Series B", "Movie C", "Documentary D", "Sport Live", "Kids Show"]
errors = ["", "", "", "BUFFERING_ERROR", "STARTUP_TIMEOUT", "LOW_BITRATE", "CDN_ERROR", "AUTH_ERROR"]

rows = []

start_date = datetime(2026, 1, 1)

for i in range(10000):
    timestamp = start_date + timedelta(minutes=i)

    country = random.choice(countries)
    platform = random.choice(platforms)
    content = random.choice(contents)

    buffering_ratio = round(random.uniform(0.01, 0.55), 2)
    startup_time_ms = random.randint(500, 12000)
    bitrate_kbps = random.randint(400, 6000)
    watch_time = random.randint(1, 90)

    revenue = round(random.uniform(0.01, 1.5), 2)

    error_code = random.choice(errors)

    rows.append({
        "timestamp": timestamp,
        "session_id": f"s{i}",
        "user_id": f"u{random.randint(1, 2500)}",
        "country": country,
        "platform": platform,
        "content_title": content,
        "views": 1,
        "watch_time_minutes": watch_time,
        "revenue": revenue,
        "buffering_ratio": buffering_ratio,
        "startup_time_ms": startup_time_ms,
        "bitrate_kbps": bitrate_kbps,
        "error_code": error_code
    })

df = pd.DataFrame(rows)
df.to_csv("big_streaming_qoe_logs.csv", index=False)

print("CSV generated: big_streaming_qoe_logs.csv")