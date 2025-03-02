import React, { useState } from "react";
import SignUp from "./components/SignUp";
import Game from "./components/Game";

function App() {
  const [userId, setUserId] = useState(null);

  // If user hasn't signed up/logged in, show SignUp
  if (!userId) {
    return <SignUp setUserId={setUserId} />;
  }

  // Else show Game
  return <Game userId={userId} />;
}

export default App;
