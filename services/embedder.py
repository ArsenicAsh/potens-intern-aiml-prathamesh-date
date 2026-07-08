from sentence_transformers import SentenceTransformer

# Load embedding model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(chunks):
    """
    Generate embeddings for all chunks.

    Args:
        chunks: List of chunk dictionaries

    Returns:
        Same chunks with embeddings attached.
    """

    for chunk in chunks:
        embedding = model.encode(chunk["text"]).tolist()

        chunk["embedding"] = embedding

    return chunks


if __name__ == "__main__":

    from services.ingest import load_documents
    from services.chunker import chunk_documents

    docs = load_documents()

    chunks = chunk_documents(docs)

    chunks = generate_embeddings(chunks)

    print(f"\nGenerated embeddings for {len(chunks)} chunks.\n")

    print(chunks[0].keys())

    print(f"\nEmbedding Length: {len(chunks[0]['embedding'])}")