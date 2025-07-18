# predict.py
import joblib
import pandas as pd

# Load model
model = joblib.load("healthsphere_model.pkl")

# Simulated input (can replace with real sensor values)
input_data = {
    "Temperature": [38.2],
    "Cough": [1],
    "Fatigue": [1],
    "Headache": [0],
    "PatientHistory": [2]  # e.g., 0: None, 1: Mild, 2: Chronic
}

df = pd.DataFrame(input_data)

# Predict
prediction = model.predict(df)

# Extract output
predicted_condition, prevention_tip, prescription = prediction[0]

print(f"""
🩺 Prediction Result:
- Condition: {predicted_condition}
- Prevention: {prevention_tip}
- Prescription: {prescription}
""")

