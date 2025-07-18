# ai_vitals_predictor.py

import random
import json

# Simulated dataset (as list of mock patient cases)
simulated_cases = [
    {"temperature": 36.5, "age": 25, "history": "none"},
    {"temperature": 38.3, "age": 70, "history": "hypertension"},
    {"temperature": 39.5, "age": 10, "history": "asthma"},
    {"temperature": 40.1, "age": 55, "history": "diabetes"},
    {"temperature": 37.8, "age": 35, "history": "none"},
]

# Predict health condition from temperature and history
def predict_condition(temperature, age=30, history="none"):
    if temperature < 36.0:
        status = "Hypothermia"
        risk = "Low circulation or cold exposure"
        alert = "Moderate"
    elif 36.0 <= temperature <= 37.5:
        status = "Normal"
        risk = "None"
        alert = "Safe"
    elif 37.6 <= temperature <= 38.4:
        status = "Low-grade Fever"
        risk = "May indicate mild infection"
        alert = "Caution"
    elif 38.5 <= temperature <= 39.5:
        status = "High Fever"
        risk = "Likely infection or flu"
        alert = "Concern"
    else:
        status = "Critical Fever"
        risk = "Possible severe infection or heatstroke"
        alert = "Emergency"

    # Modify based on history
    if history in ["diabetes", "hypertension", "asthma"] and temperature > 38:
        alert = "Emergency"
        risk += " | Underlying condition detected"

    # Recommendations
    recommendation = "Stay hydrated and rest."
    if alert == "Concern":
        recommendation = "Use fever reducer; monitor closely."
    elif alert == "Emergency":
        recommendation = "Seek medical attention immediately."

    return {
        "temperature": temperature,
        "condition": status,
        "risk_factor": risk,
        "alert_level": alert,
        "recommendation": recommendation
    }

# Test the predictor on simulated data
def test_predictions():
    results = []
    for case in simulated_cases:
        prediction = predict_condition(
            case["temperature"],
            case["age"],
            case["history"]
        )
        results.append(prediction)
    return results

if __name__ == "__main__":
    print(json.dumps(test_predictions(), indent=2))
