from flask import Flask, render_template
from flask_smorest import Api
from src.db import db
from src.schema import ma
from src.email import mail
from src.jwt_ob import jwt
from src import config

from src.api.v1.resources.user import blp as UserApiBlueprint
from src.api.v1.resources.product import blp as ProductApiBlueprint
from src.frontend_api.Users.routes import blp as UserBlueprint
from src.frontend_api.Store.routes import blp as StoreBlueprint
# from src.rq_db import rq


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_object("src.config.Config")
    app.config.from_object("src.config.Mail_Config")
    app.config.from_object("src.config.JWT_Config")
    app.config.from_object("src.config.API_Config")

    register_extentions(app)
    register_blueprints(app)

    return app


def register_extentions(app):
    api = Api(app)
    jwt.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    mail.init_app(app)
    register_api(api)


def register_blueprints(app):
    app.register_blueprint(UserBlueprint)
    app.register_blueprint(StoreBlueprint)


def register_api(api):
    api.register_blueprint(UserApiBlueprint)
    api.register_blueprint(ProductApiBlueprint)


def error_handeling(app):
    @app.errorhandler(404)
    def error_404(error):
        return render_template("404.html"), 404
