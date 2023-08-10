from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .extensions import db


def create_app(config_name=None):
    app = Flask(__name__)

    app.config.from_object("config.Config")

    if config_name == "config.TestConfig":
        app.config.from_object("config.TestingConfig")

    db.init_app(app)

    migrate = Migrate(app, db)
    migrate.init_app(app, db)

    from .routes import bp as main_bp

    app.register_blueprint(main_bp)

    return app
