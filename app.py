import streamlit as st

st.title("AI Study Assistant")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("PDF uploaded successfully!")

    st.write("Filename:", uploaded_file.name)

    st.write("File size:", uploaded_file.size, "bytes")

    if st.button("Generate Summary"):

        st.subheader("Summary")

        st.write(
            "This is a sample summary generated successfully."
        )

    if st.button("Generate Quiz"):

        st.subheader("Quiz")

        st.write("1. What is the main topic?")
        st.write("2. Explain the concept.")

    if st.button("Generate Flashcards"):

        st.subheader("Flashcards")

        st.write("Q: What is AI?")
        st.write("A: Artificial Intelligence")
