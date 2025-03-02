
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey
from sqlalchemy.types import JSON
from sqlalchemy.orm import relationship
from backend.app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)  # TODO apply password_hashing logic
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class Question(Base):
    __tablename__ = "questions"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    destination_metadata = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class Game(Base):
    __tablename__ = "games"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    current_score = Column(String, default="0")  # Could store as int if you prefer
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user = relationship("User", backref="games")

class Challenge(Base):
    __tablename__ = "challenges"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    game_id = Column(String, ForeignKey("games.id"), nullable=False)
    question_id = Column(String, ForeignKey("questions.id"), nullable=False)
    attempts = Column(String, default="0")
    is_correct = Column(Boolean, default=False)
    user_answer = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    game = relationship("Game", backref="challenges")
    question = relationship("Question", backref="challenges")

class Invitation(Base):
    __tablename__ = "invitations"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    inviter_id = Column(String, ForeignKey("users.id"), nullable=False)
    game_id = Column(String, ForeignKey("games.id"), nullable=True)  # Optionally tie to a game
    invite_code = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
