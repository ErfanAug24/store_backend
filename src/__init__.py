from flask import Flask
from flask_jwt_extended import JWTManager
from flask_smorest import Api
from src.db import db
from src.schema import ma
from flask_migrate import Migrate
from src.email import mail
from src.api.v1.resources.user import blp as UserApiBlueprint
from src.api.v1.resources.product import blp as ProductApiBlueprint
# from src.rq_db import rq


def create_app(configClass):
    app = Flask(__name__)
    app.config.from_object(configClass)
    # setting api
    api = Api(app)

    # setting database
    db.init_app(app)

    # setting schema
    ma.init_app(app)

    # setting mail
    mail.init_app(app)
    # setting jwtmanager
    jwt = JWTManager(app)
    # setting redis and queue
    # rq.init_app(app)

    # setting api
    api.register_blueprint(UserApiBlueprint)
    api.register_blueprint(ProductApiBlueprint)
    return app
