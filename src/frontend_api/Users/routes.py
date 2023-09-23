import datetime
from flask import redirect, url_for, request, render_template, Blueprint, flash
from flask_jwt_extended import jwt_required, set_access_cookies, set_refresh_cookies

from src.logic.user import *
from src.logic.error_handler.error_syntax import *
blp = Blueprint('Users', __name__, template_folder="templates")


@blp.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        auth = request.form
        if auth and auth.get("password") == auth.get("repassword"):
            resp = UserRegisteration.register(auth)
            if resp.get("message") == USER_CREATION:
                flash(USER_CREATION, 'success')
                return redirect(url_for('Users.SignIn'))
            else:
                flash(resp, 'danger')
        else:
            flash(TYPE_PASSWORD, 'warning')
    return render_template('UserTemplates/SignUp.html')


@blp.route('/signin', methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        auth = request.form
        user = UserModel.find_by_username(auth.get("username"))
        if not user:
            flash(ACCOUNT_REQUIRED, 'warning')
            return redirect(url_for("Users.SignUp"))
        if user and check_password_hash(user.password, auth.get("password")):
            resp = redirect(
                url_for("Stores.home", current_user=True))
            result = UserLogin.login(auth)
            set_access_cookies(resp, result.get("access_token"))
            set_refresh_cookies(resp, result.get("refresh_token"))
            flash(USER_LOGIN, 'success')
            return resp
        else:
            flash(WRONG_DATA, 'danger')
    return render_template("UserTemplates/SignIn.html")


@blp.route('/logout', methods=["GET", "POST"])
@jwt_required()
def Logout():
    UserLogout.logout()
    flash(USER_LOGOUT, 'success')
    return redirect(url_for("Users.home"))


@blp.route('/protected', methods=["GET", "POST"])
@jwt_required()
def protected():
    return {"message": "this link is working"}


@blp.route('/account')
def Account():
    return render_template("UerTemplates/Account.html")


@blp.route('/edit-account')
def Edit_Account():
    return render_template("UerTemplates/Account.html")
