import os

import requests
from flask import Flask, jsonify, request

app = Flask(__name__)
USERS_URL = os.getenv("USERS_URL", "http://users:5000")
ORDERS = []


@app.get("/health")
def health():
    return jsonify(status="ok", service="orders")


@app.get("/orders")
def list_orders():
    return jsonify(ORDERS)


@app.post("/orders")
def create_order():
    data = request.get_json(silent=True) or {}
    if "user_id" not in data or "item" not in data:
        return jsonify(error="user_id and item are required"), 400

    try:
        resp = requests.get(f"{USERS_URL}/users/{data['user_id']}", timeout=2)
    except requests.RequestException:
        return jsonify(error="users service unavailable"), 503
    if resp.status_code == 404:
        return jsonify(error="user does not exist"), 400

    order = {"id": len(ORDERS) + 1, "user_id": data["user_id"], "item": data["item"]}
    ORDERS.append(order)
    return jsonify(order), 201
# trigger CI
