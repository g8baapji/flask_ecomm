from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    db.init_app(app)

    # Import modules using their corresponding blueprint handlers
    from ecom.users.admin.views import mod as admin_module

    # Register blueprint
    app.register_blueprint(admin_module)

    return app
