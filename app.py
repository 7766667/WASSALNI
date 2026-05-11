from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid
from datetime import datetime

app = Flask(__name__)
CORS(app)

rides = []
drivers = []

@app.route("/")
def home():
    return jsonify({
        "app": "Wassalni API",
        "status": "running"
    })

@app.route("/api/request-ride", methods=["POST"])
def request_ride():
    data = request.get_json() or {}

    ride = {
        "id": str(uuid.uuid4()),
        "name": data.get("name"),
        "phone": data.get("phone"),
        "from": data.get("from"),
        "to": data.get("to"),
        "status": "pending",
        "created_at": datetime.now().isoformat()
    }

    rides.append(ride)
    return jsonify({"success": True, "ride": ride}), 201

@app.route("/api/rides", methods=["GET"])
def get_rides():
    return jsonify(rides)

@app.route("/api/register-driver", methods=["POST"])
def register_driver():
    data = request.get_json() or {}

    driver = {
        "id": str(uuid.uuid4()),
        "name": data.get("name"),
        "phone": data.get("phone"),
        "car_model": data.get("car_model"),
        "plate": data.get("plate"),
        "area": data.get("area"),
        "status": "available",
        "registered_at": datetime.now().isoformat()
    }

    drivers.append(driver)
    return jsonify({"success": True, "driver": driver}), 201

@app.route("/api/drivers", methods=["GET"])
def get_drivers():
    return jsonify(drivers)

if __name__ == "__main__":
    app.run(debug=True)