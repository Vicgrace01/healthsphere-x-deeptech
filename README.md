# HealthSphere X – AI-powered Portable Diagnostic Tool  
*A submission for the Africa Deep Tech Challenge 2025*

---

## 🌍 Purpose  
HealthSphere X is a smart, AI-powered health assistant designed for communities with limited access to healthcare. Built around a compact ESP32-based prototype, it helps **predict**, **prevent**, and **prescribe** solutions for temperature-related conditions — even in offline environments.

---

## ⚙️ Core Features

- 🌡️ Fever & Hypothermia Detection (via MLX90614 sensor)  
- 📺 LCD Display for live vitals  
- 🚨 Buzzer + LED Alerts for abnormal readings  
- 📡 Wi-Fi Sync & Web Alerts via Firebase  
- 🤖 AI-based Estimation of Vitals (BP, SPO2, HR)  
- 💬 First Aid Bot with Offline Health Advice  
- 🛡️ Optional Insurance & Drug APIs for scale  
- 🧑‍⚕️ First Responder Incentive System  

---

## 🧠 AI Logic Overview

HealthSphere X includes a lightweight AI simulation model that estimates basic vitals from available data:

- **Inputs:** Body temperature (IR), timestamp, and optional metadata  
- **Process:** Regression models trained in Python (scikit-learn)  
- **Outputs:** Estimated SPO2, Blood Pressure, Heart Rate  
- **Mode:** Deployed offline on ESP32 or simulated via `predict.py`  

⚠️ *AI predictions are non-diagnostic and assistive only.*

---

## 🧪 Hardware Summary  
See [hardware/README.md](./hardware/README.md) for detailed diagrams and component lists.

- ESP32-CAM microcontroller  
- MLX90614 IR Temperature Sensor  
- I2C 20x4 LCD Display  
- Buzzer + RGB LED  
- Lithium-ion Battery Pack  
- Optional: Power booster/charge module  
- Prototype casing: Recycled plastic container  

---

## 🧰 Software Stack

- Arduino (ESP32 platform)  
- Firebase Realtime Database  
- Python (for AI simulation)  
- HTML/CSS (web alert dashboard)  
- Figma (UI mockups)  
- GitHub (project repo & documentation)  

---

## 📂 Repository Structure

healthsphere-x-deeptech/
│
├── hardware/ # Circuit diagrams & component list
├── software/ # Arduino code & AI Python scripts
├── web/ # Web dashboard + Firebase integration
├── docs/ # Project documentation & setup guides
├── media/ # Images, mockups, diagrams, assets


---

## 🎯 Africa Deep Tech Focus Areas Covered

- ✅ **Edge AI:** Offline medical inference  
- ✅ **Resource-Constrained Computing:** Runs on ESP32  
- ✅ **Scalable Social Impact:** APIs for insurance + responders  
- ✅ **Hardware + Software Integration**  
- ✅ **Fully Documented GitHub Repository**

---

## 👨‍💻 Team

- **Project Lead:** Nwaruwe Victor Chukwuebuka  
- **Team Members:** Anthony, Clementina
- **Mentor/Lab:** AEDJAC Innovation Lab  
- **Country:** Nigeria 🇳🇬  

---

## 📜 License & Legal Disclaimer

> **⚠️ Health Warning:**  
> This project is a prototype for education and humanitarian aid. It is **not a certified medical device** and should not be used for diagnosis or treatment decisions.

MIT License – see [LICENSE](./LICENSE)  
Legal Notes – see [docs/disclaimer.md](./docs/disclaimer.md)
