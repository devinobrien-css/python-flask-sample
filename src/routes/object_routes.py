from flask import Blueprint, jsonify, request
from dataclasses import asdict
from src import db
from src.models import Object

objects_bp = Blueprint('objects', __name__)

@objects_bp.route('/objects', methods=['GET'])
def get_objects():
    objects = Object.query.all()
    object_list = [asdict(object) for object in objects]
    return jsonify({'objects': object_list}), 200

@objects_bp.route('/objects/<int:object_id>', methods=['GET'])
def get_object(object_id):
    task = Object.query.get_or_404(object_id)
    return jsonify({'object': asdict(task)}), 200

@objects_bp.route('/objects', methods=['POST'])
def create_object():
    data = request.get_json()
    new_object = Object(**data)
    db.session.add(new_object)
    db.session.commit()
    return jsonify({'object': asdict(new_object)}), 201

@objects_bp.route('/objects/<int:object_id>', methods=['PATCH'])
def update_object(object_id):
    data = request.get_json()
    existing_object = Object.query.get_or_404(object_id)
    for key, value in data.items():
        setattr(existing_object, key, value)
    db.session.commit()
    return jsonify({'object': asdict(existing_object)}), 200

@objects_bp.route('/objects/<int:object_id>', methods=['DELETE'])
def delete_object(object_id):
    existing_object = Object.query.get_or_404(object_id)
    db.session.delete(existing_object)
    db.session.commit()
    return '', 204