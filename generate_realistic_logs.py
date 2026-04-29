import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# حجم البيانات
n = 100000

regions = ["FR", "MA", "EG", "AE"]
devices = ["ios", "android", "web", "smart_tv"]
cdns = ["akamai", "cloudfront", "cloudflare"]
videos = [f"vid_{i}" for i in range(1, 50)]

start_time = datetime(2026, 4, 29)

rows = []

for i in range(n):

    timestamp = start_time + timedelta(seconds=i)

    region = random.choice(regions)
    device = random.choice(devices)
    cdn = random.choice(cdns)
    video = random.choice(videos)

    # Base values (normal behavior)
    latency = int(np.random.normal(200, 50))
    bitrate = int(np.random.normal(3000, 500))
    status = 200

    # 🔥 FORCED ANOMALIES (strong for demo)

    # High latency (40%)
    if random.random() < 0.4:
        latency = int(np.random.normal(800, 150))

    # Errors (25%)
    if random.random() < 0.25:
        status = 500

    # Low bitrate (30%)
    if random.random() < 0.3:
        bitrate = int(np.random.normal(1000, 300))

    # High bitrate (cost issue) (25%)
    if random.random() < 0.25:
        bitrate = int(np.random.normal(4500, 400))

    # حماية القيم
    latency = max(50, latency)
    bitrate = max(500, bitrate)

    rows.append([
        timestamp.isoformat(),
        region,
        f"user_{i}",
        device,
        latency,
        bitrate,
        status,
        cdn,
        video
    ])

# إنشاء DataFrame
df = pd.DataFrame(rows, columns=[
    "timestamp",
    "region",
    "user_id",
    "device",
    "latency",
    "bitrate",
    "status",
    "cdn",
    "video_id"
])

# حفظ الملف
df.to_csv("realistic_big_logs.csv", index=False)

print("✅ File generated successfully: realistic_big_logs.csv")
print("Rows:", len(df))
print("Sample:")
print(df.head())