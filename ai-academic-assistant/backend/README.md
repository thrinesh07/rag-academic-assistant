# AI Academic Assistant (RAG-based AI System)

A production-grade **AI Academic Assistant for B.Tech Computer Science students** built using a **Retrieval-Augmented Generation (RAG) architecture**.

The system answers academic questions from core CS subjects by retrieving relevant study material and generating structured explanations using a Large Language Model.

This project demonstrates **AI system design, backend architecture, and scalable RAG implementation** rather than a simple chatbot.

---

## Project Overview

Modern students often rely on scattered sources for academic concepts.
This system solves that by providing a **subject-aware AI assistant trained on curated academic material**.

The assistant can answer questions related to:

* Operating Systems
* Database Management Systems
* Computer Networks
* Data Structures and Algorithms
* Object-Oriented Programming

Instead of relying purely on LLM memory, the system uses **Retrieval-Augmented Generation (RAG)** to ensure answers come from verified documents.

---

## Key Features

* AI-powered academic question answering
* Retrieval-Augmented Generation pipeline
* Subject-aware semantic search
* FAISS vector database
* Groq LLM integration for fast inference
* Secure JWT authentication with refresh tokens
* Chat history storage and tracking
* Document ingestion pipeline for PDFs
* Admin document upload system
* Rate limiting and request logging
* Production-ready backend architecture
* Docker and Render deployment support
* Comprehensive automated test suite

---

## System Architecture

The application follows a **layered architecture with clear separation of concerns**.

Client
↓
FastAPI Backend
↓
Service Layer
↓
RAG Adapter
↓
Retrieval Pipeline
↓
Vector Database (FAISS)
↓
Groq LLM

### High-Level Flow

1. User submits a question.
2. Backend validates authentication and request data.
3. Question embedding is generated.
4. Vector search retrieves the most relevant document chunks.
5. Retrieved context is injected into a structured prompt.
6. Groq LLM generates an academic answer.
7. Response and retrieved sources are stored in the database.
8. Answer is returned to the user.

This design reduces hallucinations and improves answer reliability.

---

## Tech Stack

Backend

* FastAPI
* SQLAlchemy ORM
* PostgreSQL (Supabase compatible)
* JWT Authentication

AI / Machine Learning

* Sentence Transformers
* FAISS Vector Search
* Groq LLM API

Data Processing

* PyMuPDF for PDF extraction
* Token-based chunking

Infrastructure

* Docker
* Render deployment
* Supabase PostgreSQL

Testing

* Pytest
* FastAPI TestClient

---

## Backend Architecture

The backend follows a **clean architecture pattern**.

```
backend/
│
├── app/
│   ├── api/              # Route definitions
│   ├── services/         # Business logic
│   ├── models/           # Database models
│   ├── schemas/          # API validation
│   ├── middleware/       # Rate limiting & logging
│   ├── integrations/     # RAG adapter layer
│   ├── core/             # Config, security, constants
│   ├── database/         # DB session and migrations
│   └── main.py           # Application entry point
│
├── rag/                  # Complete RAG engine
│   ├── ingestion/
│   ├── chunking/
│   ├── embeddings/
│   ├── vector_store/
│   ├── retrieval/
│   ├── prompts/
│   └── services/
│
├── tests/                # Automated test suite
└── infrastructure/       # Docker & deployment configs
```

---

## Retrieval-Augmented Generation Pipeline

The RAG system consists of several modular stages.

Document Ingestion

* Extract text from PDFs
* Clean and normalize content

Chunking

* Token-aware chunking strategy
* Metadata enrichment

Embeddings

* SentenceTransformer embedding generation

Vector Storage

* FAISS index for fast similarity search

Retrieval

* Cosine similarity search
* Subject-based filtering

Prompt Construction

* Academic structured prompts
* Context injection

Generation

* Groq LLM generates final response

This architecture ensures answers are grounded in real academic material.

---

## Security Features

* JWT authentication with access and refresh tokens
* HTTPOnly secure cookies
* Password hashing using bcrypt
* Admin-only document ingestion
* Input validation via Pydantic
* Rate limiting middleware
* Structured error handling

---

## Deployment

The system is designed for cloud deployment.

Frontend

* Vercel

Backend

* Render (Docker container)

Database

* Supabase PostgreSQL

Vector Index

* Local FAISS index with persistent storage

---

## Running Locally

Install dependencies:

```
pip install -r requirements.txt
```

Start the server:

```
uvicorn app.main:app --reload
```

Open API docs:

```
http://localhost:8000/docs
```

---

## Running Tests

```
pytest
```

The test suite covers:

* authentication flow
* chat endpoint
* file upload validation
* RAG adapter behavior

---

## Example API Request

POST `/api/v1/chat`

Request:

```
{
  "subject": "OS",
  "question": "Explain deadlock prevention"
}
```

Response:

```
{
  "answer": "...",
  "retrieved_chunks": [...],
  "subject": "OS",
  "timestamp": "..."
}
```

---

## Future Improvements

Potential enhancements include:

* hybrid search (BM25 + vector search)
* reranking models
* Redis rate limiting
* distributed RAG service
* GPU embedding service
* cost tracking per user
* advanced evaluation metrics

---

## Why This Project Matters

This project demonstrates:

* real-world AI system design
* scalable backend architecture
* practical implementation of RAG
* integration of ML pipelines with production APIs
* secure authentication and data handling

It focuses on **engineering rigor rather than simple AI demos**.

---

## Author

Thrinesh Yerra
Computer Science Engineering Student

Interested in building **AI systems, backend architectures, and real-world machine learning applications**.
