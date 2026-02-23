from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('user_routes', __name__, url_prefix='/users')

@bp.route('/', methods=['POST'])
@jwt_required()
def create_user():
    if not request.is_json:
        return jsonify({'error': 'Content-Type deve ser application/json'}), 415

    data = request.get_json()
    if not data:
        return jsonify({'error': 'JSON payload é obrigatório'}), 400
    
    name = data.get('name')
    email = data.get('email')

    user_service = UserService()
    try:
        user = user_service.create_user(name, email)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    return jsonify({'id': user.id, 'name': user.name, 'email': user.email}), 201

@bp.route('/', methods=['GET'])
@jwt_required()
def get_all_users():
    
    create_user = get_jwt_identity()
    print(f"Usuário autenticado: {create_user}")
    
    user_service = UserService()
    users = user_service.get_all_users()
    return jsonify([{'id': user.id, 'name': user.name, 'email': user.email} for user in users]), 200

@bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user_by_id(user_id):
    user_service = UserService()
    try:
        user = user_service.get_user_by_id(user_id)
        return jsonify({'id': user.id, 'name': user.name, 'email': user.email}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404