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
    from src.routes.health_check import main_bp
    app.register_blueprint(main_bp)

    from src.routes.object_routes import objects_bp
    app.register_blueprint(objects_bp)

    return app