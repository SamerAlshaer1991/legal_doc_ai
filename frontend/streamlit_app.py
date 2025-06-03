import streamlit as st
import requests

st.title("LexiMind - Legal Document Classifier")

uploaded_file = st.file_uploader("Upload a legal document", type=["txt", "pdf"])

if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post("http://localhost:8000/classify", files=files)
    if response.ok:
        st.success(f"Predicted Document Type: {response.json()['label']}")
    else:
        st.error("Classification failed.")
