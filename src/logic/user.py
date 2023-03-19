from src.api.v1.models.blocklist import BlocklistModel
from src.api.v1.schemas.schemas import UserRegistrationSchema, UserSchema, user_register_schema
from src.api.v1.models.user import UserModel
from werkzeug.security import check_password_hash, generate_password_hash
from src.extention_tools.send_email import send_email
from flask_jwt_extended import (create_access_token,
                                create_refresh_token,
                                get_jwt_identity,
                                get_jwt,
                                jwt_required)
from src.logic.error_handler.error_syntax import *


class UserRegisteration(UserModel):
    @classmethod
    def register(cls, user_json):
        user = cls.find_by_username(user_json.get("username"))
        if user:
            return {'message': USER_CONFLICT}

        user = cls(user_json["username"],
                   user_json["email"],
                   generate_password_hash(user_json["password"]))

        token = "SIPER SECRET KEY"
        user.save()

        # send email in here with async

        return {'message': USER_CREATION,
                'user info': user_register_schema.dump(obj=user)}


class UserLogin(UserModel):

    @classmethod
    def login(cls, user_json):
        user = cls.find_by_username(user_json.get("username"))
        if user and check_password_hash(user.password, user_json.get("password")):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(identity=user.id)
            return {'access_token': access_token,
                    'refresh_token': refresh_token}, 200
        return {'message': PERMISSION}


class User(UserModel):
    @classmethod
    def get_user(cls, user_id: int):
        return user_register_schema.dump(cls.find_by_id(user_id))

    @classmethod
    def del_user(cls, user_id: int):
        user = cls.find_by_id(user_id)
        user.delete()
        return {'message': USER_DELETE}
