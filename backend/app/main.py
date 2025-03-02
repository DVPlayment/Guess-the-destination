
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.core.database import Base, engine
from backend.app.controllers.user_controller import router as user_router
from backend.app.controllers.game_controller import router as game_router
from backend.app.controllers.question_controller import router as question_router
from backend.app.controllers.challenge_controller import router as challenge_router
from backend.app.controllers.invitation_controller import router as invitation_router

def create_tables():
    Base.metadata.create_all(bind=engine)

def get_application():
    create_tables()
    app = FastAPI(title="Globetrotter Service")

    origins = ["http://localhost:3000"] # React app address
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(user_router)
    app.include_router(game_router)
    app.include_router(question_router)
    app.include_router(challenge_router)
    app.include_router(invitation_router)

    return app

app = get_application()
