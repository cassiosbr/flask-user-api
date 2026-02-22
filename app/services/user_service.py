from app.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository=None):
        self.user_repository = user_repository or UserRepository

    def create_user(self, name, email):
        return self.user_repository.create_user(name, email)

    def get_all_users(self):
        return self.user_repository.get_all_users()
    
    def get_user_by_id(self, user_id):
        return self.user_repository.get_user_by_id(user_id)