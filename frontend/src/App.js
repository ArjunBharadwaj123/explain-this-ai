import React, { useState } from "react";
import API from "./api";
import "./App.css";

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [filename, setFilename] = useState("");
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState(null);
  const [sources, setSources] = useState([]);
  const [loadingUpload, setLoadingUpload] = useState(false);
  const [loadingAsk, setLoadingAsk] = useState(false);
  const [showSources, setShowSources] = useState(false);


  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!selectedFile) return;

    setLoadingUpload(true);

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const response = await API.post("/upload", formData);
      setFilename(response.data.filename);
      alert("Image uploaded successfully!");
    } catch (error) {
      alert("Upload failed");
    }

    setLoadingUpload(false);
  };


  const handleAsk = async () => {
    if (!filename || !question) return;

    setLoadingAsk(true);

    try {
      const response = await API.post("/ask", {
        image_path: `uploaded_files/${filename}`,
        question: question
      });

      setAnswer(response.data.answer);
      setSources(response.data.sources);
    } catch (error) {
      alert("Ask failed");
    }

    setLoadingAsk(false);
  };


  return (
    <div className="app-container">
      <div className="header">Explain This AI</div>

      <div className="upload-section">
        <h3>Upload Screenshot</h3>
        <input type="file" onChange={handleFileChange} />
        <button onClick={handleUpload} disabled={loadingUpload}>
          {loadingUpload ? "Uploading..." : "Upload"}
        </button>
      </div>

      <div className="chat-container">
        {question && (
          <div className="message user-message">
            {question}
          </div>
        )}

        {answer && (
          <div className="message ai-message">
            <strong>Answer:</strong>
            <p>{answer}</p>

            <div style={{ marginTop: "15px" }}>
              <div
                style={{
                  cursor: "pointer",
                  fontWeight: "600",
                  display: "flex",
                  alignItems: "center",
                  gap: "6px"
                }}
                onClick={() => setShowSources(!showSources)}
              >
                📚 Sources {showSources ? "▲" : "▼"}
              </div>

              {showSources && (
                <div style={{ marginTop: "10px" }}>
                  {sources.map((source, index) => (
                    <div key={index} className="source-box">
                      <strong>Chunk {source.chunk_id}</strong> (Score: {source.score.toFixed(2)})
                      <div>{source.preview}...</div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>
        )}
      </div>

      <div className="input-bar">
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask about the image..."
        />
        <button onClick={handleAsk} disabled={loadingAsk}>
          {loadingAsk ? "Thinking..." : "Ask"}
        </button>
      </div>
    </div>
  );
}

export default App;
