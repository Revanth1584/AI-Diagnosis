import gradio as gr
import joblib
import numpy as np

# Load models
models = {
    "Diabetes": joblib.load("models/diabetes_model.pkl"),
    "Heart Disease": joblib.load("models/heart_disease_model.pkl"),
    "Parkinson's": joblib.load("models/parkinsons_model.pkl"),
}

def predict(disease, *features):
    model = models.get(disease)
    if model:
        prediction = model.predict([np.array(features)])
        return "Positive" if prediction[0] == 1 else "Negative"
    return "Error: Model not found"

# Gradio UI
diseases = list(models.keys())
demo = gr.Interface(
    fn=predict,
    inputs=[gr.Dropdown(diseases, label="Select Disease")] +
           [gr.Number(label=f"Feature {i+1}") for i in range(4)],
    outputs="text",
    title="AI Disease Prediction System",
)

demo.launch()
