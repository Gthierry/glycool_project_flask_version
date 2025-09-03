from app import app
from flask import jsonify


@app.get("/")
def index():
    return jsonify({"error": "invalid credentials"}), 401
