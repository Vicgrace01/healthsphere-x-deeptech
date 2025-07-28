# HealthSphere X – Component List

This document outlines the complete hardware components used in the HealthSphere X prototype device, with a focus on portability, cost-efficiency, and low-power rural health deployment.

---

## 🔧 Core Electronics

| Component                     | Quantity | Notes / Functionality                                 |
|------------------------------|----------|--------------------------------------------------------|
| ESP32-CAM (AI Thinker)       | 1        | Main controller, Wi-Fi + camera onboard               |
| 20x4 I2C LCD Display         | 1        | Shares I2C bus with sensor (SDA: GPIO14, SCL: GPIO15) |
| MLX90614 IR Temp Sensor      | 1        | Non-contact body temperature measurement              |
| Red LED                      | 1        | Visual warning for fever alert                        |
| Active Buzzer                | 1        | Audio alert when danger thresholds are exceeded       |

---

## ⚡ Power System

| Component                 | Quantity | Notes / Functionality                                |
|---------------------------|----------|-------------------------------------------------------|
| 18650 Li-ion Battery      | 2        | Connected in parallel for higher capacity (3.7V)     |
| TP4056 Charging Module    | 1        | With protection circuit, Micro-USB recharge support  |
| MT3608 Boost Converter    | 1        | Boosts 3.7V to stable 5V output                      |
| Slide ON/OFF Switch       | 1        | Cuts or enables 5V output from booster               |
| Power Indicator LED       | 1        | Shows power delivery to system                       |
| Capacitor (100µF)         | 1        | Smooths voltage fluctuations at ESP32 input          |

---

## 🧰 Miscellaneous

| Component                | Quantity | Purpose                                      |
|--------------------------|----------|----------------------------------------------|
| Resistors (330Ω - 1kΩ)   | ~3       | For limiting current to LED/Buzzer           |
| Jumper Wires (F-F / F-M) | Many     | Circuit connections                          |
| Breadboard or Vero Board | 1        | Prototype assembly                           |
| Enclosure (Plastic Case) | 1        | Portable packaging (e.g., takeaway pack)     |

---

> 💰 Approximate Prototype Cost: **<$15 USD**
