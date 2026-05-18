import warnings
warnings.filterwarnings("ignore")

import streamlit as st
from transformers import pipeline
from pypdf import PdfReader
import re

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="AI Study Assistant",
    layout="wide"
)

st.title("📘 AI Study Assistant")
st.write(
    "Upload PDF notes and generate summaries, quizzes, and flashcards."
)

# ----------------------------
# LOAD AI MODEL
# ----------------------------
@st.cache_resource
def load_model():

    summarizer = pipeline(
        task="summarization",
        model="sshleifer/distilbart-cnn-12-6",
        device=-1
    )

    return summarizer

summarizer = load_model()

# ----------------------------
# PDF TEXT EXTRACTION
# ----------------------------
def extract_text_from_pdf(pdf_file):

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:

        extracted = page.extract_text()

        if extracted:
            text += extracted + " "

    return text

# ----------------------------
# CLEAN TEXT
# ----------------------------
def clean_text(text):

    text = re.sub(r'\s+', ' ', text)

    return text.strip()

# ----------------------------
# GENERATE SUMMARY
# ----------------------------
def generate_summary(text):

    if len(text) > 3000:
        text = text[:3000]

    summary = summarizer(
        text,
        max_length=150,
        min_length=50,
        do_sample=False
    )

    return summary[0]["summary_text"]

# ----------------------------
# GENERATE QUIZ
# ----------------------------
def generate_quiz(text):

    sentences = text.split('.')

    questions = []

    for i, sentence in enumerate(sentences[:10]):

        sentence = sentence.strip()

        if len(sentence) > 40:

            questions.append(
                f"Q{i+1}: Explain:\n{sentence}?"
            )

    return questions

# ----------------------------
# GENERATE FLASHCARDS
# ----------------------------
def generate_flashcards(text):

    sentences = text.split('.')

    flashcards = []

    for i, sentence in enumerate(sentences[:8]):

        sentence = sentence.strip()

        if len(sentence) > 30:

            keyword = sentence.split()[0]

            flashcards.append({
                "question": f"What is {keyword}?",
                "answer": sentence
            })

    return flashcards

# ----------------------------
# FILE UPLOAD
# ----------------------------
uploaded_file = st.file_uploader(
    "Upload PDF File",
    type=["pdf"]
)

# ----------------------------
# PROCESS FILE
# ----------------------------
if uploaded_file:

    with st.spinner("Reading PDF..."):

        raw_text = extract_text_from_pdf(uploaded_file)

        cleaned_text = clean_text(raw_text)

    st.success("PDF uploaded successfully!")

    # Preview Section
    st.subheader("📄 Extracted Text Preview")

    st.text_area(
        "Preview",
        cleaned_text[:2000],
        height=250
    )

    # Buttons
    col1, col2, col3 = st.columns(3)

    # SUMMARY
    with col1:

        if st.button("Generate Summary"):

            with st.spinner("Generating summary..."):

                summary = generate_summary(cleaned_text)

            st.subheader("📝 Summary")

            st.write(summary)

    # QUIZ
    with col2:

        if st.button("Generate Quiz"):

            quiz = generate_quiz(cleaned_text)

            st.subheader("❓ Quiz Questions")

            for q in quiz:
                st.write(q)

    # FLASHCARDS
    with col3:

        if st.button("Generate Flashcards"):

            flashcards = generate_flashcards(cleaned_text)

            st.subheader("🧠 Flashcards")

            for card in flashcards:

                st.markdown(
                    f"**Q:** {card['question']}"
                )

                st.write(
                    f"A: {card['answer']}"
                )

                st.markdown("---")

# ----------------------------
# FOOTER
# ----------------------------
st.markdown("---")

st.caption(
    "Offline AI Study Assistant using HuggingFace + Streamlit"
)
