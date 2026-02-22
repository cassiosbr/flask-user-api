from app.repositories.user_repository import UserRepository
from app.model.user import User

class UserService:
    # __init__ criado para permitir a injeção de dependência do UserRepository, facilitando testes unitários
    def __init__(self, user_repository=None):
        self.user_repository = user_repository or UserRepository

    def create_user(self, name, email):

        if len(name) > 100:
            raise ValueError('Nome deve ter 100 caracteres ou menos')
        
        if User.query.filter_by(email=email).first():
            raise ValueError('Email já existe')
        return self.user_repository.create_user(name, email)

    def get_all_users(self):
        return self.user_repository.get_all_users()
    
    def get_user_by_id(self, user_id):
        return self.user_repository.get_user_by_id(user_id)