from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

bp = Blueprint('user_routes', __name__, url_prefix='/users')

@bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({'error': 'Nome e email são obrigatórios'}), 400

    user_service = UserService()
    try:
        user = user_service.create_user(name, email)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    return jsonify({'id': user.id, 'name': user.name, 'email': user.email}), 201

@bp.route('/', methods=['GET'])
def get_all_users():
    user_service = UserService()
    users = user_service.get_all_users()
    return jsonify([{'id': user.id, 'name': user.name, 'email': user.email} for user in users]), 200

@bp.route('/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user_service = UserService()
    user = user_service.get_user_by_id(user_id)
    if user:
        return jsonify({'id': user.id, 'name': user.name, 'email': user.email}), 200
    else:
        return jsonify({'error': 'User not found'}), 404