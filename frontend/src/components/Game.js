import React, { useState } from "react";
import {
  createGame,
  getRandomQuestion,
  createChallenge,
  getClue,
  submitAnswer,
  getGame,
} from "../services/api";
import ClueDisplay from "./ClueDisplay";
import AnswerForm from "./AnswerForm";
import Score from "./Score";
import Confetti from "react-confetti";
import SadFace from "./SadFace";

function Game({ userId }) {
  const [gameId, setGameId] = useState(null);
  const [challengeId, setChallengeId] = useState(null);
  const [clues, setClues] = useState([]);
  const [funFacts, setFunFacts] = useState([]);
  const [isCorrect, setIsCorrect] = useState(null);
  const [correctAnswer, setCorrectAnswer] = useState("");
  const [score, setScore] = useState("0");

  // Create a new game
  const handleNewGame = async () => {
    const g = await createGame(userId);
    setGameId(g.game_id);
    setScore(g.score);
    // Reset challenge-related state
    setChallengeId(null);
    setClues([]);
    setFunFacts([]);
    setIsCorrect(null);
    setCorrectAnswer("");
  };

  // Load a new random destination and create a new challenge
  const handleNext = async () => {
    if (!gameId) return alert("Create a game first!");
    const q = await getRandomQuestion();
    const c = await createChallenge(gameId, q.question_id);
    setChallengeId(c.challenge_id);
    setClues([]);
    setFunFacts([]);
    setIsCorrect(null);
    setCorrectAnswer("");
  };

  // Fetch Clue 1 or 2
  const handleGetClue = async (clueNumber) => {
    if (!challengeId) return alert("No active challenge. Click Next first.");
    const c = await getClue(challengeId, clueNumber);
    setClues((prev) => [...prev, c.clue]);
  };

  // Submit answer
  const handleSubmitAnswer = async (answer) => {
    if (!challengeId) return alert("No active challenge. Click Next first.");
    const result = await submitAnswer(challengeId, answer);
    setIsCorrect(result.is_correct);
    setCorrectAnswer(result.correct_answer);
    setFunFacts(result.fun_facts);
    // Fetch updated score
    const g = await getGame(gameId);
    setScore(g.score);
  };

  return (
    <div>
      <h2>Globetrotter Game</h2>
      <button onClick={handleNewGame}>Create New Game</button>
      {gameId && <Score score={score} />}
      <button onClick={handleNext} disabled={!gameId}>
        Next Destination
      </button>

      <ClueDisplay clues={clues} />

      <button onClick={() => handleGetClue(1)} disabled={!challengeId}>
        Clue 1
      </button>
      <button onClick={() => handleGetClue(2)} disabled={!challengeId}>
        Clue 2
      </button>

      <AnswerForm onSubmit={handleSubmitAnswer} disabled={!challengeId} />

      {isCorrect !== null && (
        <div>
          {isCorrect ? (
            <div style={{ position: "relative" }}>
              <Confetti />
              <p style={{ color: "green" }}>
                Correct! The answer is {correctAnswer}.
              </p>
            </div>
          ) : (
            <div style={{ position: "relative" }}>
              <SadFace />
              <p style={{ color: "red" }}>
                Incorrect. The correct answer is {correctAnswer}.
              </p>
            </div>
          )}
          {funFacts.length > 0 && (
            <ul>
              {funFacts.map((fact, idx) => (
                <li key={idx}>{fact}</li>
              ))}
            </ul>
          )}
        </div>
      )}
    </div>
  );
}

export default Game;
