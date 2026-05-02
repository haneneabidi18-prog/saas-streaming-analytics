import pandas as pd
import random
from datetime import datetime, timedelta

operators = ["MTN", "Orange", "Moov", "Airtel", "Vodacom"]
countries = ["Benin", "Cameroon", "Ivory Coast", "Senegal", "Rwanda", "Morocco"]
bundles = ["OTT Daily Pass", "OTT Weekly Pass", "Premium Sports Bundle", "Family Entertainment", "Zero-Rating Bundle"]
platforms = ["Mobile", "STB", "Smart TV", "Web"]
contents = ["Series A", "Movie C", "Sport Live", "Kids Show", "Documentary D"]

rows = []

start_date = datetime(2026, 1, 1)

for i in range(5000):
    timestamp = start_date + timedelta(minutes=i)

    bundle_price = random.choice([1.99, 4.99, 9.99, 14.99])
    usage_mb = random.randint(50, 5000)
    watch_time = random.randint(1, 120)
    revenue_share = round(bundle_price * random.uniform(0.3, 0.7), 2)

    rows.append({
        "timestamp": timestamp,
        "operator": random.choice(operators),
        "country": random.choice(countries),
        "bundle_name": random.choice(bundles),
        "platform": random.choice(platforms),
        "content_title": random.choice(contents),
        "views": 1,
        "watch_time_minutes": watch_time,
        "revenue": revenue_share,
        "bundle_price": bundle_price,
        "usage_mb": usage_mb,
        "arpu_uplift": round(random.uniform(0.1, 3.5), 2),
        "churn_risk": random.choice(["Low", "Medium", "High"]),
        "buffering_ratio": round(random.uniform(0.01, 0.45), 2),
        "startup_time_ms": random.randint(500, 9000),
        "error_code": random.choice(["", "", "", "BUFFERING_ERROR", "LOW_BITRATE", "AUTH_ERROR"])
    })

df = pd.DataFrame(rows)
df.to_csv("telco_bundle_streaming_data.csv", index=False)

print("CSV generated: telco_bundle_streaming_data.csv")