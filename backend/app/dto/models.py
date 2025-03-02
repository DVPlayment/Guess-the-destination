from pydantic import BaseModel, constr

class ChallengeCreateRequest(BaseModel):
    game_id: str
    question_id: str

class ChallengeAnswerRequest(BaseModel):
    user_answer: str

class UserCreateRequest(BaseModel):
    username: constr(strip_whitespace=True, min_length=1)
    password: constr(strip_whitespace=True, min_length=1)


class CreateInvitationRequest(BaseModel):
    inviter_id: str
    game_id: str = None