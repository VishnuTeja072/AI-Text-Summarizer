import streamlit as st
from src.summarizer import summarize_text
from src.pdf_reader import extract_text_from_pdf

st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 AI Text Summarizer")
st.write(
    "Summarize long text or PDF documents using **Transformer-based NLP models**."
)

option = st.radio(
    "Choose Input Type:",
    ["Text", "PDF"]
)

if option == "Text":
    input_text = st.text_area(
        "✍️ Paste your text here",
        height=250
    )

    if st.button("📌 Summarize Text"):
        with st.spinner("Generating summary..."):
            summary = summarize_text(input_text)
            st.subheader("📝 Summary")
            st.success(summary)

else:
    uploaded_file = st.file_uploader(
        "📄 Upload a PDF file",
        type=["pdf"]
    )

    if uploaded_file and st.button("📌 Summarize PDF"):
        with st.spinner("Reading and summarizing PDF..."):
            pdf_text = extract_text_from_pdf(uploaded_file)
            summary = summarize_text(pdf_text)
            st.subheader("📝 Summary")
            st.success(summary)
