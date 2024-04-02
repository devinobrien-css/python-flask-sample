from flask import Flask, render_template, send_file
from src.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flasgger import Swagger

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    from src.routes.health_check import main_bp
    app.register_blueprint(main_bp)

    from src.routes.object_routes import objects_bp
    app.register_blueprint(objects_bp)

    from src.routes.openapi import openapi_bp
    app.register_blueprint(openapi_bp)

    return app