# train-model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
data = pd.read_csv("training-data.csv")

# Features and Labels
features = ["Temperature", "Cough", "Fatigue", "Headache", "PatientHistory"]
X = data[features]
y = data[["PredictedCondition", "Prevention", "Prescription"]]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Save the model
joblib.dump(clf, "healthsphere_model.pkl")

print("✅ Model training complete. Saved as healthsphere_model.pkl")

