# AI Academic Assistant – Frontend

A modern React frontend for an **AI-powered Academic Assistant** designed for **B.Tech Computer Science students**.
The system allows students to ask subject-specific questions and receive AI-generated explanations using a Retrieval-Augmented Generation (RAG) backend.

This repository contains the **frontend application built with React + Vite**.

---

## Overview

The AI Academic Assistant helps students understand difficult computer science concepts by providing structured explanations.

Supported subjects include:

* Operating Systems (OS)
* Database Management Systems (DBMS)
* Computer Networks (CN)
* Data Structures & Algorithms (DSA)
* Object Oriented Programming (OOPS)

The assistant communicates with a **FastAPI backend RAG system** that retrieves relevant academic content and generates AI responses.

---

## Tech Stack

Frontend Framework

* React (Vite)

Routing

* React Router

HTTP Client

* Axios

UI Framework

* Bootstrap 5

State Management

* React Context API

Authentication

* Cookie-based JWT authentication

Deployment

* Vercel

---

## Project Structure

```
frontend/
│
├── src/
│   ├── api/                # API request layer
│   ├── components/         # Reusable UI components
│   ├── context/            # Auth and chat state management
│   ├── hooks/              # Custom React hooks
│   ├── layouts/            # Page layouts
│   ├── pages/              # Application pages
│   ├── router/             # Route protection
│   ├── services/           # Cross-cutting logic
│   ├── styles/             # Global styling
│   ├── utils/              # Helper utilities
│   ├── App.jsx
│   └── main.jsx
│
├── public/
├── package.json
├── vite.config.js
└── README.md
```

---

## Features

Authentication

* Secure login and registration
* Cookie-based JWT authentication
* Protected routes
* Role-based access control (admin / student)

AI Chat Interface

* ChatGPT-style conversation UI
* Subject selection
* AI-generated structured answers
* Retrieved context visualization

Admin Panel

* Upload academic PDFs
* Select subject category
* Monitor system index status

User Experience

* Auto-scroll chat window
* Loading indicators
* Error handling
* Toast notifications

---

## Environment Variables

Create a `.env` file in the project root.

```
VITE_API_BASE_URL=http://localhost:8000
```

For production deployment, set this variable in the hosting platform (e.g., Vercel).

---

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/ai-academic-assistant-frontend.git
cd ai-academic-assistant-frontend
```

Install dependencies:

```
npm install
```

Run the development server:

```
npm run dev
```

Open the app:

```
http://localhost:5173
```

---

## Build for Production

```
npm run build
```

The optimized production build will be generated in:

```
dist/
```

---

## Deployment

This project is optimized for deployment on **Vercel**.

Steps:

1. Push the repository to GitHub.
2. Import the project into Vercel.
3. Configure environment variables.
4. Deploy.

Build configuration:

```
Build Command: npm run build
Output Directory: dist
```

---

## Backend Integration

The frontend communicates with a FastAPI backend that implements:

* Retrieval-Augmented Generation (RAG)
* Vector search using FAISS
* Document ingestion pipeline
* Groq LLM inference
* JWT authentication
* PostgreSQL database (Supabase)

Example API endpoint used by the chat interface:

```
POST /api/v1/chat
```

Request format:

```
{
  "subject": "OS",
  "question": "What is deadlock?"
}
```

---

## Security Considerations

* JWT tokens stored in **HTTP-only cookies**
* Credentials sent using `withCredentials: true`
* Backend enforces role-based authorization
* File uploads validated server-side

---

## Future Improvements

* Streaming AI responses
* Markdown rendering for AI answers
* Chat history persistence
* Citation links to source documents
* Dark mode support
* Analytics dashboard

---

## License

This project is intended for educational and research purposes.

---

## Author

Thrinesh Yerra
Computer Science Engineering Student
