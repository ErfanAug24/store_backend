from dotenv import load_dotenv
import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):

    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    PROPAGATE_EXCEPTIONS = os.getenv("PROPAGATE_EXCEPTIONS")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_BLACKLIST_TOKEN_CHECKS = os.getenv("JWT_BLACKLIST_TOKEN_CHECKS")
    API_TITLE = os.getenv("API_TITLE")
    API_VERSION = os.getenv("API_VERSION")
    OPENAPI_VERSION = "3.0.2"

    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PORT = os.getenv("MAIL_PORT")
    MAIL_USE_TSL = os.getenv("MAIL_USE_TSL")
    MAIL_USE_SSL = os.getenv("MAIL_USE_SSL")
    MAIL_SERVER = os.getenv("MAIL_SERVER")
