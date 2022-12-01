import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """ Base configuration class """

    # Default settings
    FLASK_DEBUG=False
    TESTING=False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    WTF_CSRF_ENABLED=True

class DevelopmentConfig(Config):

      #Development settings...
      FLASK_DEBUG = True
      SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "database.db")}'

class TestingConfig(Config):

      #Testing settings...
      TESTING = True
      WTF_CSRF_ENABLED = False