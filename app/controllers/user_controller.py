from app import app
from flask import jsonify
from app.services.user_service import User_service
from app.forms.users.user_insert_form import User_insert_form

from flask import request


@app.get("/users")
def get_users():
    users = User_service.get_all()
    return jsonify([user.__dict__ for user in users])


@app.post("/user/create")
def create_user():

    form = User_insert_form.from_json(request.json)

    if form.validate():
        user = User_service.create(form)

        return jsonify(user.serialize())

    return jsonify(form.errors)
