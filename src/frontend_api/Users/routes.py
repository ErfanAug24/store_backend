from flask import redirect, url_for, request, jsonify, render_template, Blueprint, flash
from flask_jwt_extended import jwt_required
from src.api.v1.resources.user import UserRegisterApi
from src.logic.user import UserRegisteration, UserLogin
from src.logic.error_handler.error_syntax import USER_CONFLICT,PERMISSION
blp = Blueprint('Users', __name__, template_folder="templates")


user_register = UserRegisterApi()


@blp.route('/signup', methods=["GET", "POST"])
def SignUp():
    user_date = {"username": request.form.get("username"),
                 "email": request.form.get("email"),
                 "password": request.form.get("password"),
                 "repassword": request.form.get("repassword")}
    if user_date.get("password") == user_date.get("repassword") and user_date.get("password"):
        result = UserRegisteration.register(user_date)
        if result.get("message") == USER_CONFLICT:
            flash(f"Error : {USER_CONFLICT}", "danger")
            return redirect(url_for("blp.SignUp"))
        flash("You Have Created An Account For Yourself.", "success")
        return redirect(url_for('blp.home'))
    flash("Please Type A Correct Password", "warning")
    return render_template('UserTemplates/SignUp.html')


@blp.route('/signin')
def SignIn():
    user_date = {"username": request.form.get("username"),
                 "email": request.form.get("email"),
                 "password": request.form.get("password")}
    if user_date.get("username"):
        result = UserLogin.login(user_date)
        if result.get("message")==PERMISSION:
            flash(PERMISSION,"danger")
            return redirect(url_for("blp.SignIn"))
        

        
    return render_template("UserTemplates/SignIn.html")
