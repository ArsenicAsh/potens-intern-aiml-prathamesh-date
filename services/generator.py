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
You are DocLens AI, a technical documentation assistant.

Use ONLY the information provided in the retrieved documentation below.

IMPORTANT RULES:

1. Respond in the SAME language as the user's question.
   - English question → English answer
   - Hindi question → Hindi answer
   - Marathi question → Marathi answer

2. Use ONLY the retrieved documentation.

3. Do NOT use your own knowledge.

4. Do NOT guess.

5. If the retrieved documentation does not contain enough information,
respond in the SAME language as the user's question that the available
documentation does not contain sufficient information to answer it.

6. Keep the answer concise, accurate, and well structured.

Question:
{question}

Retrieved Documentation:
{context}

Return your response in exactly this format:

Answer:
<answer in the user's language>

Evidence:
- Source: <filename>
  Section: <section>
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