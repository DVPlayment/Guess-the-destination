
from typing import Optional
from backend.app.core.database import SessionLocal
from backend.app.models.models import Game

class GameRepository:
    def __init__(self):
        self.db = SessionLocal()

    def create_game(self, user_id: str) -> Game:
        # first disable any existing active game for this user
        active_games = self.db.query(Game).filter(
            Game.user_id == user_id, Game.is_active == True
        ).all()
        for ag in active_games:
            ag.is_active = False
            self.db.add(ag)

        new_game = Game(user_id=user_id, current_score="0", is_active=True)
        self.db.add(new_game)
        self.db.commit()
        self.db.refresh(new_game)
        return new_game

    def get_game(self, game_id: str) -> Optional[Game]:
        return self.db.query(Game).filter(Game.id == game_id).first()

    def update_game_score(self, game: Game, new_score: str) -> Game:
        game.current_score = new_score
        self.db.add(game)
        self.db.commit()
        self.db.refresh(game)
        return game

    def close(self):
        self.db.close()
