# ContextIQ — Enterprise Document Intelligence System

ContextIQ is a **Retrieval-Augmented Generation (RAG) based AI system** that allows users to upload documents and ask natural language questions about them.
The system processes documents, converts them into vector embeddings, stores them in a vector database, and retrieves relevant context to generate accurate answers using a local LLM.

It demonstrates a **production-style architecture for building AI-powered document intelligence systems**.

---

## Key Features

* Upload and process **PDF documents**
* Automatic **text extraction and cleaning**
* Intelligent **document chunking**
* **Semantic embeddings** using Sentence Transformers
* **Vector database** using FAISS
* **Persistent vector storage**
* **Retrieval-Augmented Generation (RAG) pipeline**
* Local LLM inference using **Ollama**
* **FastAPI backend**
* **Streamlit chat interface**
* API documentation via **Swagger UI**

---

## System Architecture

```
User
  ↓
Streamlit Frontend
  ↓
FastAPI Backend
  ↓
RAG Pipeline
  ↓
Retriever (Semantic Search)
  ↓
FAISS Vector Database
  ↓
Ollama LLM
  ↓
Answer
```

---

## Project Structure

```
ContextIQ
│
├── app
│   ├── api
│   │   └── server.py
│   │
│   ├── core
│   │   └── config.py
│   │
│   ├── embeddings
│   │   ├── embedding_generator.py
│   │   └── vector_store.py
│   │
│   ├── ingestion
│   │   ├── pdf_loader.py
│   │   ├── text_cleaner.py
│   │   └── chunker.py
│   │
│   ├── retrieval
│   │   └── retriever.py
│   │
│   ├── llm
│   │   └── ollama_client.py
│   │
│   ├── rag_pipeline.py
│   └── main.py
│
├── ui
│   └── app.py
│
├── data
│
├── vector_store_data
│
├── run_contextiq.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

| Component       | Technology            |
| --------------- | --------------------- |
| Backend API     | FastAPI               |
| Frontend        | Streamlit             |
| Vector Database | FAISS                 |
| Embeddings      | Sentence Transformers |
| LLM             | Ollama (Llama3)       |
| Retrieval       | Semantic Search       |
| Language        | Python                |

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/contextiq.git
cd contextiq
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama from: https://ollama.com

Pull the required model:

```bash
ollama pull llama3
```

Verify Ollama is working:

```bash
ollama run llama3
```

---

## Running the System

Start both **backend and frontend** with one command:

```bash
python run_contextiq.py
```

This launches:

| Service            | URL                          |
| ------------------ | ---------------------------- |
| FastAPI Backend    | http://127.0.0.1:8000        |
| API Documentation  | http://127.0.0.1:8000/docs   |
| Streamlit Frontend | http://localhost:8501        |

---
OR
---
1.Start Backend Manually

**Run:uvicorn app.api.server:app --reload**

2.Start Frontend

**streamlit run ui/app.py**

## How It Works

### Document Ingestion Pipeline

```
PDF Upload
   ↓
Text Extraction
   ↓
Text Cleaning
   ↓
Chunking
   ↓
Embedding Generation
   ↓
Vector Storage (FAISS)
```

### Query Pipeline

```
User Question
      ↓
Query Embedding
      ↓
Vector Similarity Search
      ↓
Relevant Document Chunks
      ↓
Prompt Construction
      ↓
LLM Response Generation
```

---

## Example API Request

```
GET /ask?query=What is this document about?
```

Response:

```json
{
  "question": "What is this document about?",
  "answer": "The document appears to be a resume describing..."
}
```

---

## Future Improvements

* Multi-document search support
* Conversation memory
* LangChain text splitters
* Hybrid search (BM25 + vector search)
* Authentication for APIs
* Docker containerization
* Deployment on cloud infrastructure

---

## Use Cases

* Enterprise document intelligence
* Knowledge base assistants
* Resume or research document analysis
* Internal company document Q&A
* AI-powered document search

---

## Author

**Dheeraj K**  
Interested in **AI Systems, GenAI, and Cybersecurity**

---

## License

This project is for educational and research purposes.
