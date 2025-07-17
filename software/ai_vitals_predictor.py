# ai_vitals_predictor.py

"""
Simulated AI Model for Predicting Vital Signs from Temperature
Author: HealthSphere X Team
Date: 2025
"""

import random
import json

def predict_vitals(body_temp, age=None, gender=None, prior_conditions=None):
    """
    Simulate AI prediction of vitals from temperature and optional metadata.
    """
    # Default ranges (mock logic)
    heart_rate = random.randint(70, 100)
    spo2 = random.randint(95, 99)
    systolic = random.randint(110, 130)
    diastolic = random.randint(70, 90)
    
    # Simulated logic based on temperature
    if body_temp >= 38.0:
        heart_rate += 10
        spo2 -= 2
        systolic += 5
        diastolic += 3
    elif body_temp <= 36.0:
        heart_rate -= 5
        spo2 += 1
        systolic -= 5
        diastolic -= 3

    # Adjustments based on age or conditions (simulated logic)
    if age and age > 60:
        systolic += 10
        diastolic += 5

    if prior_conditions and "hypertension" in prior_conditions.lower():
        systolic += 15
        diastolic += 10

    result = {
        "Temperature": body_temp,
        "Predicted_Heart_Rate": heart_rate,
        "Predicted_SPO2": spo2,
        "Predicted_BP": f"{systolic}/{diastolic}"
    }

    return json.dumps(result, indent=4)

# Example usage
if __name__ == "__main__":
    temp = 38.5
    prediction = predict_vitals(temp, age=65, prior_conditions="Hypertension")
    print("Simulated AI Prediction from Temperature Input:")
    print(prediction)

