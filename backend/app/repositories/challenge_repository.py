
from typing import Optional
from backend.app.core.database import SessionLocal
from backend.app.models.models import Challenge
from sqlalchemy.orm import joinedload
from typing import List


class ChallengeRepository:
    def __init__(self):
        self.db = SessionLocal()

    def create_challenge(self, game_id: str, question_id: str) -> Challenge:
        challenge = Challenge(game_id=game_id, question_id=question_id)
        self.db.add(challenge)
        self.db.commit()
        self.db.refresh(challenge)
        return challenge

    def get_challenge(self, challenge_id: str) -> Optional[Challenge]:
        return self.db.query(Challenge).options(joinedload(Challenge.question), joinedload(Challenge.game)).filter(Challenge.id == challenge_id).first()

    def update_challenge(self, challenge: Challenge) -> Challenge:
        self.db.add(challenge)
        self.db.commit()
        self.db.refresh(challenge)
        return challenge

    def get_challenges_by_game(self, game_id: str) -> List[Challenge]:
        return self.db.query(Challenge).filter(Challenge.game_id == game_id).all()

    def close(self):
        self.db.close()

