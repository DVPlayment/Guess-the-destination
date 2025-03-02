import uuid
import json
from datetime import datetime
from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.types import JSON
from sqlalchemy.orm import sessionmaker

# --- Database Setup ---
DATABASE_URL = "sqlite:///globetrotter.db"
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

# --- Schema Definition ---
class Question(Base):
    __tablename__ = "questions"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    destination_metadata = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Create the table
Base.metadata.create_all(engine)

# --- Ingest Data into SQLite ---
session = SessionLocal()

# Load data from destinations.json
with open("destinations.json", "r") as file:
    destinations = json.load(file)

# Insert each destination as a question
for dest in destinations:
    question_metadata = {
        "clues": dest["clues"],  # List of clues
        "funFacts": dest["funFacts"],  # List of fun facts
        "trivia": dest.get("trivia", []),  # Optional trivia
        "correct_answer": dest["name"]  # Correct answer is the city name
    }

    question_record = Question(
        destination_metadata=question_metadata
    )
    session.add(question_record)

# Commit and close
session.commit()
session.close()

print(f"Inserted {len(destinations)} questions into the database.")
