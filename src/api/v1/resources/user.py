from flask.views import MethodView
from src.db import db
from flask_smorest import Blueprint, abort
from flask_jwt_extended import (create_access_token,
                                create_refresh_token,
                                get_jwt_identity,
                                get_jwt,
                                jwt_required)
from src.api.v1.schemas.schemas import UserRegistrationSchema
from src.api.v1.models.user import UserModel
from werkzeug.security import check_password_hash, generate_password_hash
from src.extention_tools.send_email import send_email
import os

blp = Blueprint("Users", "users", description="Operations on users")


@blp.route('/register')
class UserRegister:
    @blp.arguments(UserRegistrationSchema)
    def post(self, user_data):
        if UserModel.find_by_username(user_data["username"]):
            abort(409, message="This username is already exist.")
        user = UserModel(user_data["username"],
                         user_data["email"],
                         generate_password_hash(user_data["password"]))
        token = "Super Secret Key"
        db.session.add(user)
        db.session.commit()
        send_email("احراز هویت شما", user_data["email"], body=f"""لطفا برای تایید صحت ایمیل خود بر لینک زیر کلیک کرده
        https://VpnShop.ir/authenticating/{token}  واگر شما نقشی در ارسال این ایمیل نداشته اید . این پیام را نادیده بگیرید""")
        return {"message": "User created successfully."}, 201


class UserLogin:
    pass


class UserLogout:
    pass


class User:
    pass


class TokenRefresh:
    pass
