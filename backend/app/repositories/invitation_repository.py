import uuid
from typing import Optional, List
from backend.app.core.database import SessionLocal
from backend.app.models.models import Invitation

class InvitationRepository:
    def __init__(self):
        self.db = SessionLocal()

    def create_invitation(self, inviter_id: str, game_id: str = None) -> Invitation:
        invite_code = str(uuid.uuid4())  # Use UUID as the invite code
        invitation = Invitation(
            inviter_id=inviter_id,
            game_id=game_id,
            invite_code=invite_code
        )
        self.db.add(invitation)
        self.db.commit()
        self.db.refresh(invitation)
        return invitation

    def get_invitation_by_code(self, invite_code: str) -> Optional[Invitation]:
        return self.db.query(Invitation).filter(Invitation.invite_code == invite_code).first()

    def close(self):
        self.db.close()
