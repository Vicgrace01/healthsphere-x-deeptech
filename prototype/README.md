# 🧰 HealthSphere X – Physical Prototype

This folder documents the construction of the **first physical prototype** of the HealthSphere X device, designed for low-cost, offline-first health diagnostics in rural and resource-limited settings.

---

## 📦 Enclosure Design

The prototype is built using a **transparent plastic food container** (rectangular, Made in Australia), selected for:

- Availability and affordability
- Adequate space for ESP32-CAM, sensors, and power modules
- Transparency, aiding inspection and LED visibility

Components are mounted using glue, adhesive pads, or tape. No 3D printing was used for this version.

---

## 🔧 Component Layout

| Component              | Placement Description                      |
|------------------------|---------------------------------------------|
| **LCD Screen**         | Mounted on top of the container lid         |
| **ESP32-CAM**          | Inside wall, outward-facing orientation     |
| **MLX90614 IR Sensor** | On same side as camera, near the edge       |
| **Buzzer**             | Rear end of the base                        |
| **LED Bulbs**          | Front-facing for visual feedback            |
| **Push Button**        | Side-mounted (near charging port)           |
| **TP4056 Charger**     | Same side as button, externally accessible  |

Internal wiring is arranged to minimize clutter and reduce interference. Components are spaced to prevent heat buildup or shorting.

---

## ⚙️ Prototype Features

- Fully offline AI-based predictions (via ESP32)
- IR sensor for non-contact temperature measurement
- Visual (LED) and auditory (buzzer) feedback
- Rechargeable via USB (TP4056 module)
- MicroSD card for model thresholds and data logging
- Built without custom PCB or printed enclosure

---

## 📁 Files in This Folder

| File                 | Description |
|----------------------|-------------|
| [`layout-diagram.png`](layout-diagram.png) | Physical layout of internal components |
| [`build-notes.md`](build-notes.md)         | Step-by-step instructions to replicate this prototype |
| [`mockup-final.png`](../mockup-final.png)  | Final mockup design of the intended product |
| [`version-notes.md`](version-notes.md)     | Log of build versions and hardware iterations |

---

## 🧪 Known Limitations

- Enclosure not waterproof or dustproof
- Manual mounting may result in slight component misalignment
- Wiring may shift during transport without bracing or foam padding

---

## 🚀 Next Iteration Goals

- Design a custom 3D-printed enclosure with mount slots
- Improve internal cable management
- Optimize component placement for ergonomics
- Integrate OLED or TFT touchscreen for expanded UX

---
