# Example Queries

The following examples demonstrate the expected behaviour of DocLens AI.

---

# Example 1

### Question

What is Retrieval-Augmented Generation (RAG)?

### Expected Behaviour

Returns an explanation of RAG with citations from:

- 01_rag_fundamentals.md

---

# Example 2

### Question

How do embeddings work?

### Expected Behaviour

Explains semantic embeddings and similarity search.

Expected citations:

- 02_embeddings.md

---

# Example 3

### Question

What is semantic search?

### Expected Behaviour

Explains semantic similarity using vector embeddings.

Expected citations:

- 02_embeddings.md
- 03_vector_databases.md

---

# Example 4

### Question

Why are vector databases used?

### Expected Behaviour

Explains why vector databases enable efficient similarity search.

Expected citations:

- 03_vector_databases.md

---

# Example 5

### Question

How does prompt engineering improve AI responses?

### Expected Behaviour

Explains prompt engineering and grounded prompting.

Expected citations:

- 04_prompt_engineering.md

---

# Example 6

### Question

What is hallucination in AI?

### Expected Behaviour

Defines hallucinations and explains their causes.

Expected citations:

- 05_hallucination_and_ai_safety.md

---

# Example 7

### Question

How does RAG reduce hallucinations?

### Expected Behaviour

Combines information from multiple documents.

Expected citations:

- 01_rag_fundamentals.md
- 05_hallucination_and_ai_safety.md

---

# Example 8

### Question

What is RAG and how do embeddings help it?

### Expected Behaviour

Demonstrates multi-document retrieval and synthesis.

Expected citations:

- 01_rag_fundamentals.md
- 02_embeddings.md

---

# Example 9 (Out-of-Scope)

### Question

Who won the 2022 FIFA World Cup?

### Expected Behaviour

The system should refuse to answer because the indexed documentation does not contain this information.

---

# Example 10 (Out-of-Scope)

### Question

Explain quantum computing.

### Expected Behaviour

The system should indicate that the available documentation does not contain sufficient information instead of generating unsupported information.