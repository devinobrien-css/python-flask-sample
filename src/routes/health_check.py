from flask import Blueprint, jsonify
from sqlalchemy import text 
from src import db


main_bp = Blueprint('main', __name__)

@main_bp.route('/health', methods=['GET'])
def health_check():
    try:
        # Check if the database connection is working
        db.session.execute(text('SELECT 1'))
        db.session.commit()
        return jsonify({'message': 'Database connection is successful!'})
    except Exception as e:
        return jsonify({'error': f'Database connection error: {str(e)}'}), 500