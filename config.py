import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Base configuration class. Contains default configuration settings.
    """
    # Default settings
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = True

    # Settings applicable to all environments
    SECRET_KEY = os.getenv('SECRET_KEY', default='development')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    RESULT_BACKEND = os.getenv('RESULT_BACKEND')

    FILE_UPLOADS = './Metadata_Extraction_API/static/uploads/'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'metadata.db')
