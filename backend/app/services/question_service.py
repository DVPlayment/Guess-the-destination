
from backend.app.repositories.question_repository import QuestionRepository
from backend.app.models.models import Question

class QuestionService:
    @staticmethod
    def get_random_question() -> Question:
        repo = QuestionRepository()
        try:
            return repo.get_random_question()
        finally:
            repo.close()
