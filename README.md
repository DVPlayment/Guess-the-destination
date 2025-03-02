# Globetrotter

**Globetrotter** is a travel guessing game where users sign up, create a game, receive cryptic clues about famous destinations, submit guesses, and earn points. There’s also a **“Challenge a Friend”** feature that allows users to invite others via a shareable link. The invited friend can see the inviter’s score before playing.

## Table of Contents
- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Core Features](#core-features)
- [Setup & Installation](#setup--installation)
- [Endpoints](#endpoints)
- [Additional Notes](#additional-notes)

---

## Project Overview

Globetrotter provides a fun, interactive travel quiz experience where:
- **Users Sign Up** with a unique username and password.
- **Game Creation** disables any existing active game for a user and starts a new session with a fresh score.
- **Clues & Answers**: Each challenge provides cryptic clues about a destination. The user submits their guess, and the backend checks correctness, updates the challenge record, and recalculates the game score based on correctly answered challenges.
- **Challenge a Friend**: A unique invite link is generated so that friends can see the inviter’s score before signing up and playing.

---

## Tech Stack

**Backend:**
- **Python 3.12**
- **FastAPI** – Fast, async-friendly REST API framework.
- **SQLAlchemy** – ORM for database interactions.
- **SQLite** – Lightweight database.

**Frontend:**
- **React** – Built using Create React App.
- **JavaScript** – For dynamic, component-based UI.
- **Node.js** – For dependency management.

**Why this stack?**
- **FastAPI** offers rapid development and asynchronous capabilities.
- **React** enables a modern, engaging UI and seamless state management.
- **SQLAlchemy + SQLite** provide an easy-to-setup yet robust data layer for demo/small-scale purposes.

---

## Architecture

The project follows a **Controller–Service–Repository** pattern:

- **Controllers:**  
  Define API endpoints and handle HTTP requests/responses.  
  (Located in `backend/app/controllers/`)

- **Services:**  
  Contain the business logic (e.g., score recalculation, challenge processing, invitation generation).  
  (Located in `backend/app/services/`)

- **Repositories:**  
  Handle direct database operations (CRUD) using SQLAlchemy.  
  (Located in `backend/app/repositories/`)

**Benefits:**
- **Separation of Concerns:** Each layer has a single responsibility.
- **Maintainability:** Changes in one layer don’t ripple through the entire application.
- **Scalability:** Clear boundaries make it easy to extend the functionality.

---

## Core Features

- **User Sign Up:**  
  Users register with a unique username and password.

- **Game Creation:**  
  When a new game is created, any existing active game for the user is disabled and a fresh game starts with a score of zero.

- **Clues & Answers:**  
  Each challenge ties a random question (destination) to the user’s game. Clues are fetched via API endpoints, and submitting an answer checks for correctness, updates the challenge record, and recalculates the overall game score.

- **Score Recalculation:**  
  The final game score is recalculated by counting the number of correctly answered challenges.

- **Challenge a Friend:**  
  Generates a unique invitation link (e.g., `http://localhost:3000/invitations/INVITE_CODE`) which shows the inviter’s current score. The invited friend can view this and then sign up to play.

---

## Setup & Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/DVPlayment/Guess-the-destination.git
   ```
2. Install libraries for python backend ->
    ```bash
   pip install fastapi uvicorn sqlalchemy pydantic
    ```
4. **Run the apps in 2 separate terminals**
   ```bash

   cd Globetrotter
   uvicorn backend.app.main:app --reload
   cd frontend
   npm start
   ```

---

## Endpoints

- **User:**
  - `POST /users/signup`  
    Register a new user.

- **Game:**
  - `POST /games`  
    Create a new game. This endpoint disables any existing active game for the user and starts a fresh game.
  - `GET /games/{game_id}`  
    Retrieve game details, including the current score.

- **Question/Challenge:**
  - `GET /questions/random`  
    Get a random question (destination) for a new challenge.
  - `POST /challenges`  
    Create a challenge for the game by associating a random question with the user's active game.
  - `GET /challenges/{challenge_id}/clue/{n}`  
    Retrieve the nth clue (e.g., Clue 1 or Clue 2) for the challenge.
  - `POST /challenges/{challenge_id}/answer`  
    Submit an answer for the challenge. This endpoint checks the answer, updates the challenge record, and recalculates the overall game score.

- **Invitations:**
  - `POST /invitations`  
    Create an invitation link for challenging a friend. The response includes a unique invite code and link.
  - `GET /invitations/{invite_code}`  
    Retrieve invitation details including the inviter's ID and the current game score.

   
