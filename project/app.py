from flask import Flask
from flask_mongoengine import MongoEngine
from project.config import BaseConfig
import os

db = MongoEngine()


def create_app() -> Flask:
    """
    Flask application factory
    :return: the flask app
    """
    app = Flask("TinyUrl")

    app_settings = os.getenv("FLASK_CONFIG", BaseConfig)
    app.config.from_object(app_settings)
    app.config['MONGODB_SETTINGS'] = {
        'db': 'tinyUrlDataBase'}

    # Initialize Database
    db.init_app(app)

    from project.api.tinyurl_api import tinyurl_api_bp

    url_prefix = app.config["URL_PREFIX"]
    app.register_blueprint(tinyurl_api_bp, url_prefix=url_prefix)

    return app
