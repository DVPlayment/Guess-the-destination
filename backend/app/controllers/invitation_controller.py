from fastapi import APIRouter, HTTPException

from backend.app.dto.models import CreateInvitationRequest
from backend.app.services.invitation_service import InvitationService
from backend.app.services.game_service import GameService

router = APIRouter(prefix="/invitations", tags=["invitations"])




@router.post("/", response_model=dict)
def create_invitation(payload: CreateInvitationRequest):
    invitation = InvitationService.create_invitation(payload.inviter_id, payload.game_id)
    invite_link = f"http://localhost:3000/invitations/{invitation.invite_code}"
    return {"invite_code": invitation.invite_code, "invite_link": invite_link}


@router.get("/{invite_code}", response_model=dict)
def get_invitation(invite_code: str):
    invitation = InvitationService.get_invitation(invite_code)
    if not invitation:
        raise HTTPException(status_code=404, detail="Invitation not found")

    score = None
    if invitation.game_id:
        game = GameService.get_game(invitation.game_id)
        score = game.current_score if game else "0"

    return {
        "invite_code": invitation.invite_code,
        "inviter_id": invitation.inviter_id,
        "game_id": invitation.game_id,
        "score": score,
    }
