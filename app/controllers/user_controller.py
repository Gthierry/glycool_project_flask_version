from app import app
from flask import jsonify
from app.services.user_service import User_service


@app.get("/users")
def get_users():
    users = User_service.get_all_users()
    return jsonify([user.__dict__ for user in users])


@app.post("/user/create")
def create_user(first_name, last_name, email, username):
    User_service.create_user(first_name, last_name, email, username)
    # Placeholder for user creation logic
    return jsonify({"message": "User created"}), 201
