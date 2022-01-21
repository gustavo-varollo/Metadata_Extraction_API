import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()


def create_app():
    """
    Core function that creates the application
    """
    app = Flask(__name__, instance_relative_config=True)

    CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(CONFIG_TYPE)

    # HTML Templates
    from . import routes
    app.register_blueprint(routes.main)

    with app.app_context():
        # Create uploads
        from . import upload_controller
        app.register_blueprint(upload_controller.uploader)

        # Initialize DB
        db.init_app(app)
        db.create_all()

    return app

