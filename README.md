# healthsphere-x-deeptech
 Africa Deep Tech Challenge submission: HealthSphere X – AI-powered portable diagnostic tool
# HealthSphere X

HealthSphere X is a smart, AI-powered health assistant designed for communities with limited access to advanced healthcare. Built around a compact ESP32-based prototype, it helps **prevent, prescribe, and treat** temperature-related conditions in both offline and connected settings.

## 🌍 Purpose

To democratize healthcare access through a low-cost, portable device that empowers individuals and communities to:
- 🛑 **Predict** health risks through real-time monitoring
- 📋 **Prevent** AI-guided health advice based on vitals
- 💊 **Prescribe** early-stage conditions or escalate to a caregiver/doctor

---

## ⚙️ Features

- 🌡️ **Fever & Hypothermia Detection** (via MLX90614 sensor)
- 📺 **LCD Display Output** for live vitals
- 🚨 **Buzzer + LED Alert** for abnormal readings
- 📡 **Wi-Fi Sync & Web Alerts** via Firebase
- 🤖 **AI-based Prediction of Vitals** (e.g., blood pressure, SPO2)
- 💬 **Therapy Bot + First Aid Recommendations**
- 🧠 **Offline Mode** with embedded AI logic
- 🛡️ **Health Insurance Integration** (for scale)
- 🏥 **First Responder Reward System**

---

## 🧪 Hardware Components

- ESP32-CAM microcontroller
- MLX90614 IR Temperature Sensor
- I2C 20x4 LCD Display
- Buzzer + RGB LED
- Lithium-ion Battery Pack
- Optional: Power Booster / Charging Module
- Prototype case: **Plastic plate or takeaway container**

---

## 🧰 Software/Stack

- Arduino (ESP32 Platform)
- Firebase Realtime Database
- Python (for AI logic simulation)
- HTML/CSS (web monitoring page)
- Figma (UI mockups)
- GitHub (code + documentation)

---

## 🧠 AI Functionality

The system uses AI to estimate:
- SPO2 levels
- Blood Pressure
- Heart Rate

These are inferred from temperature trends and optional patient history to offer **clinically guided suggestions**. All suggestions remain **non-diagnostic** and are intended for preliminary care only.

---

## 🌐 Scalability Features

- 🔌 Vendor APIs (insurance, drugs, telemedicine)
- 🧑‍⚕️ Health worker/first responder incentives
- 💼 Can be deployed in: Homes, Schools, Clinics, Pharmacies

---

## 📦 Folders Overview
## Repository Structure

- hardware/ ← Circuit diagrams, components list
- software/ ← Arduino & AI code
- webapp/ ← Web dashboard & remote alert code
- docs/ ← Technical documentation & planning
- assets/ ← Images, diagrams, and pitch materials


---

## 🎯 ADTC Focus Areas Covered

- ✅ Edge AI (offline medical inference)
- ✅ Resource-Constrained Computing (ESP32)
- ✅ Scalable Social Impact (via vendor/insurance integration)
- ✅ Hardware + Software Prototype
- ✅ Fully documented GitHub repo (code, files, pitch)

---

## 👨‍💻 Team & Credits

- **Project Lead:** Nwaruwe Victor Chukwuebuka
- **Team Members:** Anthony, Precious, Chinecherem
- **Mentor/Lab:** AEDJAC Innovation Lab
- **Country:** Nigeria 🇳🇬

---

## License & Disclaimer

See [`docs/disclaimer.md`](docs/disclaimer.md) for legal notes.
---

