from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load pre-trained models
models = {
    "diabetes": joblib.load("models/diabetes_model.pkl"),
    "heart_disease": joblib.load("models/heart_disease_model.pkl"),
    "parkinsons": joblib.load("models/parkinsons_model.pkl"),
    "lung_disease": joblib.load("models/lung_disease_model.pkl"),
}

# Define API endpoint
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    disease = data.get("disease")  # Type of disease to predict
    features = data.get("features")  # List of feature values
    
    if disease not in models:
        return jsonify({"error": "Invalid disease type"}), 400
    
    model = models[disease]
    prediction = model.predict([np.array(features)])
    
    result = "Positive" if prediction[0] == 1 else "Negative"
    return jsonify({"disease": disease, "prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
