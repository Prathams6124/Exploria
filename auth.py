from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, unset_jwt_cookies

auth_bp = Blueprint('auth', __name__)

USERS = {"admin": "password123"}  # simple user store

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    if data["username"] in USERS and USERS[data["username"]] == data["password"]:
        token = create_access_token(identity=data["username"])
        return jsonify(token=token), 200
    return jsonify({"msg": "Bad username or password"}), 401

@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    response = jsonify({"msg": "Logged out"})
    unset_jwt_cookies(response)
    return response
