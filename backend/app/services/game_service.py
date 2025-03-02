
from typing import Optional

from backend.app.repositories.challenge_repository import ChallengeRepository
from backend.app.repositories.game_repository import GameRepository
from backend.app.models.models import Game

class GameService:
    @staticmethod
    def create_new_game(user_id: str) -> Game:
        repo = GameRepository()
        try:
            return repo.create_game(user_id)
        finally:
            repo.close()

    @staticmethod
    def get_game(game_id: str) -> Optional[Game]:
        repo = GameRepository()
        try:
            return repo.get_game(game_id)
        finally:
            repo.close()

    @staticmethod
    def update_score(game: Game, new_score: str) -> Game:
        repo = GameRepository()
        try:
            return repo.update_game_score(game, new_score)
        finally:
            repo.close()

    @staticmethod
    def recalculate_score(game: Game) -> Game:
        game_repo = GameRepository()
        challenge_repo = ChallengeRepository()

        try:
            challenges = challenge_repo.get_challenges_by_game(game.id)
            new_score = sum(1 for challenge in challenges if challenge.is_correct)
            return game_repo.update_game_score(game, str(new_score))

        finally:
            game_repo.close()
            challenge_repo.close()
