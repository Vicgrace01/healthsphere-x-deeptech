# thresholds.py

THRESHOLDS = {
    "temperature": {
        "hypothermia": {"max": 35.9, "alert": "Moderate"},
        "normal": {"min": 36.0, "max": 37.5, "alert": "Safe"},
        "low_grade_fever": {"min": 37.6, "max": 38.4, "alert": "Caution"},
        "high_fever": {"min": 38.5, "max": 39.5, "alert": "Concern"},
        "critical_fever": {"min": 39.6, "alert": "Emergency"}
    },
    "high_risk_histories": {"diabetes", "hypertension", "asthma"},
    "alerts": {
        "Safe": "Maintain healthy habits.",
        "Moderate": "Warm up and monitor temperature.",
        "Caution": "Stay hydrated and rest.",
        "Concern": "Use fever reducer; monitor closely.",
        "Emergency": "Seek medical attention immediately."
    }
}

