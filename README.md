# 📝 Approach Summary

This project was designed as a lightweight, modular Retrieval-Augmented Generation (RAG) system that prioritizes transparency and grounded responses over unnecessary complexity. Instead of relying on frameworks that abstract the retrieval pipeline, I implemented the core RAG workflow using Sentence Transformers for semantic embeddings, ChromaDB for vector storage, FastAPI for API endpoints, and Google's Gemini 2.5 Flash for response generation. The knowledge base was curated from industry-standard documentation and converted into structured Markdown before being semantically chunked and indexed. During inference, user queries are embedded, matched against the vector database, and the retrieved context is provided to the language model with strict prompting to prevent hallucinations. If the required information is unavailable, the system explicitly refuses to fabricate an answer. The project also includes document contradiction analysis, a Streamlit interface for interaction, and evidence-backed citations to improve explainability and trustworthiness.

---

# 🤖 AI Use Log

The following AI tools were used during development in accordance with the assignment guidelines.

| Stage | AI Tool | Purpose |
|--------|---------|---------|
| Project Planning | ChatGPT | Discussed architecture options, technology selection, and project scope. |
| Knowledge Base Design | ChatGPT | Assisted in refining the structure of curated Markdown documents. |
| Implementation | ChatGPT | Helped with debugging, FastAPI integration, ChromaDB integration, prompt engineering, and code review. |
| Documentation | ChatGPT | Assisted in drafting and refining the README, approach summary, and documentation. |
| Application Runtime | Gemini 2.5 Flash | Used as the language model for grounded answer generation and contradiction analysis within the application. |

## Human Contributions

The following decisions and work were completed by me:

- Selected the project domain.
- Curated the knowledge base from official documentation.
- Structured the repository and project architecture.
- Implemented, tested, and validated the RAG pipeline.
- Verified multilingual behaviour.
- Evaluated hallucination handling using in-domain and out-of-domain queries.
- Performed final integration, testing, and debugging.

AI assistance was used as an engineering collaborator for brainstorming, debugging, documentation, and implementation guidance. All AI usage has been disclosed transparently.