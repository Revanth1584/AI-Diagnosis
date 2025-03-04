document.addEventListener("DOMContentLoaded", function () {
    const diseaseSelect = document.getElementById("disease");
    const inputFields = document.getElementById("input-fields");
    const predictButton = document.getElementById("predict-btn");
    const resultDiv = document.getElementById("result");

    // Disease-specific input fields
    const diseaseParameters = {
        "diabetes": ["Glucose Level", "Blood Pressure", "BMI", "Age"],
        "heart_disease": ["Cholesterol Level", "Blood Pressure", "Heart Rate", "Age"],
        "lung_cancer": ["Smoking History", "Cough Intensity", "Shortness of Breath", "Age"],
        "parkinsons": ["Tremor Severity", "Voice Changes", "Muscle Stiffness", "Age"]
    };

    // Update input fields when disease is selected
    diseaseSelect.addEventListener("change", function () {
        inputFields.innerHTML = "";
        const selectedDisease = diseaseSelect.value;
        if (selectedDisease) {
            diseaseParameters[selectedDisease].forEach(param => {
                const input = document.createElement("input");
                input.type = "number";
                input.placeholder = param;
                input.dataset.param = param;
                inputFields.appendChild(input);
            });
        }
    });

    // Predict function
    predictButton.addEventListener("click", function () {
        const selectedDisease = diseaseSelect.value;
        if (!selectedDisease) {
            alert("Please select a disease first.");
            return;
        }

        // Collect input values
        const inputs = Array.from(inputFields.querySelectorAll("input")).map(input => ({
            name: input.dataset.param,
            value: parseFloat(input.value)
        }));

        // Validate inputs
        if (inputs.some(input => isNaN(input.value))) {
            alert("Please enter valid values for all parameters.");
            return;
        }

        // Send data to backend (Replace this with actual API call)
        fetch("http://localhost:5000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ disease: selectedDisease, parameters: inputs })
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.innerHTML = `Prediction: ${data.prediction}`;
            resultDiv.style.color = data.prediction === "High Risk" ? "red" : "green";
        })
        .catch(error => console.error("Error:", error));
    });
});
