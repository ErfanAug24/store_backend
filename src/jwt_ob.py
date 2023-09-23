from flask_jwt_extended import JWTManager, current_user
from src.api.v1.models.user import UserModel
from src.api.v1.models.blocklist import BlocklistModel
from flask import current_app

jwt = JWTManager()


@jwt.revoked_token_loader
def check_if_token_revoked(jwt_header, jwt_payload) -> bool:
    jti = jwt_payload['jti']
    token = BlocklistModel.find_by_jwtID(jti)
    return token is not None



@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return UserModel.find_by_id(id=identity)
