from flask import Flask
from src.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    app.config.from_object(Config)

    # Initialize extensions/plugins
    db.init_app(app)

    # Register blueprints/routes
    from src.routes.health_check import main_bp
    app.register_blueprint(main_bp)

    from src.routes.object_routes import objects_bp
    app.register_blueprint(objects_bp)

    return app