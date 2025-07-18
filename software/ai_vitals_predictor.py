# ai_vitals_predictor.py

import json
from typing import List, Dict, Any

# Simulated dataset (as list of mock patient cases)
simulated_cases = [
    {"temperature": 36.5, "age": 25, "history": "none"},
    {"temperature": 38.3, "age": 70, "history": "hypertension"},
    {"temperature": 39.5, "age": 10, "history": "asthma"},
    {"temperature": 40.1, "age": 55, "history": "diabetes"},
    {"temperature": 37.8, "age": 35, "history": "none"},
]

def predict_condition(
    temperature: float,
    age: int = 30,
    history: str = "none"
) -> Dict[str, Any]:
    """
    Predicts health condition based on temperature, age, and medical history.

    Args:
        temperature (float): Body temperature in Celsius.
        age (int, optional): Age of the patient. Default is 30.
        history (str, optional): Medical history. Default is "none".

    Returns:
        dict: Prediction result including condition, risk factor, alert level, and recommendation.
    """
    # Initial status assignment based on temperature
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

    # Increase alert for high-risk histories
    high_risk_histories = {"diabetes", "hypertension", "asthma"}
    if history.lower() in high_risk_histories and temperature > 38:
        alert = "Emergency"
        risk += " | Underlying condition detected"

    # Recommendations by alert level
    recommendations = {
        "Safe": "Maintain healthy habits.",
        "Moderate": "Warm up and monitor temperature.",
        "Caution": "Stay hydrated and rest.",
        "Concern": "Use fever reducer; monitor closely.",
        "Emergency": "Seek medical attention immediately."
    }
    recommendation = recommendations.get(alert, "Consult a healthcare provider.")

    return {
        "temperature": temperature,
        "age": age,
        "history": history,
        "condition": status,
        "risk_factor": risk,
        "alert_level": alert,
        "recommendation": recommendation
    }

def test_predictions(cases: List[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    """
    Runs the predictor on a list of cases and returns the predictions.

    Args:
        cases (list, optional): List of patient case dicts. Defaults to simulated_cases.

    Returns:
        list: List of prediction results.
    """
    if cases is None:
        cases = simulated_cases
    return [
        predict_condition(
            case.get("temperature"),
            case.get("age", 30),
            case.get("history", "none")
        )
        for case in cases
    ]

if __name__ == "__main__":
    print(json.dumps(test_predictions(), indent=2))
