from app.domain.entities.user import User
from app.infrastructure.repositories import UserRepository

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, name: str, email: str):
        existing_user = self.repository.find_by_email(email)
        if existing_user:
            raise ValueError("E-mail já cadastrado!")

        user = User(name=name, email=email)
        return self.repository.save(user)