from flask.views import MethodView
from src.api.v1.models.blocklist import BlocklistModel
from flask_smorest import Blueprint
from flask_jwt_extended import (create_access_token,
                                create_refresh_token,
                                get_jwt_identity,
                                get_jwt,
                                jwt_required)
from src.api.v1.schemas.schemas import UserRegistrationSchema, UserSchema
from src.api.api_locker.safe_link_generator import base_api_secret_key
from src.logic.user import UserLogin, UserRegisteration, User

blp = Blueprint("Users", "users", description="Operations on users")


@blp.route(f'/register')
class UserRegisterApi(MethodView):
    @blp.arguments(UserRegistrationSchema)
    def post(self, user_data):
        print(type(user_data))
        return UserRegisteration.register(user_data)


@blp.route(f'/login')
class UserLoginApi(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        return UserLogin.login(user_data)


@blp.route(f'/logout')
class UserLogoutApi(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        Revoaked_Token = BlocklistModel(jti, 'User Logging out.')
        Revoaked_Token.save()
        return {'message': 'The user is successfully logged out.'}, 200


@blp.route(f'/user/<int:user_id>')
class UserApi(MethodView):
    @blp.response(200, UserSchema)  # i didn't get it
    def get(self, user_id):
        return User.get_user(user_id)

    def delete(self, user_id):
        return User.del_user(user_id)


@blp.route(f'/refresh')
class TokenRefreshApi(MethodView):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=True)
        jti = get_jwt()['jti']
        revoaked_token = BlocklistModel(
            jti, 'new refresh token is now in the place of this.')
        revoaked_token.save()
        return {'access_token': new_token}
