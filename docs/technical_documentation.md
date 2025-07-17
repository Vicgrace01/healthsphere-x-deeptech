# HealthSphere X - Technical Documentation

## 📌 Overview

**HealthSphere X** is an AI-powered vital signs assistant designed to prevent, prescribe, and support treatment for temperature-related illnesses in resource-constrained environments. It combines local sensor analysis (temperature, alerts) with cloud AI predictions (heart rate, BP, SPO2) and remote doctor access.

---

## 🧱 System Architecture

### 1. Device Layer
- **Microcontroller:** ESP32-CAM
- **Sensors:** MLX90614 IR thermometer
- **Output:** I2C LCD Display (20x4), buzzer, LED, optional buttons
- **Power:** USB or battery with TP4056 charger module

### 2. Edge AI & Software
- Offline logic (Arduino C++) for:
  - Temperature classification
  - Triggering alerts
  - Displaying warnings
- Simple rule-based logic + placeholder for AI input

### 3. Cloud & Connectivity
- Firebase for remote data sync
- Optional AI model integration for:
  - Predicting vitals based on temperature + user history
  - Providing alerts or suggestions to caregivers/doctors
- Future webhook or WhatsApp bot for alerts

### 4. Mobile & Web Dashboard
- Displays:
  - Patient profile
  - Live vitals & predicted symptoms
  - Emergency contacts
- Enables:
  - History logging
  - Remote doctor viewing
  - Insurance/first responder integration

---

## 🧰 Hardware Components

| Component                 | Purpose                            | Quantity |
|--------------------------|-------------------------------------|----------|
| ESP32-CAM Module         | Core microcontroller + WiFi         | 1        |
| MLX90614 IR Sensor       | Non-contact body temperature        | 1        |
| 20x4 I2C LCD             | Vital display                       | 1        |
| Buzzer                   | Audio alert                         | 1        |
| LED Bulb (Red/Yellow)    | Visual alert                        | 1–2      |
| TP4056 Module            | Battery charging circuit            | 1        |
| 18650 Li-ion Battery     | Power source (optional)             | 1        |
| USB to Serial Cable      | Programming ESP32-CAM               | 1        |
| Wires, Breadboard        | Connections & testing               | —        |
| Plastic Casing           | Housing/protection                  | 1        |

---

## ⚙️ Software Flow

1. **Power On**
   - LCD displays welcome message
   - Sensor initializes

2. **Temperature Readings**
   - MLX90614 reads user’s forehead
   - Display shows live °C
   - Alerts triggered if temp is abnormal

3. **Local AI Logic**
   - Uses if-else logic (future: YAML-configurable AI)
   - Classifies as: Normal, Mild, High Fever, Dangerous
   - Predicts related vitals if connected to Firebase AI

4. **Cloud Sync (Optional)**
   - Data pushed to Firebase Realtime DB
   - Prediction AI calculates estimated BP, SPO2, HR
   - Web interface updates automatically

5. **Alerts**
   - Red LED/Buzzer if danger
   - Optional message/email alert (e.g. to caregiver)

---

## 🔁 AI Prediction Logic (Phase 2)

| Input         | Model Type       | Output               |
|---------------|------------------|----------------------|
| Temperature   | Regression        | Estimated HR, SPO2   |
| + Symptoms    | Classification    | Risk level           |
| + History     | LLM/GPT Logic     | Suggestion/Advice    |

Stored in:
software/config.yaml

---

## 🖼️ Circuit Diagram

> See [`assets/circuit_diagram.png`](../assets/circuit_diagram.png)  
(Simplified top-down breadboard layout included.)

---

## 🌐 Web Interface

| Page         | Features                              |
|--------------|---------------------------------------|
| Dashboard    | Live vitals, status, AI suggestions   |
| Records      | History of measurements               |
| Alerts       | Emergency triggers and logs           |
| Doctor View  | Patient details + connect button      |

---

## 📦 Folder Structure
HealthSphereX/
│
├── hardware/ ← Circuit diagrams, components list
├── software/ ← Arduino & AI code
├── webapp/ ← Web dashboard & remote alert code
├── docs/ ← Technical documentation & planning
│ ├── disclaimer.md
│ └── technical_documentation.md
├── assets/ ← Images, diagrams, and pitch materials
└── README.md ← Project overview

---

## 🚧 Known Limitations

- **AI still under testing**: Vitals predictions are simulated or estimated.
- **Camera removed temporarily**: Due to damaged ribbon; not affecting core vitals functionality.
- **Limited cloud use offline**: Offline mode relies solely on temperature logic.
- **Prototype casing not optimized**: Made from plastic takeaway plate, not 3D printed yet.

---

## 🛣️ Roadmap

- ✅ Basic prototype completed (offline + Firebase support)
- 🚧 Improve AI prediction accuracy
- 🚧 Add emergency response integration (HerSafe + insurance)
- ⏳ Mobile app companion (for users and caregivers)
- ⏳ Support multi-patient monitoring

---

## 🧠 Future Opportunities

- School health programs
- Elderly monitoring in rural areas
- Remote clinics, pharmacies
- Integration with NHIS/insurance claims
- Crowdsourced alert response via first responder incentives

---

## 📄 License & Disclaimer

See [`docs/disclaimer.md`](docs/disclaimer.md) for more.
