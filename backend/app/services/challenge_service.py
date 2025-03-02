
from typing import Optional

from backend.app.dto.models import ChallengeAnswerRequest
from backend.app.repositories.challenge_repository import ChallengeRepository
from backend.app.models.models import Challenge, Question, Game
from backend.app.services.game_service import GameService


class ChallengeService:
    @staticmethod
    def create_challenge(game_id: str, question_id: str) -> Challenge:
        repo = ChallengeRepository()
        try:
            return repo.create_challenge(game_id, question_id)
        finally:
            repo.close()

    @staticmethod
    def get_challenge(challenge_id: str) -> Optional[Challenge]:
        repo = ChallengeRepository()
        try:
            return repo.get_challenge(challenge_id)
        finally:
            repo.close()

    @staticmethod
    def update_challenge(challenge: Challenge) -> Challenge:
        repo = ChallengeRepository()
        try:
            return repo.update_challenge(challenge)
        finally:
            repo.close()

    @staticmethod
    def process_user_submission(challenge: Challenge, question: Question, game: Game, payload: ChallengeAnswerRequest) -> (str, bool):
        # Compare user_answer with correct answer
        correct_answer = question.destination_metadata.get("correct_answer", "")
        is_correct = (payload.user_answer.lower().strip() == correct_answer.lower().strip())

        # Update challenge
        challenge.user_answer = payload.user_answer
        challenge.is_correct = is_correct
        # increment attempts
        old_attempts = int(challenge.attempts)
        challenge.attempts = str(old_attempts + 1)
        ChallengeService.update_challenge(challenge)

        # If correct, update game score
        # if is_correct:
        #     new_score = str(int(game.current_score) + 1)
        #     GameService.update_score(game, new_score)
        GameService.recalculate_score(game)

        return correct_answer, is_correct
