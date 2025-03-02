# app/controllers/game_controller.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.app.services.game_service import GameService
from backend.app.models.models import Game

router = APIRouter(prefix="/games", tags=["games"])

class CreateGameRequest(BaseModel):
    user_id: str

@router.post("/", response_model=dict)
def create_game(payload: CreateGameRequest):
    game: Game = GameService.create_new_game(payload.user_id)
    if not game:
        raise HTTPException(status_code=400, detail="Failed to create a game.")
    return {
        "game_id": game.id,
        "user_id": game.user_id,
        "score": game.current_score,
        "is_active": game.is_active
    }

@router.get("/{game_id}", response_model=dict)
def get_game(game_id: str):
    game: Game = GameService.get_game(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found.")
    return {
        "game_id": game.id,
        "user_id": game.user_id,
        "score": game.current_score,
        "is_active": game.is_active
    }

@router.get("/{game_id}/score")
def get_score(game_id: str):
    game = GameService.get_game(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found.")
    return {"score": game.current_score}
