from flask import Flask
from src.config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions/plugins
    db.init_app(app)

    # Register blueprints/routes
    from src.routes import main_bp
    app.register_blueprint(main_bp)

    return app