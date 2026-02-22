from flask import Flask
from app.core.config import Config
from app.core.extensions import db
from app.routes.user_routes import bp as user_routes_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()
    
    app.register_blueprint(user_routes_bp)

    return app