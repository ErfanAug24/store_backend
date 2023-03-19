from flask import redirect, url_for, request, jsonify, render_template,Blueprint
from flask_jwt_extended import jwt_required
from src.api.v1.resources.user import UserRegisterApi

blp = Blueprint('blp', __name__,template_folder="templates")
user_data = {"username": "erfan",
             "password": "261384",
             "email": "eshirkhanei261384@gmail.com"}

user_register = UserRegisterApi()


@blp.route('/test')
def test():
    return render_template('base.html')

@blp.route('/signup', methods=["GET", "POST"])
def SignUp():
    return render_template('base.html')
