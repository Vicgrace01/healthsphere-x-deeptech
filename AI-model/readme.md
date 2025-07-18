# HealthSphere X - AI Model

This folder contains the AI-driven logic used to simulate and predict vital signs based on body temperature and contextual patient data.

## 💡 Purpose
The goal is to provide proactive health assessment and triage by estimating:
- Blood Pressure (BP)
- Heart Rate (HR)
- Oxygen Saturation (SpO₂)
- Risk Level (Normal, Mild Fever, Severe, Emergency)

## 🔧 How it Works
- Input: Temperature value (°C)
- Output: Predicted vital signs and alert level
- Logic: Based on a mix of rule-based estimation and future AI extensibility
- Integration: Works on-device with ESP32-CAM or cloud-based via Firebase

## 🧪 Files
- `vitals-predictor.py`: Rule-based prediction script
- `training-data.csv`: Simulated input data
- `model-output-samples.txt`: Sample inputs and prediction outputs
- `ai-logic-diagram.png`: Optional diagram showing prediction flow (add if needed)

## 📈 Future Work
- Train with real patient datasets
- Improve prediction with TinyML models
- Integrate feedback from medical professionals

