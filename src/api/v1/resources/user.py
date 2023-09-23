from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

from src.api.v1.schemas.schemas import UserRegistrationSchema, UserSchema
from src.api.api_locker.safe_link_generator import Permission_Required
from src.logic.user import UserLogin, UserRegisteration, User, UserLogout, TokenRefresh

blp = Blueprint("UsersApi", "usersapi", description="Operations on users")


@blp.route(f'/register')
@Permission_Required()
class UserRegisterApi(MethodView):
    @blp.arguments(UserRegistrationSchema)
    def post(self, user_data):
        return UserRegisteration.register(user_data)


@blp.route(f'/login')
@Permission_Required()
class UserLoginApi(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        return UserLogin.login(user_data)


@blp.route(f'/logout')
@Permission_Required()
class UserLogoutApi(MethodView):
    @jwt_required()
    def post(self):
        resp = UserLogout.logout(identity=get_jwt_identity())
        return resp


@blp.route(f'/user/<int:user_id>')
@Permission_Required()
class UserApi(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        return User.get_user(user_id)

    def delete(self, user_id):
        return User.del_user(user_id)


@blp.route(f'/refresh')
@Permission_Required()
class TokenRefreshApi(MethodView):
    @jwt_required(refresh=True)
    def post(self):
        resp = TokenRefresh.refresh()
        return resp
