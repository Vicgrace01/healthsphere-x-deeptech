# predict.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
df = pd.read_csv("training-data.csv")

# Select features and target columns
features = ['Temperature_C', 'Age', 'Gender']
targets = ['HeartRate_BPM', 'BloodPressure_Systolic', 'BloodPressure_Diastolic']

# Drop rows with missing data
df = df.dropna(subset=features + targets)

# Encode gender (Male = 1, Female = 0)
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})

# Split data
X = df[features]
y = df[targets]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "vitals_predictor_model.joblib")

# Example: load and run prediction
loaded_model = joblib.load("vitals_predictor_model.joblib")
sample_input = pd.DataFrame([{
    "Temperature_C": 38.0,
    "Age": 25,
    "Gender": 1  # Male
}])
prediction = loaded_model.predict(sample_input)

print("\n--- Predicted Vitals ---")
print(f"Heart Rate: {prediction[0][0]:.1f} bpm")
print(f"Systolic BP: {prediction[0][1]:.1f} mmHg")
print(f"Diastolic BP: {prediction[0][2]:.1f} mmHg")
