import React, { useState, useRef, useEffect } from 'react';
import { sendChatQuery } from './services/api';
import ChatMessage from './components/ChatMessage';
import ChartDisplay from './components/ChartDisplay';
import DataTable from './components/DataTable';
import './App.css';

function App() {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [loading, setLoading] = useState(false);
  const [currentAnalysis, setCurrentAnalysis] = useState(null);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    setMessages([{
      id: 1,
      text: "Hello! I'm your Real Estate Analysis Assistant. 🏠\n\nAsk me about property trends in Wakad, Aundh, Ambegaon Budruk, or Akurdi!",
      isUser: false,
    }]);
  }, []);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, currentAnalysis]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!inputValue.trim()) return;

    const userMessage = {
      id: Date.now(),
      text: inputValue,
      isUser: true,
    };

    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setLoading(true);
    setCurrentAnalysis(null);

    try {
      const response = await sendChatQuery(inputValue);
      
      if (response.success) {
        const botMessage = {
          id: Date.now() + 1,
          text: response.summary,
          isUser: false,
        };
        
        setMessages(prev => [...prev, botMessage]);
        setCurrentAnalysis({
          chartData: response.chart_data,
          tableData: response.table_data,
        });
      } else {
        throw new Error(response.message || 'Failed to process query');
      }
    } catch (err) {
      const errorMessage = {
        id: Date.now() + 1,
        text: `Sorry, error: ${err.error || err.message || 'Check if backend is running at http://localhost:8000'}`,
        isUser: false,
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  const sampleQueries = [
    "Give me analysis of Wakad",
    "Compare Ambegaon Budruk and Aundh",
    "Show price growth for Akurdi"
  ];

  return (
    <div className="app">
      <header className="header">
        <div className="container">
          <h1>🏠 Real Estate AI Chatbot</h1>
          <p>AI-Powered Property Market Insights</p>
        </div>
      </header>

      <div className="container main-content">
        <div className="chat-section">
          <div className="chat-container">
            <div className="messages-container">
              {messages.map((message) => (
                <ChatMessage
                  key={message.id}
                  message={message.text}
                  isUser={message.isUser}
                />
              ))}
              
              {loading && (
                <div className="loading">
                  <div className="spinner"></div>
                  <p>Analyzing...</p>
                </div>
              )}
              
              {currentAnalysis && (
                <div className="analysis-results">
                  <ChartDisplay chartData={currentAnalysis.chartData} />
                  <DataTable data={currentAnalysis.tableData} />
                </div>
              )}
              
              <div ref={messagesEndRef} />
            </div>

            <div className="input-section">
              <div className="sample-queries">
                <small>Try these:</small>
                {sampleQueries.map((query, index) => (
                  <button
                    key={index}
                    className="sample-btn"
                    onClick={() => setInputValue(query)}
                  >
                    {query}
                  </button>
                ))}
              </div>
              
              <form onSubmit={handleSubmit} className="input-form">
                <input
                  type="text"
                  placeholder="Ask about real estate trends..."
                  value={inputValue}
                  onChange={(e) => setInputValue(e.target.value)}
                  disabled={loading}
                  className="chat-input"
                />
                <button
                  type="submit"
                  disabled={loading || !inputValue.trim()}
                  className="send-btn"
                >
                  ➤
                </button>
              </form>
            </div>
          </div>
        </div>

        <div className="sidebar">
          <div className="info-card">
            <h3>📊 Available Areas</h3>
            <ul>
              <li>✓ Wakad</li>
              <li>✓ Aundh</li>
              <li>✓ Ambegaon Budruk</li>
              <li>✓ Akurdi</li>
            </ul>
          </div>
          
          <div className="info-card">
            <h3>💡 Features</h3>
            <ul>
              <li>Analyze price trends</li>
              <li>Show demand patterns</li>
              <li>Compare multiple areas</li>
              <li>Export data to CSV</li>
            </ul>
          </div>
        </div>
      </div>

      <footer className="footer">
        <p>Built with React + Django + Gemini AI | Sigmavalue Assignment</p>
      </footer>
    </div>
  );
}

export default App;
