from flask import Flask, render_template, jsonify
from scanner import scan, load_last

app = Flask(__name__)

NETWORK = "192.168.1.25/24"   
KNOWN = set()

@app.route("/")
def index():
    return render_template("dashboard.html")

@app.route("/api/last")
def api_last():
    return jsonify(load_last())

@app.route("/api/scan", methods=["POST"])
def api_scan():
    data = scan(NETWORK)
    global KNOWN
    new_ips = [d["ip"] for d in data["devices"] if d["ip"] not in KNOWN]
    KNOWN.update(d["ip"] for d in data["devices"])
    return jsonify({"data": data, "new_ips": new_ips})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
