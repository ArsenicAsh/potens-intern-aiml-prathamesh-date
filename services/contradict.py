import os

from dotenv import load_dotenv
from google import genai

from services.ingest import load_document_by_name

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def check_contradiction(document1, document2, topic):
    """
    Compare two documents on a given topic and determine
    whether they contradict each other.
    """

    doc1 = load_document_by_name(document1)
    doc2 = load_document_by_name(document2)

    if doc1 is None:
        return {
            "error": f"Document '{document1}' not found."
        }

    if doc2 is None:
        return {
            "error": f"Document '{document2}' not found."
        }

    prompt = f"""
You are a technical documentation reviewer.

Compare the two documents ONLY with respect to the topic below.

Topic:
{topic}

----------------------------
Document A:
{doc1}

----------------------------
Document B:
{doc2}

Determine whether the two documents contradict each other.

Return your response in the following format:

Contradiction: Yes or No

Reasoning:
<Explain your reasoning clearly in 2-4 sentences.>

Do NOT invent contradictions.
If the documents complement each other, explicitly say so.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return {
        "document1": document1,
        "document2": document2,
        "topic": topic,
        "result": response.text
    }


if __name__ == "__main__":

    result = check_contradiction(
        "01_rag_fundamentals.md",
        "05_hallucination_and_ai_safety.md",
        "Reducing Hallucinations"
    )

    print(result["result"])