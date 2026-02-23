from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

bp = Blueprint("auth", __name__)

@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data or not data.get("email"):
        return jsonify({"error": "Email não informado"}), 400

    # Simulando um email para testes. Em um cenário real, você verificaria o email e senha no banco de dados.
    access_token = create_access_token(identity=data["email"])
    return jsonify(access_token=access_token), 200