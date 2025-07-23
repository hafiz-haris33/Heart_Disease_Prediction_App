import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("final_model.pkl")

# Page config
st.set_page_config(page_title="Heart Disease Predictor", page_icon="❤️", layout="centered")

# --- Custom CSS Styling ---
st.markdown("""
    <style>
        body { background-color: #f5f5f5; }
        .main {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 2rem;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: crimson;
        }
        .result-box {
            border-radius: 10px;
            padding: 1rem;
            margin-top: 1rem;
            text-align: center;
            font-size: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main'>", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1>❤️ Heart Disease Prediction</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border: 1px solid crimson;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Fill in the form below to check your risk of heart disease.</p>", unsafe_allow_html=True)

# --- Input Form ---
with st.form("prediction_form"):
    st.subheader("🩺 Patient Information")
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", min_value=1, max_value=120, step=1)
        sex = st.selectbox("Sex", ["Male", "Female"])
        cp = st.selectbox("Chest Pain Type", ["TA", "ATA", "NAP", "ASY"])

    with col2:
        trestbps = st.number_input("Resting Blood Pressure", min_value=80, max_value=200)
        chol = st.number_input("Cholesterol (mg/dl)", min_value=100, max_value=600)
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
        restecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])

    with col3:
        thalach = st.number_input("Max Heart Rate Achieved", min_value=60, max_value=250)
        exang = st.selectbox("Exercise Induced Angina", [0, 1])
        oldpeak = st.number_input("Oldpeak (ST depression)", step=0.1)
        slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

    submitted = st.form_submit_button("🔍 Predict")

# --- Prediction Result ---
if submitted:
    input_dict = {
        "Age": [age],
        "Sex": ["M" if sex == "Male" else "F"],
        "ChestPainType": [cp],
        "RestingBP": [trestbps],
        "Cholesterol": [chol],
        "FastingBS": [fbs],
        "RestingECG": [restecg],
        "MaxHR": [thalach],
        "ExerciseAngina": [exang],
        "Oldpeak": [oldpeak],
        "ST_Slope": [slope]
    }

    input_df = pd.DataFrame(input_dict)

    prediction = model.predict(input_df)[0]
    result_text = "✅ No Major Heart Disease Detected" if prediction == 0 else "🚨 High Risk of Heart Disease"

    if prediction == 0:
        st.success(result_text)
    else:
        st.error(result_text)

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:13px;'>Made with ❤️ by Haris</p>", unsafe_allow_html=True)
