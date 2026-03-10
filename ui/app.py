import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("ContextIQ")

st.write("Upload a PDF and ask questions about it.")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file is not None:

    files = {"file": uploaded_file.getvalue()}

    response = requests.post(
        f"{API_URL}/upload-document",
        files={"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
    )

    if response.status_code == 200:
        st.success("Document uploaded successfully!")

question = st.text_input("Ask a question about the document")

if st.button("Ask"):

    if question:

        response = requests.get(
            f"{API_URL}/ask",
            params={"query": question}
        )

        answer = response.json()["answer"]

        st.subheader("Answer")
        st.write(answer)