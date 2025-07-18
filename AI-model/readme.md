# HealthSphere X AI Models

The AI system powering **HealthSphere X** is designed around a three-pronged approach to community-centered healthcare:

> **Predict. Prevent. Prescribe.**

---

## 🔬 1. Predict
HealthSphere X uses AI to infer vital signs (SpO₂, heart rate, blood pressure) from a simple temperature reading. This enables low-cost health monitoring even when only a digital thermometer is available.

- Model: `temperature-vitals-model.ipynb`
- Inputs: Body temperature (in °C), basic patient data (age, gender, history)
- Outputs: Predicted vitals (SpO₂, Heart Rate, BP)

Additionally, AI analyzes temperature trends to **predict potential illnesses** like:
- Fever & Malaria
- Hypothermia
- COVID-19 patterns
- Dengue-like symptoms

- Model: `condition-predictor-model.ipynb`

---

## 🚨 2. Prevent
Using historical health patterns and thresholds, the models flag early warning signs:

- Fever trend detection
- Dangerous vitals warning
- Personalized risk profiles (based on age, history, etc.)

This enables preventive steps before an emergency arises.

---

## 💊 3. Prescribe
Our AI module gives basic **prescription suggestions** when a doctor isn’t nearby:

- Mild Fever → Paracetamol + Rest
- Severe Fever → See doctor ASAP
- Low SpO₂ → Urgent medical attention
- Cold + Hypothermia → Apply warmth, hydrate

- Model: `prescription-ai-module.ipynb`

⚠️ Note: These are **suggestions**, not replacements for clinical diagnosis.

---

## 📁 Files Included

| Filename | Description |
|----------|-------------|
| `temperature-vitals-model.ipynb` | Predicts vitals (HR, BP, SpO₂) from temperature |
| `condition-predictor-model.ipynb` | Predicts illnesses based on temp patterns |
| `prescription-ai-module.ipynb` | Gives basic suggestions for home care or escalation |
| `readme.md` | This file |

---

## 🧠 Dataset

We used a combination of public medical references, anonymized simulations, and medically informed assumptions for training. Real data collection will improve performance over time.

---

## ✅ Future Improvements
- Integrate real patient history
- Personalize models based on region or demographics
- Expand to handle symptoms beyond temperature

---

