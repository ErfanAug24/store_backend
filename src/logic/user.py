from src.api.v1.models.blocklist import BlocklistModel
from src.api.v1.schemas.schemas import UserRegistrationSchema, UserSchema, user_register_schema
from src.api.v1.models.user import UserModel
from werkzeug.security import check_password_hash, generate_password_hash
from src.extention_tools.send_email import send_email
from flask_jwt_extended import (create_access_token,
                                create_refresh_token,
                                get_jwt_identity,
                                get_jwt,
                                jwt_required,
                                current_user,
                                get_current_user,
                                unset_access_cookies)
from flask import jsonify
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


class UserLogout:
    @classmethod
    @jwt_required()
    def logout(cls, identity, revoke_token=False):
        resp = jsonify(USER_LOGOUT)
        token = get_jwt()
        jti = token['jti']
        ttype = token['type']
        identity = get_jwt_identity()
        revoked_jwt = BlocklistModel(jti, "Logging out", identity, ttype)

        if revoke_token:
            unset_access_cookies(resp)

        revoked_jwt.save()
        return resp


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


class TokenRefresh:
    @classmethod
    @jwt_required(refresh=True)
    def refresh(cls):
        identity = get_jwt_identity()
        token = get_jwt()
        access_token = create_access_token(identity=current_user, fresh=True)
        jti = token['jti']
        ttype = token['type']
        revoked_token = BlocklistModel(
            jti, 'new refresh token is now in the place of this.', identity, ttype)
        return jsonify({'access_token': access_token})
