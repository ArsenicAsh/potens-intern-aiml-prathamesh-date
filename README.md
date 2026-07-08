# 📚 DocLens AI

A Retrieval-Augmented Generation (RAG) system that answers questions over a curated technical knowledge base with grounded responses, citations, and contradiction analysis.

Built as part of the Potens IT Services & Consultancy 2026 Internship Take-Home Assignment.

---

## 🚀 Project Overview

DocLens AI is a lightweight RAG application that retrieves relevant technical documentation before generating responses with Google's Gemini model.

Instead of relying solely on an LLM's internal knowledge, the application performs semantic retrieval over an indexed knowledge base and provides evidence-backed answers with citations.

The system also includes a document contradiction endpoint for comparing two documents on a specified topic.

---

## ✨ Features

- Semantic Retrieval using Sentence Transformers
- ChromaDB Vector Database
- Retrieval-Augmented Generation (RAG)
- Evidence-backed answers with citations
- Hallucination-aware prompting
- Document contradiction analysis
- FastAPI REST API
- Streamlit Web Interface
- Curated technical knowledge base
- Modular architecture

---

# 🏗 Architecture

```text
                        User Question
                              │
                              ▼
                     FastAPI (/ask)
                              │
                              ▼
                Query Normalization
                              │
                              ▼
          Sentence Transformer Embedding
                              │
                              ▼
                   ChromaDB Retrieval
                              │
                              ▼
                Top-K Relevant Chunks
                              │
                              ▼
                    Gemini 2.5 Flash
                              │
                              ▼
              Grounded Answer + Citations
```

---

# 📂 Project Structure

```
potens-intern-ai-prathamesh-date/

├── api/
│   ├── main.py
│   └── routes.py
│
├── docs/
│   ├── 01_rag_fundamentals.md
│   ├── 02_embeddings.md
│   ├── 03_vector_databases.md
│   ├── 04_prompt_engineering.md
│   └── 05_hallucination_and_ai_safety.md
│
├── knowledge_base/
│   └── sources/
│       ├── google_ai/
│       ├── chromadb/
│       ├── sentence_transformers/
│       └── microsoft/
│
├── services/
│   ├── ingest.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── chroma_service.py
│   ├── retriever.py
│   ├── generator.py
│   ├── contradict.py
│   └── translator.py
│
├── ui/
│   └── app.py
│
├── vector_store/
│
├── README.md
└── requirements.txt
```

---

# 📖 Knowledge Base

The indexed knowledge base consists of curated technical documentation created from industry-standard documentation.

Topics include:

- Retrieval-Augmented Generation (RAG)
- Embeddings
- Vector Databases
- Prompt Engineering
- Hallucination & AI Safety

Source material was curated from:

- Google AI Documentation
- ChromaDB Documentation
- Sentence Transformers Documentation
- Microsoft Learn

---

# ✂ Chunking Strategy

The knowledge base is chunked semantically using Markdown section headings rather than fixed-size token windows.

Each chunk stores:

- Source document
- Section title
- Chunk ID
- Text content

This preserves contextual meaning while enabling precise retrieval and citation generation.

---

# 🧠 Embedding Strategy

Embeddings are generated using:

**Sentence Transformers**

Model:

```
all-MiniLM-L6-v2
```

Reasons for choosing this model:

- Lightweight
- Fast local inference
- 384-dimensional embeddings
- Strong semantic search performance
- Excellent free/open-source option for RAG systems

---

# 🗄 Vector Store

The project uses **ChromaDB** as the vector database.

Responsibilities:

- Store document embeddings
- Perform semantic similarity search
- Retrieve Top-K relevant chunks

---

# 🔍 Retrieval Strategy

Retrieval flow:

1. User submits a question.
2. Common abbreviations are normalized.
3. The query is converted into an embedding.
4. ChromaDB performs semantic similarity search.
5. Top-K document chunks are retrieved.
6. Retrieved context is supplied to Gemini.
7. Gemini generates a grounded response with citations.

---

# 🤖 Generation Strategy

Google Gemini 2.5 Flash is responsible only for response generation.

The model is instructed to:

- Answer ONLY from retrieved context
- Never invent missing information
- Explicitly refuse unsupported questions
- Return supporting evidence

This minimizes hallucinations while keeping responses grounded in the indexed documentation.

---

# 🚫 Hallucination Prevention

The application intentionally avoids silent hallucinations.

If the retrieved documentation does not contain sufficient information, the model responds with:

> "The available documentation does not contain sufficient information to answer this question."

This behavior was validated using multiple out-of-domain queries.

---

# ⚖ Contradiction Analysis

The `/contradict` endpoint compares two documentation files on a user-specified topic.

Rather than using keyword matching, Gemini evaluates whether the supplied documents:

- contradict,
- complement,
- or agree

while providing reasoning for its decision.

---

# 🌍 Multilingual Support

The system supports multilingual interaction by preserving the user's query language during response generation.

(Current implementation uses prompt-based language preservation.)

---

# 🛠 Technology Stack

| Category | Technology |
|----------|------------|
| Backend | FastAPI |
| Frontend | Streamlit |
| LLM | Gemini 2.5 Flash |
| Embeddings | Sentence Transformers |
| Embedding Model | all-MiniLM-L6-v2 |
| Vector Database | ChromaDB |
| Language | Python |

---

# 📡 API Endpoints

## POST `/ask`

Returns a grounded answer with citations.

Example request

```json
{
    "question": "What is RAG?"
}
```

---

## POST `/contradict`

Compares two documents.

Example request

```json
{
    "document1":"01_rag_fundamentals.md",
    "document2":"05_hallucination_and_ai_safety.md",
    "topic":"Reducing Hallucinations"
}
```

---

# ▶ Running the Project

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Start FastAPI

```bash
uvicorn api.main:app --reload
```

---

## Start Streamlit

```bash
streamlit run ui/app.py
```

---

# 🧪 Example Queries

### Supported

- What is Retrieval-Augmented Generation?
- How do embeddings work?
- What is semantic search?
- Why are vector databases used?
- How does prompt engineering improve AI systems?
- How does RAG reduce hallucinations?
- Explain embeddings and vector databases together.

### Out-of-Scope

- Who won the FIFA World Cup?
- Explain LangChain.
- What is Quantum Computing?

The system correctly refuses unsupported questions instead of hallucinating.

---

# ⚠ Known Limitations

- Knowledge is limited to indexed documentation.
- Contradiction analysis depends on LLM reasoning.
- No reranking layer.
- No confidence scoring.
- Optimized for Markdown knowledge bases.

---

# 🚀 Future Improvements

- Cross-encoder reranking
- Hybrid BM25 + Vector Search
- Confidence scores
- Human-in-the-loop review
- Docker deployment
- Authentication
- Streaming responses
- Incremental indexing

---

# 🤖 AI Usage

AI tools were used transparently throughout development.

Used for:

- Architecture discussions
- Debugging
- Code review
- Documentation refinement
- Prompt engineering

All engineering decisions, technology selection, knowledge base curation, implementation, testing, and validation were performed by the project author.

---

# 👨‍💻 Author

Prathamesh Date

Built for the Potens IT Services & Consultancy 2026 Internship Selection Process.
