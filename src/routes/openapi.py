from flask import Blueprint, send_file, render_template
from sqlalchemy import text 
from src import db

openapi_bp = Blueprint('openapi', __name__)

@openapi_bp.route('/openapi.yaml')
def get_spec():
    return send_file('../openapi.yaml', as_attachment=False)

@openapi_bp.route('/openapi')
def send_openapi_spec():
    return render_template('openapi.html')