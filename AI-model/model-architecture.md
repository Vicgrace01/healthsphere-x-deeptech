# 🧠 Model Architecture Overview

This document explains the structure of each AI model in HealthSphere X.

---

## 1. Vitals Prediction Model
**File**: `temperature-vitals-model.ipynb`  
**Input Features**:
- Body temperature (°C)
- Age (numeric)
- Gender (binary)
- Patient history (optional)

**Model Type**: Linear Regression (or MLP in later versions)  
**Output**:
- SpO₂ (%)
- Heart Rate (BPM)
- Blood Pressure (mmHg)

---

## 2. Illness Condition Predictor
**File**: `condition-predictor-model.ipynb`  
**Input Features**:
- Recent temperature values
- Trend over time

**Model Type**: Decision Tree / Lightweight RNN  
**Output**:
- Fever risk
- Hypothermia likelihood
- Suspected viral pattern

---

## 3. Prescription Recommendation Engine
**File**: `prescription-ai-module.ipynb`  
**Input**:
- Predicted vitals
- Condition flags

**Logic**:
- Rule-based mapping (e.g., low SpO₂ → emergency)
- Lookup table from WHO/national health guidelines

**Output**:
- Home care tip
- Escalation suggestion
