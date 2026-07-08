from sentence_transformers import SentenceTransformer
import chromadb

ABBREVIATIONS = {
    "rag": "retrieval augmented generation",
    "llm": "large language model",
    "ai": "artificial intelligence",
}


def normalize_query(query: str) -> str:
    normalized = query.lower()

    for short, full in ABBREVIATIONS.items():
        normalized = normalized.replace(short, full)

    return normalized

# Load embedding model (loads only once)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to persistent ChromaDB
client = chromadb.PersistentClient(path="vector_store")

collection = client.get_collection("knowledge_base")


def retrieve(query: str, top_k: int = 5):
    """
    Retrieve the most relevant chunks for a user query.

    Args:
        query (str): User question
        top_k (int): Number of results to return

    Returns:
        List of dictionaries containing retrieved chunks.
    """

    normalized_query = normalize_query(query)

    query_embedding = model.encode(normalized_query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
    )

    retrieved_chunks = []

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    for doc, metadata, distance in zip(documents, metadatas, distances):

        retrieved_chunks.append(
            {
                "document": doc,
                "source": metadata["source"],
                "section": metadata["section"],
                "chunk_id": metadata["chunk_id"],
                "distance": distance,
            }
        )

    return retrieved_chunks


if __name__ == "__main__":

    question = input("\nAsk something: ")

    results = retrieve(question)

    print("\nTop Results:\n")

    for result in results:

        print("=" * 70)
        print(f"Source   : {result['source']}")
        print(f"Section  : {result['section']}")
        print(f"Chunk ID : {result['chunk_id']}")
        print(f"Distance : {result['distance']:.4f}")
        print()

        preview = result["document"][:300]

        if len(result["document"]) > 300:
            preview += "..."

        print(preview)
        print()