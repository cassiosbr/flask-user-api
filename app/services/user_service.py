from app.repositories.user_repository import UserRepository
from app.model.user import User

class UserService:
    # __init__ criado para injetar a dependência do UserRepository, facilitando testes e manutenção
    def __init__(self, user_repository=None):
        self.user_repository = user_repository or UserRepository()

    def create_user(self, name, email):
        user = User(name=name, email=email)
        return self.user_repository.add(user)

    def get_all_users(self):
        return self.user_repository.get_all()
    
    def get_user_by_id(self, user_id):
        return self.user_repository.get_by_id(user_id)