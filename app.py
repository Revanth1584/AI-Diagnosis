import streamlit as st
import joblib
import numpy as np

# Load models
models = {
    "Diabetes": joblib.load("models/diabetes_model.pkl"),
    "Heart Disease": joblib.load("models/heart_disease.pkl"),
    "Parkinson's": joblib.load("models/parkinsons.pkl"),
}

# Streamlit UI
st.title("AI Disease Prediction")

# Select disease
disease = st.selectbox("Select a Disease", list(models.keys()))

# Input fields based on disease
disease_params = {
    "Diabetes": ["Glucose Level", "Blood Pressure", "BMI", "Age"],
    "Heart Disease": ["Cholesterol Level", "Blood Pressure", "Heart Rate", "Age"],
    "Parkinson's": ["Tremor Severity", "Voice Changes", "Muscle Stiffness", "Age"],
}

if disease:
    st.write(f"Enter the required values for {disease}:")
    user_inputs = []
    
    for param in disease_params[disease]:
        value = st.number_input(param, min_value=0.0, step=0.1)
        user_inputs.append(value)

    if st.button("Predict"):
        model = models[disease]
        prediction = model.predict([np.array(user_inputs)])
        result = "Positive" if prediction[0] == 1 else "Negative"
        
        if result == "Positive":
            st.error(f"The model predicts **{disease} Positive**.")
        else:
            st.success(f"The model predicts **{disease} Negative**.")
