import streamlit as st
import PyPDF2

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI Study Assistant",
    layout="wide"
)

# -----------------------------
# TITLE
# -----------------------------
st.title("📘 AI Study Assistant")

st.write(
    "Upload PDF notes and generate summaries, quizzes, and flashcards."
)

# -----------------------------
# EXTRACT PDF TEXT
# -----------------------------
def extract_text_from_pdf(uploaded_file):

    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:

        extracted_text = page.extract_text()

        if extracted_text:
            text += extracted_text

    return text

# -----------------------------
# GENERATE SUMMARY
# -----------------------------
def generate_summary(text):

    summary = text[:1000]

    return summary

# -----------------------------
# GENERATE QUIZ
# -----------------------------
def generate_quiz(text):

    sentences = text.split(".")

    quiz = []

    for i, sentence in enumerate(sentences[:5]):

        sentence = sentence.strip()

        if len(sentence) > 20:

            quiz.append(
                f"Q{i+1}: Explain this statement:\n{sentence}?"
            )

    return quiz

# -----------------------------
# GENERATE FLASHCARDS
# -----------------------------
def generate_flashcards(text):

    sentences = text.split(".")

    flashcards = []

    for sentence in sentences[:5]:

        sentence = sentence.strip()

        if len(sentence) > 20:

            words = sentence.split()

            keyword = words[0]

            flashcards.append({
                "question": f"What is {keyword}?",
                "answer": sentence
            })

    return flashcards

# -----------------------------
# FILE UPLOAD
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload PDF File",
    type=["pdf"]
)

# -----------------------------
# PROCESS FILE
# -----------------------------
if uploaded_file is not None:

    with st.spinner("Reading PDF..."):

        pdf_text = extract_text_from_pdf(uploaded_file)

    st.success("PDF uploaded successfully!")

    # Preview
    st.subheader("📄 Extracted Text Preview")

    st.text_area(
        "Preview",
        pdf_text[:2000],
        height=250
    )

    # Buttons
    col1, col2, col3 = st.columns(3)

    # SUMMARY
    with col1:

        if st.button("Generate Summary"):

            summary = generate_summary(pdf_text)

            st.subheader("📝 Summary")

            st.write(summary)

    # QUIZ
    with col2:

        if st.button("Generate Quiz"):

            quiz = generate_quiz(pdf_text)

            st.subheader("❓ Quiz Questions")

            for q in quiz:

                st.write(q)

    # FLASHCARDS
    with col3:

        if st.button("Generate Flashcards"):

            flashcards = generate_flashcards(pdf_text)

            st.subheader("🧠 Flashcards")

            for card in flashcards:

                st.markdown(
                    f"**Q:** {card['question']}"
                )

                st.write(
                    f"A: {card['answer']}"
                )

                st.markdown("---")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")

st.caption("AI Study Assistant using Streamlit")
