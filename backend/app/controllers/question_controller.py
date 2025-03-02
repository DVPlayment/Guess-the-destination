# app/controllers/question_controller.py

from fastapi import APIRouter
from backend.app.services.question_service import QuestionService
from backend.app.models.models import Question

router = APIRouter(prefix="/questions", tags=["questions"])

@router.get("/random", response_model=dict)
def get_random_question():
    question: Question = QuestionService.get_random_question()
    if not question:
        return {"message": "No questions available."}
    # Return only the ID so user can request clues
    return {"question_id": question.id}
