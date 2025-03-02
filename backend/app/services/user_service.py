
from backend.app.repositories.user_repository import UserRepository
from backend.app.models.models import User

class UserService:
    @staticmethod
    def create_user(username: str, password: str) -> User:
        repo = UserRepository()
        try:
            existing = repo.get_by_username(username)
            if existing:
                raise ValueError("Username already exists.")
            user = repo.create_user(username, password)
            return user
        finally:
            repo.close()

    @staticmethod
    def get_user_by_username(username: str) -> User:
        repo = UserRepository()
        try:
            return repo.get_by_username(username)
        finally:
            repo.close()
