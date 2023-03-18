from flask.views import MethodView
from src.api.v1.models.blocklist import BlocklistModel
from flask_smorest import Blueprint, abort
from flask_jwt_extended import (create_access_token,
                                create_refresh_token,
                                get_jwt_identity,
                                get_jwt,
                                jwt_required)
from src.api.v1.schemas.schemas import UserRegistrationSchema, UserSchema
from src.api.v1.models.user import UserModel
from werkzeug.security import check_password_hash, generate_password_hash
from src.extention_tools.send_email import send_email
from src.api.api_locker.safe_link_generator import base_api_secret_key


blp = Blueprint("Users", "users", description="Operations on users")


@blp.route(f'{base_api_secret_key}/register')
class UserRegister(MethodView):
    @blp.arguments(UserRegistrationSchema)
    def post(self, user_data):
        if UserModel.find_by_username(user_data["username"]):
            abort(409, message="This username is already exist.")
        user = UserModel(user_data["username"],
                         user_data["email"],
                         generate_password_hash(user_data["password"]))
        token = "Super Secret Key"
        user.save()
        # send_email("احراز هویت شما", user_data["email"], body=f"""لطفا برای تایید صحت ایمیل خود بر لینک زیر کلیک کرده
        # https://VpnShop.ir/authenticating/{token}  واگر شما نقشی در ارسال این ایمیل نداشته اید . این پیام را نادیده بگیرید""")
        return {"message": "User created successfully."}, 201


@blp.route(f'{base_api_secret_key}/login')
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel.find_by_username(user_data['username'])
        if user and check_password_hash(user.password, user_data['password']):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {"access token": access_token,
                    "refresh token": refresh_token}
        abort(401, message="Invalid credentials")


@blp.route(f'{base_api_secret_key}/logout')
class UserLogout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        Revoaked_Token = BlocklistModel(jti, 'User Logging out.')
        Revoaked_Token.save()
        return {'message': 'The user is successfully logged out.'}, 200


@blp.route(f'{base_api_secret_key}/user/<int:user_id>')
class User(MethodView):
    @blp.response(200, UserSchema)  # i didn't get it
    def get(self, user_id):
        return UserModel.query.filter_by(id=user_id).first()

    def delete(self, user_id):
        user = UserModel.find_by_id(user_id)
        user.delete()
        return {"message": "User deleted ."}, 200


@blp.route(f'{base_api_secret_key}/refresh')
class TokenRefresh(MethodView):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=True)
        jti = get_jwt()['jti']
        revoaked_token = BlocklistModel(
            jti, 'new refresh token is now in the place of this.')
        revoaked_token.save()
        return {'access_token': new_token}
