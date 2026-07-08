import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="DocLens AI",
    page_icon="📚",
    layout="centered"
)

st.title("📚 DocLens AI")

st.caption("Technical Documentation Assistant")

st.divider()

question = st.text_input(
    "Ask a question about the knowledge base"
)

if st.button("Ask"):

    if question.strip():

        with st.spinner("Searching documentation..."):

            response = requests.post(

                f"{API_URL}/ask",

                json={
                    "question": question
                }

            )

            result = response.json()

        st.subheader("Answer")

        st.write(result["answer"])

        st.divider()

        st.subheader("Supporting Citations")

        for citation in result["citations"]:

            st.markdown(
                f"""
**📄 {citation['source']}**

Section: {citation['section']}
"""
            )