import streamlit as st
import PyPDF2

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="AI Study Assistant",
    layout="wide"
)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.title("📘 AI Study Assistant")

st.write(
    "Upload your PDF notes and generate summaries, quizzes, and flashcards."
)

# ---------------------------------------------------
# PDF TEXT EXTRACTION FUNCTION
# ---------------------------------------------------
def extract_text_from_pdf(uploaded_file):

    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + " "

    return text

# ---------------------------------------------------
# SUMMARY FUNCTION
# ---------------------------------------------------
def generate_summary(text):

    if len(text) > 1000:
        summary = text[:1000]
    else:
        summary = text

    return summary

# ---------------------------------------------------
# QUIZ FUNCTION
# ---------------------------------------------------
def generate_quiz(text):

    sentences = text.split(".")

    quiz_questions = []

    count = 1

    for sentence in sentences:

        sentence = sentence.strip()

        if len(sentence) > 30:

            question = f"Q{count}: Explain this statement:\n{sentence}?"

            quiz_questions.append(question)

            count += 1

        if count > 5:
            break

    return quiz_questions

# ---------------------------------------------------
# FLASHCARD FUNCTION
# ---------------------------------------------------
def generate_flashcards(text):

    sentences = text.split(".")

    flashcards = []

    count = 1

    for sentence in sentences:

        sentence = sentence.strip()

        if len(sentence) > 30:

            words = sentence.split()

            keyword = words[0]

            flashcards.append({
                "question": f"What is {keyword}?",
                "answer": sentence
            })

            count += 1

        if count > 5:
            break

    return flashcards

# ---------------------------------------------------
# FILE UPLOADER
# ---------------------------------------------------
uploaded_file = st.file_uploader(
    "Upload PDF File",
    type=["pdf"]
)

# ---------------------------------------------------
# PROCESS PDF
# ---------------------------------------------------
if uploaded_file is not None:

    with st.spinner("Reading PDF file..."):

        pdf_text = extract_text_from_pdf(uploaded_file)

    st.success("PDF uploaded successfully!")

    # ---------------------------------------------------
    # TEXT PREVIEW
    # ---------------------------------------------------
    st.subheader("📄 Extracted Text Preview")

    st.text_area(
        "Preview",
        pdf_text[:2000],
        height=250
    )

    # ---------------------------------------------------
    # BUTTON SECTION
    # ---------------------------------------------------
    col1, col2, col3 = st.columns(3)

    # SUMMARY BUTTON
    with col1:

        if st.button("Generate Summary"):

            summary = generate_summary(pdf_text)

            st.subheader("📝 Summary")

            st.write(summary)

    # QUIZ BUTTON
    with col2:

        if st.button("Generate Quiz"):

            quiz = generate_quiz(pdf_text)

            st.subheader("❓ Quiz Questions")

            for question in quiz:

                st.write(question)

    # FLASHCARD BUTTON
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

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("---")

st.caption("AI Study Assistant using Streamlit + Python")
