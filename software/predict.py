# predict.py

import json
from typing import List, Dict, Any

# Simulated dataset (mock patient vitals)
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
    Predicts health condition based on body temperature, age, and medical history.

    Args:
        temperature (float): Body temperature in Celsius.
        age (int): Patient's age.
        history (str): Medical history (e.g., 'diabetes', 'asthma').

    Returns:
        dict: Condition summary, risk factor, alert level, and recommendation.
    """
    if temperature < 36.0:
        condition = "Hypothermia"
        risk = "Cold exposure / poor circulation"
        alert = "Moderate"
    elif 36.0 <= temperature <= 37.5:
        condition = "Normal"
        risk = "None"
        alert = "Safe"
    elif 37.6 <= temperature <= 38.4:
        condition = "Low-grade Fever"
        risk = "Possible mild infection"
        alert = "Caution"
    elif 38.5 <= temperature <= 39.5:
        condition = "High Fever"
        risk = "Likely infection or flu"
        alert = "Concern"
    else:
        condition = "Critical Fever"
        risk = "Severe infection or heatstroke"
        alert = "Emergency"

    # High-risk underlying conditions
    high_risk = {"diabetes", "hypertension", "asthma"}
    if history.lower() in high_risk and temperature > 38:
        alert = "Emergency"
        risk += " | Underlying risk factor present"

    # Age-based modifiers
    if age < 5 or age > 65 and alert in {"Concern", "Caution"}:
        alert = "Emergency"
        risk += " | Age-related vulnerability"

    # Recommendations
    advice = {
        "Safe": "No concern. Keep hydrated and well-rested.",
        "Moderate": "Wrap in warm clothing. Recheck temperature.",
        "Caution": "Rest, hydrate, and monitor symptoms.",
        "Concern": "Use fever reducers. Monitor and reassess.",
        "Emergency": "Seek medical attention immediately."
    }

    return {
        "temperature": temperature,
        "age": age,
        "history": history,
        "condition": condition,
        "risk_factor": risk,
        "alert_level": alert,
        "recommendation": advice.get(alert, "Consult a healthcare provider.")
    }

def test_predictions(cases: List[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    """
    Test the model with provided or simulated cases.
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
    results = test_predictions()
    with open("prediction_log.json", "w") as f:
        json.dump(results, f, indent=2)
    print("Prediction complete. Results saved to prediction_log.json.")
