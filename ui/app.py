import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="DocLens AI",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

with st.sidebar:

    st.title("📚 DocLens AI")

    st.markdown("### Knowledge Base")

    st.success("Indexed Topics")

    st.markdown("""
- Retrieval-Augmented Generation (RAG)
- Embeddings
- Vector Databases
- Prompt Engineering
- Hallucination & AI Safety
""")

    st.divider()

    st.markdown("### Tech Stack")

    st.markdown("""
- Gemini 2.5 Flash
- Sentence Transformers
- ChromaDB
- FastAPI
- Streamlit
""")

    st.divider()

    st.info(
        "Supports English, Hindi and Marathi queries."
    )

    st.divider()

    st.caption(
        "Built for Potens Internship Assessment 2026"
    )

# ---------------------------------------------------
# Header
# ---------------------------------------------------

st.title("📚 DocLens AI")

st.markdown(
    """
### Explainable Multilingual RAG Assistant

Ask questions over a curated technical knowledge base and receive
grounded responses backed by retrieved documentation and citations.
"""
)

st.divider()

# ---------------------------------------------------
# Example Questions
# ---------------------------------------------------

st.markdown("### 💡 Try asking")

col1, col2 = st.columns(2)

with col1:

    st.code("What is RAG?")

    st.code("How do embeddings work?")

with col2:

    st.code("How does RAG reduce hallucinations?")

    st.code("Explain vector databases.")

st.divider()

# ---------------------------------------------------
# Question Input
# ---------------------------------------------------

question = st.text_area(
    "Ask a Question",
    placeholder="Example: What is RAG and how does it reduce hallucinations?",
    height=120
)

# ---------------------------------------------------
# Ask Button
# ---------------------------------------------------

if st.button("🚀 Generate Response", use_container_width=True):

    if question.strip():

        try:

            with st.spinner(
                "Retrieving relevant documentation and generating grounded response..."
            ):

                response = requests.post(
                    f"{API_URL}/ask",
                    json={
                        "question": question
                    },
                    timeout=60
                )

                response.raise_for_status()

                result = response.json()

            st.divider()

            # -----------------------------
            # Metrics
            # -----------------------------

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Documents Retrieved",
                    len(result["citations"])
                )

            with col2:

                st.metric(
                    "Response Status",
                    "Grounded ✅"
                )

            st.divider()

            # -----------------------------
            # Answer
            # -----------------------------

            st.success("Grounded Response")

            st.markdown(result["answer"])

            st.divider()

            # -----------------------------
            # Citations
            # -----------------------------

            st.subheader("📚 Supporting Evidence")

            for citation in result["citations"]:

                with st.container(border=True):

                    st.markdown(
                        f"""
**📄 Source**

`{citation['source']}`

**Section**

{citation['section']}

**Chunk ID**

{citation['chunk_id']}
"""
                    )

        except requests.exceptions.ConnectionError:

            st.error(
                "Unable to connect to the FastAPI server.\n\n"
                "Please make sure the backend is running."
            )

        except Exception as e:

            st.error(str(e))

st.divider()

st.caption(
    "DocLens AI • Explainable AI • Grounded Generation • Semantic Retrieval"
)