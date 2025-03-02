// src/components/InvitationPage.js
import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getInvitation } from "../services/api";
import SignUp from "./SignUp"; // You can reuse your sign-up component

function InvitationPage() {
  const { invite_code } = useParams();
  const [invitation, setInvitation] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchInvitation() {
      try {
        const data = await getInvitation(invite_code);
        setInvitation(data);
      } catch (err) {
        setError(err.message);
      }
    }
    fetchInvitation();
  }, [invite_code]);

  return (
    <div>
      <h2>You're Invited!</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {invitation ? (
        <div>
          <p>
            Invited by: <strong>{invitation.inviter_id}</strong>
          </p>
          <p>
            Current Score: <strong>{invitation.score || 0}</strong>
          </p>
          <p>Please sign up to join the challenge!</p>
          <SignUp />
        </div>
      ) : (
        <p>Loading invitation details...</p>
      )}
    </div>
  );
}

export default InvitationPage;
