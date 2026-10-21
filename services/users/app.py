from flask import Flask, jsonify, request

app = Flask(__name__)
USERS = {1: {"id": 1, "name": "Alice"}, 2: {"id": 2, "name": "Bob"}}


@app.get("/health")
def health():
    return jsonify(status="ok", service="users")


@app.get("/users")
def list_users():
    return jsonify(list(USERS.values()))


@app.get("/users/<int:user_id>")
def get_user(user_id):
    user = USERS.get(user_id)
    if not user:
        return jsonify(error="user not found"), 404
    return jsonify(user)


@app.post("/users")
def create_user():
    data = request.get_json(silent=True) or {}
    if "name" not in data:
        return jsonify(error="name is required"), 400
    new_id = max(USERS) + 1
    USERS[new_id] = {"id": new_id, "name": data["name"]}
    return jsonify(USERS[new_id]), 201
# trigger CI
