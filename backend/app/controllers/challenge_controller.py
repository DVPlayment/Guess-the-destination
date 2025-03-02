
from fastapi import APIRouter, HTTPException

from backend.app.dto.models import ChallengeCreateRequest, ChallengeAnswerRequest
from backend.app.services.challenge_service import ChallengeService
from backend.app.models.models import Challenge, Game, Question

router = APIRouter(prefix="/challenges", tags=["challenges"])


@router.post("/", response_model=dict)
def create_challenge(payload: ChallengeCreateRequest):
    # Create a new challenge for a given game/question
    challenge: Challenge = ChallengeService.create_challenge(
        payload.game_id, payload.question_id
    )
    return {"challenge_id": challenge.id}

@router.get("/{challenge_id}/clue/{clue_number}", response_model=dict)
def get_clue(challenge_id: str, clue_number: int):
    challenge: Challenge = ChallengeService.get_challenge(challenge_id)
    if not challenge:
        raise HTTPException(status_code=404, detail="Challenge not found.")

    question = challenge.question
    if not question:
        raise HTTPException(status_code=404, detail="Question not found.")

    clues = question.destination_metadata.get("clues", [])
    if clue_number < 1 or clue_number > len(clues):
        raise HTTPException(status_code=400, detail="Invalid clue number.")

    return {"clue": clues[clue_number - 1]}

@router.post("/{challenge_id}/answer", response_model=dict)
def submit_answer(challenge_id: str, payload: ChallengeAnswerRequest):
    challenge: Challenge = ChallengeService.get_challenge(challenge_id)
    if not challenge:
        raise HTTPException(status_code=404, detail="Challenge not found.")

    question: Question = challenge.question
    if not question:
        raise HTTPException(status_code=404, detail="Question not found.")

    game: Game = challenge.game
    if not game:
        raise HTTPException(status_code=404, detail="Game not found.")

    correct_answer, is_correct = ChallengeService.process_user_submission(challenge, question, game, payload)

    return {
        "correct_answer": correct_answer,
        "is_correct": is_correct,
        "fun_facts": question.destination_metadata.get("funFacts", []),
    }
