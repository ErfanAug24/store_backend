from flask_smorest import Blueprint, abort
from flask.views import MethodView
from src.api.v1.schemas.schemas import UserSchema
from src.api.v1.models.user import UserModel
from werkzeug.security import check_password_hash

blp=Blueprint("Role",'role',description="Operations on Role")

@blp.route('/role')
class Role(MethodView):
    @blp.response(200)
    @blp.arguments(UserSchema)
    def post(self,user_data):
        user=UserModel.find_by_username(user_data['username'])
        if user and check_password_hash(user.password,user_data['password']):
            user.role 
            pass

        # should i leave it here ? work on this.