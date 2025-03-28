# Sensor Data Ingestion & Analytics Pipeline

![Looker Studio](assets/looker%20snip.png)

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

```bash
curl -X POST http://127.0.0.1:5000/process_sensor_data \
-H "Content-Type: application/json" \
-d '{
  "sensor_id": "5",
  "temperature": 25.5,
  "pressure": 1020,
  "humidity": 50.3,
  "timestamp": "2025-03-15T15:45:00Z"
}'
``` 
## Project Screenshots

![Flask Running](assets/data%20shell%20snip.png)
![Firestore](assets/firestore%20reading%20snip.png)
![Google Cloud Storage](assets/gcs%20snip.png)
![BigQuery](assets/big%20query%20snip.png)
![Looker Studio](assets/looker%20snip.png)

---

## 🧠 What I Learned

- 🛠️ **Built a manual ETL pipeline** using Google Cloud services to simulate real-world workflows  
- 🏠 **Stored structured sensor data** in Firestore (NoSQL) with JSON formatting  
- ☁️ **Uploaded raw JSON** to Google Cloud Storage for backup and pipeline processing  
- 🧹 **Debugged malformed JSON exports** and ensured integrity before loading into BigQuery  
- 📊 **Loaded and queried data** in BigQuery to understand scalable data warehouse operations

## 🧩 Challenges Faced

- 🧪 Debugging Firestore exports that returned malformed JSON due to nested structures
- ⚠️ Handling authentication issues with `gcloud` CLI when triggering BigQuery and Cloud Storage
- 🧵 Managing async behavior when sending multiple API calls in sequence
- 🔄 Understanding how to properly convert and format exported Firestore backups for BigQuery ingestion

## 🚀 Future Improvements

- 🔁 Automate the ETL process using **Cloud Functions** or **Cloud Dataflow** for real-time ingestion
- 📅 Schedule recurring BigQuery loads with **Cloud Scheduler** + **Cloud Pub/Sub**
- 🔐 Add authentication and API key validation to the Flask API
- 📈 Integrate a dashboard with **live visualizations** using tools like **Streamlit** or **Looker Studio Embedded**
- 🧪 Add unit and integration testing using **pytest** or **unittest**
