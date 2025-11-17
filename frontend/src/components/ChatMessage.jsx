import React from 'react';
import './ChatMessage.css';

const ChatMessage = ({ message, isUser }) => {
  return (
    <div className={`chat-message ${isUser ? 'user' : 'bot'}`}>
      <div className="message-bubble">
        <div className="message-icon">{isUser ? '👤' : '🤖'}</div>
        <div className="message-text">{message}</div>
      </div>
    </div>
  );
};

export default ChatMessage;
