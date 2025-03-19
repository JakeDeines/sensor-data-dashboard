import random
from flask import Flask, jsonify, request
from google.cloud import firestore, storage
import json
import time

app = Flask(__name__)

# Initialize Firestore
db = firestore.Client()
collection_name = "sensor_readings"

# Initialize Cloud Storage
storage_client = storage.Client()
bucket_name = "sensor-data-bucket-jd"  # Change this to your actual bucket name

def generate_sensor_data():
    """Generate random sensor data for testing"""
    return {
        "sensor_id": str(random.randint(1, 10)),  # Random sensor ID between 1-10
        "temperature": round(random.uniform(15.0, 35.0), 2),  # Temperature between 15-35°C
        "pressure": random.randint(900, 1100),  # Pressure between 900-1100 hPa
        "humidity": round(random.uniform(30.0, 70.0), 2),  # Humidity between 30-70%
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")  # ISO 8601 timestamp
    }

@app.route('/process_sensor_data', methods=['POST'])
def process_sensor_data():
    """Handles incoming sensor data"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON"}), 400

        # Save to Firestore
        doc_ref = db.collection(collection_name).add(data)

        # Save raw JSON log to Cloud Storage
        file_name = f"sensor_log_{doc_ref[1].id}.json"
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(file_name)
        blob.upload_from_string(json.dumps(data))

        return jsonify({"message": "Data received successfully", "doc_id": doc_ref[1].id}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Sensor API is running!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
