
from sqlalchemy.sql.expression import func
from backend.app.core.database import SessionLocal
from backend.app.models.models import Question

class QuestionRepository:
    def __init__(self):
        self.db = SessionLocal()

    def get_random_question(self) -> Question:
        # Return a single random question from the table
        return self.db.query(Question).order_by(func.random()).first()

    def close(self):
        self.db.close()
