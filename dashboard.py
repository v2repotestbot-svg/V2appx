from flask import Flask, jsonify, request
from config import DASHBOARD_KEY

app = Flask(__name__)

STATS = {"processed":0,"success":0,"failed":0}

@app.route("/")
def home():
    key = request.args.get("key")
    if key != DASHBOARD_KEY:
        return "Unauthorized", 401
    return jsonify({
        "panel": "Ultra TXT Uploader Dashboard",
        "stats": STATS
    })

@app.route("/update", methods=["POST"])
def update():
    STATS.update(request.json)
    return {"ok": True}

if __name__ == "__main__":
    app.run("0.0.0.0", 8000)
  
