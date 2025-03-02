from backend.app.repositories.invitation_repository import InvitationRepository

class InvitationService:
    @staticmethod
    def create_invitation(inviter_id: str, game_id: str = None):
        repo = InvitationRepository()
        try:
            return repo.create_invitation(inviter_id, game_id)
        finally:
            repo.close()

    @staticmethod
    def get_invitation(invite_code: str):
        repo = InvitationRepository()
        try:
            return repo.get_invitation_by_code(invite_code)
        finally:
            repo.close()
