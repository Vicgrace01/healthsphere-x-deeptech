# simulate.py

from predict import predict_condition
import csv

# Sample cases for test
test_cases = [
    {"temperature": 36.4, "age": 25, "history": "none"},
    {"temperature": 38.8, "age": 72, "history": "hypertension"},
    {"temperature": 39.2, "age": 8, "history": "asthma"},
    {"temperature": 37.9, "age": 44, "history": "none"},
    {"temperature": 40.0, "age": 60, "history": "diabetes"}
]

# Run predictions
results = []
for case in test_cases:
    result = predict_condition(
        temperature=case["temperature"],
        age=case["age"],
        history=case["history"]
    )
    results.append(result)

# Write to CSV
csv_file = "simulate.csv"
fieldnames = list(results[0].keys())

with open(csv_file, mode='w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in results:
        writer.writerow(row)

print(f"Simulation complete. Results saved to {csv_file}.")

