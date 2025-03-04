document.addEventListener("DOMContentLoaded", function () {
    const diseaseSelect = document.getElementById("disease");
    const parameterForm = document.getElementById("parameter-form");
    const predictButton = document.getElementById("predict-btn");
    const resultDiv = document.getElementById("result");

    // Disease-specific input fields
    const diseaseParameters = {
        "diabetes": ["Glucose Level", "Blood Pressure", "BMI", "Age"],
        "heart_disease": ["Cholesterol Level", "Blood Pressure", "Heart Rate", "Age"],
        "parkinsons": ["Tremor Severity", "Voice Changes", "Muscle Stiffness", "Age"]
    };

    // Update input fields when disease is selected
    diseaseSelect.addEventListener("change", function () {
        parameterForm.innerHTML = "";
        const selectedDisease = diseaseSelect.value;
        if (selectedDisease) {
            diseaseParameters[selectedDisease].forEach(param => {
                const input = document.createElement("input");
                input.type = "number";
                input.placeholder = param;
                input.dataset.param = param;
                parameterForm.appendChild(input);
            });
            predictButton.style.display = "block";
        } else {
            predictButton.style.display = "none";
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
        const inputs = Array.from(parameterForm.querySelectorAll("input")).map(input => parseFloat(input.value));

        // Validate inputs
        if (inputs.some(value => isNaN(value))) {
            alert("Please enter valid values for all parameters.");
            return;
        }

        // Send data to Flask backend
        fetch("/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ disease: selectedDisease, features: inputs })
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.innerHTML = `Prediction: ${data.prediction}`;
            resultDiv.style.color = data.prediction === "Positive" ? "red" : "green";
        })
        .catch(error => console.error("Error:", error));
    });
});
