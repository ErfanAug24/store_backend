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
        db.session.add(user)
        db.session.commit()
        


class UserLogin:
    pass


class UserLogout:
    pass


class User:
    pass


class TokenRefresh:
    pass
