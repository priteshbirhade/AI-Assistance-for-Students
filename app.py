import streamlit as st

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="AI Healthcare Assistant",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title("🏥 AI Healthcare Assistant")

st.write(
    "This AI Healthcare Assistant helps analyze symptoms and provides basic health suggestions."
)

# --------------------------------------------------
# PATIENT DETAILS
# --------------------------------------------------
st.subheader("👤 Patient Information")

patient_name = st.text_input("Patient Name")

patient_age = st.number_input(
    "Patient Age",
    min_value=1,
    max_value=120,
    value=25
)

patient_gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)

# --------------------------------------------------
# SYMPTOMS INPUT
# --------------------------------------------------
st.subheader("🩺 Enter Symptoms")

symptoms = st.text_area(
    "Type symptoms separated by commas",
    placeholder="Example: fever, cough, headache"
)

# --------------------------------------------------
# DISEASE PREDICTION FUNCTION
# --------------------------------------------------
def predict_disease(user_symptoms):

    user_symptoms = user_symptoms.lower()

    if "fever" in user_symptoms and "cough" in user_symptoms:
        return "Possible Flu or Viral Infection"

    elif "headache" in user_symptoms and "vomiting" in user_symptoms:
        return "Possible Migraine"

    elif "chest pain" in user_symptoms:
        return "Possible Heart-related Problem"

    elif "stomach pain" in user_symptoms:
        return "Possible Gastric Issue"

    elif "cold" in user_symptoms:
        return "Possible Common Cold"

    elif "diabetes" in user_symptoms:
        return "Possible Blood Sugar Issue"

    else:
        return "Symptoms unclear. Please consult a medical professional."

# --------------------------------------------------
# HEALTH RECOMMENDATION FUNCTION
# --------------------------------------------------
def health_recommendations():

    recommendations = [
        "Drink plenty of water",
        "Take proper rest",
        "Eat healthy food",
        "Exercise regularly",
        "Avoid junk food",
        "Sleep at least 7-8 hours daily"
    ]

    return recommendations

# --------------------------------------------------
# ANALYZE BUTTON
# --------------------------------------------------
if st.button("Analyze Symptoms"):

    if symptoms.strip() == "":

        st.warning("Please enter symptoms before analysis.")

    else:

        predicted_result = predict_disease(symptoms)

        st.success("Analysis Completed Successfully")

        # --------------------------------------------------
        # REPORT SECTION
        # --------------------------------------------------
        st.subheader("📋 Patient Report")

        st.write(f"👤 Patient Name: {patient_name}")

        st.write(f"🎂 Age: {patient_age}")

        st.write(f"⚧ Gender: {patient_gender}")

        st.write(f"🩺 Symptoms: {symptoms}")

        # --------------------------------------------------
        # PREDICTION RESULT
        # --------------------------------------------------
        st.subheader("🧠 AI Prediction")

        st.error(predicted_result)

        # --------------------------------------------------
        # HEALTH TIPS
        # --------------------------------------------------
        st.subheader("💡 Health Recommendations")

        tips = health_recommendations()

        for tip in tips:

            st.write(f"✅ {tip}")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")

st.caption("AI Healthcare Assistant using Python + Streamlit")
