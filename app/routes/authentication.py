from flask import Blueprint, request, jsonify
from app.models import User

from app.extensions import db

bp = Blueprint("main", __name__)


@bp.route("/create_user", methods=["POST"])
def create_user():
    data = request.json
    new_user = User(email=data["email"], password=data["password"])
    db.session.add(new_user)
    try:
        db.session.commit()
        return jsonify({"message": "User created successfully"}), 201
    except Exception:
        db.session.rollback()
        return jsonify({"message": "Username or email already exists"}), 400


@bp.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    user_list = [
        {"id": user.id, "username": user.username, "email": user.email}
        for user in users
    ]
    return jsonify(user_list)
