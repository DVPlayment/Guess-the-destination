import React from "react";

function ClueDisplay({ clues }) {
  return (
    <div>
      <h3>Clues</h3>
      {clues.map((clue, idx) => (
        <p key={idx}>{clue}</p>
      ))}
    </div>
  );
}

export default ClueDisplay;
