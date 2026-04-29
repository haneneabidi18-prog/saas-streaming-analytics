from fastapi import FastAPI, UploadFile, File
import pandas as pd
import uuid

app = FastAPI()


@app.get("/")
def home():
    return {"status": "running"}


@app.post("/upload-logs")
async def upload_logs(file: UploadFile = File(...)):

    file_id = str(uuid.uuid4())

    # Read CSV in chunks for performance (important for big files)
    chunks = pd.read_csv(file.file, chunksize=50000)

    total_latency = 0
    total_rows = 0
    max_latency = 0
    error_count = 0
    total_bitrate = 0

    for chunk in chunks:
        total_latency += chunk["latency"].sum()
        total_rows += len(chunk)
        max_latency = max(max_latency, chunk["latency"].max())
        error_count += (chunk["status"] != 200).sum()
        total_bitrate += chunk["bitrate"].sum()

    # Avoid division by zero
    if total_rows == 0:
        return {"error": "empty file"}

    return {
        "file_id": file_id,
        "avg_latency": float(total_latency / total_rows),
        "max_latency": int(max_latency),
        "avg_bitrate": float(total_bitrate / total_rows),
        "error_rate": float(error_count / total_rows)
    }