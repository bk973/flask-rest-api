import os
from flask import Flask
from flask_marshmallow import Marshmallow

def create_app():
    app = Flask(__name__)

    #configure the flask app instance
    CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(CONFIG_TYPE)

    initialize_extensions(app)
    register_blueprints(app)

    return app


def register_blueprints(app):
    from .auth import auth_blueprint
    from .main import main_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(main_blueprint)

def initialize_extensions(app):
    from .Models import db, ma
    db.init_app(app)
    ma.init_app(app)

def register_error_handlers(app):
    pass

def configure_logging(app):
    pass