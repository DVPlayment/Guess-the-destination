import React, { useState } from "react";

function AnswerForm({ onSubmit, disabled }) {
  const [answer, setAnswer] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(answer);
    setAnswer("");
  };

  return (
    <div>
      <h3>Enter Your Guess</h3>
      <form onSubmit={handleSubmit}>
        <input
          value={answer}
          onChange={(e) => setAnswer(e.target.value)}
          disabled={disabled}
          placeholder="Your Answer"
        />
        <button type="submit" disabled={disabled}>Submit</button>
      </form>
    </div>
  );
}

export default AnswerForm;
