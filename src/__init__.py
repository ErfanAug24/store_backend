from flask import Flask
from flask_jwt_extended import JWTManager
from flask_smorest import Api
from src.db import db
from src.schema import ma
from flask_migrate import Migrate
from src.email import mail
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
    
    # setting redis and queue
    # rq.init_app(app)

    # setting api

    return app
