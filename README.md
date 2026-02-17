# Explain-This-AI

Explain-This-AI is an AI-powered learning assistant that extracts text from images using OCR, retrieves the most relevant context using vector embeddings (RAG), and generates clear explanations using a large language model.

The goal is to help students better understand AI/ML slides, diagrams, and notes by turning visual content into grounded, structured explanations.

---

## 🚀 Features

- 📷 Upload slide or diagram images
- 🔍 OCR-based text extraction
- 🧠 Embedding-based semantic retrieval (RAG pipeline)
- 🤖 LLM-powered explanation generation
- 📚 Source-aware answers (top-k relevant chunks)
- 💻 Full-stack architecture (FastAPI + React)

---

## 🏗️ System Architecture

```
User Upload
     ↓
OCR (extract text)
     ↓
Text Cleaning
     ↓
Chunking
     ↓
Embeddings (SentenceTransformers)
     ↓
Cosine Similarity Search
     ↓
Top-K Relevant Chunks
     ↓
LLM (OpenAI)
     ↓
Structured Explanation + Sources
```

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- Python
- SentenceTransformers
- NumPy
- EasyOCR
- OpenAI API
- Cosine Similarity Retrieval

### Frontend
- React
- Axios

---

## 📂 Project Structure

```
explain-this-ai/
│
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   ├── requirements.txt
│   └── uploaded_files/ (ignored)
│
├── frontend/
│   ├── src/
│   └── public/
│
├── .gitignore
└── README.md
```

---

## ⚙️ Local Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/YOUR_USERNAME/explain-this-ai.git
cd explain-this-ai
```

---

### 2️⃣ Backend Setup

```
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file inside `backend/`:

```
OPENAI_API_KEY=your_key_here
```

Run backend:

```
uvicorn app.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

### 3️⃣ Frontend Setup

```
cd frontend
npm install
npm start
```

Frontend runs at:

```
http://localhost:3000
```

---

## 🧠 How Retrieval (RAG) Works

1. OCR extracts raw text from the uploaded image.
2. Text is cleaned and split into chunks.
3. Each chunk is embedded using SentenceTransformers.
4. The user’s question is embedded.
5. Cosine similarity finds the top-k most relevant chunks.
6. Those chunks are passed to the LLM.
7. The LLM generates a grounded explanation using retrieved context.

This ensures responses are based on extracted slide content rather than hallucinated information.

---

## 🔐 Security Notes

- `.env` files are excluded from version control.
- API keys should never be committed.
- Uploaded files and cache directories are ignored via `.gitignore`.

---

## 📈 Future Improvements

- Persistent vector database (FAISS / pgvector)
- Streaming LLM responses
- Multi-document support
- Improved UI/UX
- Dockerized deployment
- Cloud deployment (AWS / Render)

---

## 👨‍💻 Author

Arjun Bharadwaj  
Computer Science @ University of Maryland  
AWS Certified Cloud Practitioner  

---

## 📄 License

MIT License
