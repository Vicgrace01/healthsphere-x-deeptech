
# health_advisor_bt.py
# This code simulates a HealthSphereX-like interaction via terminal or Bluetooth
# where the user inputs temperature and symptoms across five different times.

def get_health_advice(temp, symptoms):
    advice = []
    if temp < 35.0:
        advice.append("Temperature too low. Risk of hypothermia. Keep warm and monitor.")
    elif 35.0 <= temp <= 37.5:
        advice.append("Normal temperature. Stay hydrated and maintain routine care.")
    elif 37.5 < temp <= 39.0:
        advice.append("Mild fever detected. Rest, monitor symptoms, and drink fluids.")
    else:
        advice.append("High fever! Consider seeking medical help immediately.")

    # Additional symptom-based advice
    if "cough" in symptoms.lower():
        advice.append("Persistent cough noted. Watch for other respiratory symptoms.")
    if "headache" in symptoms.lower():
        advice.append("Consider rest and hydration. If persistent, consult a provider.")
    if "rash" in symptoms.lower():
        advice.append("Unexplained rash detected. Avoid scratching and monitor changes.")
    if "pain" in symptoms.lower():
        advice.append("Pain noted. Track intensity and location. May require evaluation.")

    return advice

# Simulate 5-time interaction
print("HealthSphereX - Temperature & Symptom Logger")
times = ["Morning", "Afternoon", "Evening", "Night", "Next Day"]

for i in range(5):
    print(f"\nEntry {i+1} - {times[i]}")
    try:
        temp = float(input("Enter body temperature (°C): "))
        symptoms = input("Describe any symptoms (comma separated or freeform): ")
        advice = get_health_advice(temp, symptoms)
        print("Health Advice:")
        for tip in advice:
            print(" -", tip)
    except ValueError:
        print("Invalid input. Please enter a numeric value for temperature.")

print("\nThank you for using HealthSphereX prototype simulation.")
