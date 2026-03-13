# AI Academic Assistant

A production-grade **AI Academic Assistant for B.Tech Computer Science students** built using a **Retrieval-Augmented Generation (RAG) architecture**.

The system allows students to ask subject-specific academic questions and receive structured explanations generated using an AI model grounded in verified study material.

Unlike simple chatbots, this project demonstrates **real-world AI system architecture**, combining **machine learning pipelines, scalable backend APIs, and a modern React frontend**.

---

# Project Overview

Students often rely on scattered resources to understand complex computer science concepts.
This system centralizes those resources into a **subject-aware AI assistant** capable of answering questions based on curated academic documents.

Supported subjects include:

* Operating Systems (OS)
* Database Management Systems (DBMS)
* Computer Networks (CN)
* Data Structures & Algorithms (DSA)
* Object-Oriented Programming (OOPS)

Instead of relying purely on a language model's internal knowledge, the assistant uses a **Retrieval-Augmented Generation (RAG) pipeline** to retrieve relevant content before generating answers.

This significantly improves **accuracy, reliability, and transparency**.

---

# System Architecture

The application follows a layered architecture with clear separation of concerns.

```
Client (React)
        ↓
FastAPI Backend API
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
```

---

# High-Level Workflow

1. User submits a question through the chat interface.
2. Backend validates authentication and request data.
3. The question is converted into a semantic embedding.
4. FAISS performs vector similarity search on indexed academic documents.
5. Relevant document chunks are retrieved.
6. Retrieved context is injected into a structured prompt.
7. Groq LLM generates the final explanation.
8. Chat history and retrieved sources are stored in the database.
9. The response is returned to the frontend.

This architecture reduces hallucinations and ensures answers are grounded in real academic material.

---

# Key Features

### AI Features

* Retrieval-Augmented Generation (RAG)
* Semantic vector search using FAISS
* Sentence Transformer embeddings
* Structured academic prompts
* Groq LLM integration for fast inference

### Backend Features

* FastAPI production API
* Clean architecture backend design
* PostgreSQL database (Supabase compatible)
* SQLAlchemy ORM
* JWT authentication with refresh tokens
* HTTP-only secure cookies
* Chat history storage
* Document ingestion pipeline
* Admin-only PDF upload
* Rate limiting middleware
* Structured logging
* Docker deployment

### Frontend Features

* React + Vite application
* ChatGPT-style chat interface
* Subject selection
* Authenticated routes
* Cookie-based JWT authentication
* Admin document upload panel
* Toast notifications and loading indicators
* Axios API integration
* React Router navigation

### Infrastructure

* Docker containerization
* Render backend deployment
* Vercel frontend hosting
* Supabase PostgreSQL database
* Automated test suite

---

# Technology Stack

## Backend

* FastAPI
* SQLAlchemy
* PostgreSQL
* JWT Authentication
* Pydantic Validation

## AI / Machine Learning

* Sentence Transformers
* FAISS Vector Search
* Groq LLM API

## Data Processing

* PyMuPDF for PDF extraction
* Token-based chunking

## Frontend

* React
* Vite
* React Router
* Axios
* Bootstrap 5
* React Context API

## Infrastructure

* Docker
* Render
* Supabase
* Vercel

## Testing

* Pytest
* FastAPI TestClient

---

# Backend Architecture

```
backend/
│
├── app/
│   ├── api/              # Route definitions
│   ├── services/         # Business logic
│   ├── models/           # Database models
│   ├── schemas/          # API validation
│   ├── middleware/       # Logging & rate limiting
│   ├── integrations/     # RAG adapter layer
│   ├── core/             # Security and configuration
│   ├── database/         # DB sessions and migrations
│   ├── lifespan.py       # Startup / shutdown lifecycle
│   └── main.py           # Application entry point
│
├── rag/                  # Complete RAG pipeline
│   ├── ingestion/
│   ├── chunking/
│   ├── embeddings/
│   ├── vector_store/
│   ├── retrieval/
│   ├── prompts/
│   └── services/
│
├── tests/
└── infrastructure/
```

---

# Frontend Architecture

```
frontend/
│
├── src/
│   ├── api/                # API request layer
│   ├── components/         # Reusable UI components
│   ├── context/            # Auth & chat state
│   ├── hooks/              # Custom React hooks
│   ├── layouts/            # Page layouts
│   ├── pages/              # Application pages
│   ├── router/             # Route protection
│   ├── services/           # Business logic
│   ├── styles/             # Global styles
│   ├── utils/              # Helper utilities
│   ├── App.jsx
│   └── main.jsx
│
├── public/
├── package.json
└── vite.config.js
```

---

# Retrieval-Augmented Generation Pipeline

The RAG engine consists of several modular stages.

### Document Ingestion

* Extract text from PDFs
* Clean and normalize content

### Chunking

* Token-aware chunking
* Metadata enrichment

### Embedding Generation

* Sentence Transformer embeddings

### Vector Storage

* FAISS vector index for similarity search

### Retrieval

* Cosine similarity search
* Subject-aware filtering

### Prompt Construction

* Academic structured prompts
* Context injection

### Generation

* Groq LLM generates final answer

This ensures answers are grounded in real academic material.

---

# Security Features

* JWT authentication
* Access + refresh token lifecycle
* HTTP-only secure cookies
* Password hashing with bcrypt
* Admin-only ingestion endpoints
* Input validation via Pydantic
* Rate limiting middleware
* Structured error handling

---

# Local Development Setup

## Backend

Install dependencies:

```
pip install -r requirements.txt
```

Run server:

```
uvicorn app.main:app --reload
```

Open API docs:

```
http://localhost:8000/docs
```

---

## Frontend

Install dependencies:

```
npm install
```

Run development server:

```
npm run dev
```

Open:

```
http://localhost:5173
```

---

# Environment Variables

Frontend `.env`

```
VITE_API_BASE_URL=http://localhost:8000
```

Backend `.env`

```
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7
FRONTEND_URL=http://localhost:5173
```

---

# Example API Request

### POST `/api/v1/chat`

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

# Running Tests

Run automated test suite:

```
pytest
```

Tests cover:

* authentication flow
* chat endpoint
* file upload validation
* RAG adapter behavior

---

# Deployment

### Frontend

* Platform: **Vercel**

Build command:

```
npm run build
```

Output directory:

```
dist
```

---

### Backend

* Platform: **Render**
* Docker container deployment

---

### Database

* **Supabase PostgreSQL**

---

### Vector Database

* **FAISS index with persistent storage**

---

# Future Improvements

Possible future upgrades:

* Hybrid search (BM25 + vector search)
* Re-ranking models
* Redis-based rate limiting
* Distributed RAG microservice
* GPU embedding service
* Token usage tracking
* Streaming AI responses
* Chat history visualization
* Citation linking to source documents

---

# Why This Project Matters

This project demonstrates:

* Real-world AI system architecture
* Production-grade backend design
* Retrieval-Augmented Generation implementation
* Integration of machine learning pipelines with APIs
* Secure authentication and data handling
* Full-stack system development

It emphasizes **engineering rigor rather than simple AI demos**.

---

# Author

**Thrinesh Yerra**
Computer Science Engineering Student

Interested in building:

* AI systems
* Backend architectures
* Real-world machine learning applications
