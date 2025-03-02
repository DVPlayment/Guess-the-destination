
from backend.app.core.database import SessionLocal
from backend.app.models.models import User

class UserRepository:
    def __init__(self):
        self.db = SessionLocal()

    def create_user(self, username: str, password: str) -> User:
        user = User(username=username, password=password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_by_username(self, username: str) -> User:
        return self.db.query(User).filter(User.username == username).first()

    def close(self):
        self.db.close()
