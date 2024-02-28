from flask import Blueprint, jsonify, request
from models import User
from flask_jwt_extended import create_access_token, create_refresh_token


auth_bp = Blueprint('auth', __name__)

@auth_bp.post('/register')

def register_user():

    data = request.get_json()
    user = User.get_user_by_username(username=data.get("username"))

    if user is not None:
        return jsonify({"error": "User already exists"}), 403
    
    new_user = User(
        username = data.get("username"),
        email = data.get('email'),
    )

    new_user.create_password(password = data.get('password'))
    new_user.save()


    return jsonify({"message": "User Registered"}), 201

@auth_bp.post('/login')
def login():

    data = request.get_json()
    user = User.get_user_by_username(username = data.get('username'))

    if user and (user.confirm_password(password = data.get('password'))):
        access_token = create_access_token(identity= user.username)
        refresh_token = create_refresh_token(identity= user.username)
        return jsonify(
            {
                "message":"You have been logged in successfully",
                "tokens":{
                    "access": access_token,
                    "refresh": refresh_token,
                }
            }
        ),  200

    return jsonify({"error":"Invalid credentials"}),400




    