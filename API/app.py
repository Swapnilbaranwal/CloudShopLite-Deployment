from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route("/")
def home():
    return jsonify({"message": "API running"})

@app.route("/count")
def count():
    value = r.incr("counter")
    background_jobs = r.get("background_jobs") or 0
    return jsonify({ "visits": value, "redis_host": redis_host, "background_jobs": background_jobs })

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)