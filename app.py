import streamlit as st
import joblib
import numpy as np

# Load models safely
models = {}
try:
    models = {
        "Diabetes": joblib.load("models/diabetes_model.pkl"),
        "Heart Disease": joblib.load("models/heart_disease_model.pkl"),
        "Parkinson's": joblib.load("models/parkinsons_model.pkl"),
    }
except Exception as e:
    st.error(f"⚠️ Error loading models: {e}")

# Streamlit UI
st.title("🩺 AI Disease Prediction System")
st.markdown("### Predict the likelihood of a disease using machine learning models.")

# Select disease
disease = st.selectbox("🔍 Select a Disease:", list(models.keys()))

# Define parameters for each disease
disease_params = {
    "Diabetes": ["Glucose Level", "Blood Pressure", "BMI", "Age"],
    "Heart Disease": ["Cholesterol Level", "Blood Pressure", "Heart Rate", "Age"],
    "Parkinson's": ["Tremor Severity", "Voice Changes", "Muscle Stiffness", "Age"],
}

if disease:
    st.subheader(f"📊 Enter the required values for {disease}:")
    user_inputs = []

    for param in disease_params[disease]:
        value = st.number_input(f"🔹 {param}", min_value=0.0, step=0.1)
        user_inputs.append(value)

    if st.button("🧪 Predict"):
        try:
            model = models[disease]
            prediction = model.predict([np.array(user_inputs)])
            result = "Positive" if prediction[0] == 1 else "Negative"

            if result == "Positive":
                st.error(f"🚨 The model predicts **{disease} Positive**. Please consult a doctor.")
            else:
                st.success(f"✅ The model predicts **{disease} Negative**. No signs detected.")
        
        except Exception as e:
            st.error(f"⚠️ Error making prediction: {e}")
