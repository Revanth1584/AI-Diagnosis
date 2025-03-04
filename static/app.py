from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load pre-trained models
models = {
    "diabetes": joblib.load("models/diabetes_model.pkl"),
    "heart_disease": joblib.load("models/heart_disease_model.pkl"),
    "parkinsons": joblib.load("models/parkinsons_model.pkl"),
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        disease = data.get("disease")
        features = data.get("features")

        if disease not in models:
            return jsonify({"error": "Invalid disease type"}), 400

        model = models[disease]
        prediction = model.predict([np.array(features)])

        result = "Positive" if prediction[0] == 1 else "Negative"
        return jsonify({"disease": disease, "prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
