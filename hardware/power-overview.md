# HealthSphere X – Power Supply Overview

The HealthSphere X device is designed for rural, off-grid environments. It uses a rechargeable battery system with onboard boosting and USB charging.

---

## 🔋 Power Architecture

| Component         | Function                                                  |
|-------------------|-----------------------------------------------------------|
| 2x 18650 Li-ion   | 3.7V cells connected in parallel for higher capacity      |
| TP4056 Module     | Safe charging via USB (with overcharge protection)        |
| MT3608 Converter  | Boosts 3.7V to stable 5V required by ESP32-CAM            |
| Slide Switch      | Allows user to cut or enable power output manually        |
| Power LED         | Indicates when device is powered                          |
| Capacitor (100µF) | Stabilizes voltage spikes during Wi-Fi/camera usage       |

---

## ⚡ Power Flow Diagram

[USB Power Input]
↓
[TP4056 Charger]
↓
[2x 18650 Batteries in Parallel]
↓
[MT3608 Boost Converter (Set to 5V)]
↓
[Slide Switch] ————→ [ESP32-CAM + Peripherals]
↑
[100µF Capacitor at VCC/GND]


---

## ⚠️ Engineering Notes

- **Adjust booster output** to 5.0V with multimeter before connecting ESP32-CAM.
- Avoid exceeding **5.2V**, as the ESP32-CAM is voltage-sensitive.
- The capacitor prevents **brownout resets** during Wi-Fi or camera operation spikes.
- A heat sink may be added to MT3608 if device runs for long periods.

---

## 🔧 Future Expansion (Optional)

- Add second TP4056 for dual-cell charging if batteries are separated
- Consider battery fuel gauge for status monitoring (e.g., MAX17043)

---

> 📎 Reference: See `circuit-diagram.png` for exact wiring details.
