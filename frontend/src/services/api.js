const BASE_URL = "http://127.0.0.1:8000"; // Your backend address

// Sign Up User
export async function signUp(username, password) {
  const resp = await fetch(`${BASE_URL}/users/signup`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });
  if (!resp.ok) {
    const errorData = await resp.json();
    throw new Error(errorData.detail || "Sign up failed");
  }
  return resp.json(); // { user_id, username }
}

// Create a New Game
export async function createGame(userId) {
  const resp = await fetch(`${BASE_URL}/games`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_id: userId }),
  });
  if (!resp.ok) {
    const errorData = await resp.json();
    throw new Error(errorData.detail || "Create game failed");
  }
  return resp.json(); // { game_id, user_id, score, is_active }
}

// Get a Random Question
export async function getRandomQuestion() {
  const resp = await fetch(`${BASE_URL}/questions/random`);
  return resp.json(); // { question_id }
}

// Create Challenge
export async function createChallenge(gameId, questionId) {
  const resp = await fetch(`${BASE_URL}/challenges`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ game_id: gameId, question_id: questionId }),
  });
  return resp.json(); // { challenge_id }
}

// Get a Clue
export async function getClue(challengeId, clueNumber) {
  const resp = await fetch(`${BASE_URL}/challenges/${challengeId}/clue/${clueNumber}`);
  return resp.json(); // { clue: "..." }
}

// Submit an Answer
export async function submitAnswer(challengeId, userAnswer) {
  const resp = await fetch(`${BASE_URL}/challenges/${challengeId}/answer`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_answer: userAnswer }),
  });
  return resp.json(); // { correct_answer, is_correct, fun_facts: [...] }
}

// (Optional) Get Score for a Game
export async function getGame(gameId) {
  const resp = await fetch(`${BASE_URL}/games/${gameId}`);
  return resp.json(); // { game_id, user_id, score, is_active }
}

