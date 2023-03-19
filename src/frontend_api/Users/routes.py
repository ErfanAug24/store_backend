from flask import redirect, url_for, request, jsonify, render_template
from flask_smorest import Blueprint
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from src.api.v1.resources.user import UserLogin, UserLogout, UserRegister, User

blp = Blueprint('users', __name__)
user_data = {"username": "erfan",
             "password": "261384",
             "email": "eshirkhanei261384@gmail.com"}


@blp.route('/get')
def get():
    return User.get(user_data,2)
