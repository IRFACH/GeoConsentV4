from flask import Flask, request, jsonify, send_from_directory
from flask_socketio import SocketIO, emit
from datetime import datetime

app = Flask(__name__, static_folder="../frontend")
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "dashboard.html")

@app.route("/location", methods=["POST"])
def location():
    data = request.json

    lat = data.get("lat")
    lon = data.get("lon")
    acc = data.get("accuracy")
    speed = data.get("speed", 0)
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Send live update via SocketIO
    socketio.emit("update_location", {
        "lat": lat,
        "lon": lon,
        "accuracy": acc,
        "speed": speed,
        "time": time
    })

    # Save log
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


if __name__ == "__main__":
    # Run Flask with SocketIO
    socketio.run(app, host="0.0.0.0", port=5000)
