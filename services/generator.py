import os

from dotenv import load_dotenv
from google import genai

from services.retriever import retrieve

# Load environment variables
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_answer(question: str):

    retrieved_chunks = retrieve(question)

    context = ""

    citations = []

    for chunk in retrieved_chunks:

        context += (
            f"\nSource: {chunk['source']}"
            f"\nSection: {chunk['section']}"
            f"\nContent:\n{chunk['document']}\n"
        )

        citations.append(
            {
                "source": chunk["source"],
                "section": chunk["section"],
                "chunk_id": chunk["chunk_id"],
            }
        )

    prompt = f"""
You are a technical documentation assistant.

Use ONLY the information provided in the context below.

Answer ONLY using the retrieved documentation.

If the retrieved context contains enough information, answer the question clearly.

If the retrieved context does NOT contain enough information, respond exactly:

"The available documentation does not contain sufficient information to answer this question."

Do not guess.
Do not use outside knowledge.

Question:
{question}

Context:
{context}

Return your answer in exactly this format:

Answer:
<your answer>

Evidence:
- Source: <filename>
  Section: <section>

If the documentation does not contain enough information, say so instead of guessing.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return {
        "answer": response.text,
        "citations": citations,
    }


if __name__ == "__main__":

    question = input("\nAsk something: ")

    result = generate_answer(question)

    print("\n=== RESPONSE ===\n")
    print(result["answer"])

    print("\nRetrieved Sources:\n")

    for citation in result["citations"]:
        print(citation)