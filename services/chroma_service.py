import chromadb
from chromadb.config import Settings

# Persistent database stored locally
client = chromadb.PersistentClient(path="vector_store")

collection = client.get_or_create_collection(
    name="knowledge_base"
)


def store_chunks(chunks):
    """
    Store chunks inside ChromaDB.
    """

    # Clean previous collection contents
    existing = collection.get()

    if existing["ids"]:
        collection.delete(ids=existing["ids"])

    for chunk in chunks:

        collection.add(

            ids=[chunk["id"]],

            embeddings=[chunk["embedding"]],

            documents=[chunk["text"]],

            metadatas=[

                {
                    "source": chunk["source"],
                    "section": chunk["section"],
                    "chunk_id": chunk["chunk_id"]
                }

            ]

        )

    print(f"Stored {len(chunks)} chunks in ChromaDB.")

if __name__ == "__main__":

    from services.ingest import load_documents
    from services.chunker import chunk_documents
    from services.embedder import generate_embeddings

    docs = load_documents()

    chunks = chunk_documents(docs)

    chunks = generate_embeddings(chunks)

    store_chunks(chunks)

    print(collection.count())
    