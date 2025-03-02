import React from "react";
import "./SadFace.css";

function SadFace() {
  return (
    <svg
      className="sad-face"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 64 64"
    >
      <circle cx="32" cy="32" r="30" fill="#ffd983" />
      <circle cx="22" cy="25" r="5" fill="#333" />
      <circle cx="42" cy="25" r="5" fill="#333" />
      <path
        d="M20,45 C25,38 39,38 44,45"
        stroke="#333"
        strokeWidth="3"
        fill="none"
        strokeLinecap="round"
      />
    </svg>
  );
}

export default SadFace;
