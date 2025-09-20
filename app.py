import os

import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Root endpoint
@app.route("/")
def home():
    return jsonify(message="Hello! Flask API is running 🚀")

# Echo endpoint (test POST requests)
@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json()
    return jsonify(received=data)

# Simple health check
@app.route("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    port = 5001 or os.getenv("PORT")
    app.run(debug=True, host="0.0.0.0", port=port)
