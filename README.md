# Sensor Data Ingestion & Analytics Pipeline

## Overview
This project demonstrates a **Flask-based ETL pipeline** that ingests sensor data, processes it, and loads it into **Google BigQuery** for analysis. The goal was to simulate a **real-world data engineering workflow**, using **Google Cloud services** to manage and analyze structured sensor data.

## Tech Stack
- **Backend:** Flask (Python API)
- **Database:** Firestore (NoSQL)
- **Storage:** Google Cloud Storage (GCS)
- **ETL Processing:** Python, gcloud CLI
- **Data Warehouse:** BigQuery (SQL-based analytics)

## ETL Process: Manual vs. Industry Standard

| **Step** | **Manual Process (This Project)** | **Industry Standard** |
|---------------|--------------------------------|--------------------------|
| **Extract (E)** | Firestore → JSON export to GCS | Cloud Dataflow auto-ingestion |
| **Transform (T)** | Python script to clean data | dbt / Cloud Dataflow |
| **Load (L)** | Manually loaded into BigQuery | BigQuery scheduled ingestion |

> **Key Learning:** Understanding how manual ETL maps to **automated cloud workflows** is crucial for real-world **data engineering roles**.

## How to Run
1. Clone the repo
2. Set up a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Start Flask API: `python main.py`
5. Send test data using:
```sh
curl -X POST http://127.0.0.1:5000/process_sensor_data \
-H "Content-Type: application/json" \
-d '{
"sensor_id": "5",
"temperature": 25.5,
"pressure": 1020,
"humidity": 50.3,
"timestamp": "2025-03-15T15:45:00Z"
}'
