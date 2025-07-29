# 🧠 HealthSphere X – AI Model

This folder contains the AI logic powering the offline diagnostic capabilities of HealthSphere X. The models support prediction of vital signs, early warning for illnesses, and basic care suggestions.

## 🔗 Core AI Pipeline

1. **Input**: Body temperature, age, gender, medical history
2. **Predict Vitals**: AI model estimates SpO₂, heart rate, and blood pressure
3. **Detect Conditions**: AI identifies abnormal patterns (e.g., fever, hypothermia)
4. **Recommend Care**: Suggests basic home care or alerts for emergency help

See `ai-logic-diagram.png` for the full logic flow.

---

## 📂 File Structure

| File                             | Purpose                                                      |
|----------------------------------|--------------------------------------------------------------|
| `predict.py`                     | Inference script using the trained models                    |
| `train-model.py`                 | Main training pipeline using `training-data.csv`             |
| `training-data.csv`             | Simulated dataset for temperature-vitals correlation         |
| `temperature-vitals-model.ipynb`| Predict vitals from temperature + demographics               |
| `condition-predictor-model.ipynb`| Identify illnesses from temperature trends                   |
| `prescription-ai-module.ipynb`  | Provide basic prescription recommendations                   |
| `model-architecture.md`         | Description of architecture used for each model              |
| `model-usage-guide.md`          | Explains how to run and integrate the models on ESP32        |
| `ai-logic-diagram.png`          | Visual schematic of AI logic pipeline                        |

---

## 🗃️ Model Overview

### 🔬 Vitals Prediction
**Model**: `temperature-vitals-model.ipynb`  
**Inputs**: Temperature, age, gender  
**Outputs**: SpO₂, Heart Rate, Blood Pressure

---

### 🚨 Condition Detection
**Model**: `condition-predictor-model.ipynb`  
**Purpose**: Predict possible fever, hypothermia, or infection patterns.

---

### 💊 Home Care Recommendation
**Model**: `prescription-ai-module.ipynb`  
Provides home care advice (not medical-grade) based on symptoms detected.

---

## 🧪 Limitations

- Models trained on simulated and generalized datasets
- Not yet validated with real patient data
- Only temperature-based — no wearable or biometric inputs

---

## ✅ Future Upgrades

- Incorporate real-world patient datasets
- Add symptom check via image/audio analysis
- Optimize models for ESP32-CAM memory constraints
