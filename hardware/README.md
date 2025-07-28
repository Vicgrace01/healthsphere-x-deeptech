# HealthSphere X Hardware Overview

This folder documents the hardware design, configuration, and powering of the HealthSphere X device — a compact, offline-first illness prediction and emergency response unit built on ESP32-CAM.

---

## 📁 Folder Contents

| File | Description |
|------|-------------|
| `circuit-diagram.png` | Annotated schematic of the HealthSphere X hardware setup. |
| `component-list.md` | Full bill of materials including sensors, boosters, and supporting modules. |
| `esp32cam-setup.md` | Guide to flashing and wiring the ESP32-CAM for deployment. |
| `power-overview.md` | Explanation of power requirements, booster modules, and energy efficiency. |
| `.keep` | Keeps the folder tracked in version control when empty. |

---

## 🔧 Core Hardware Modules

- **ESP32-CAM** — Microcontroller with built-in Wi-Fi and camera support.
- **MLX90614** — Contactless infrared temperature sensor.
- **Buzzer & LED** — For alert notifications.
- **MicroSD Card Slot** — For offline model/data storage and logging.
- **MT3608 Boost Converter** — To stabilize power supply from battery/solar inputs.
- **Optional LCD Screen** — For visual feedback.

---

## 🔌 Wiring Notes

Refer to `esp32cam-setup.md` and `circuit-diagram.png` for:
- Flashing instructions
- GPIO pin mapping
- Sensor connections
- Voltage & current considerations

---

## ⚡ Power Resilience

The HealthSphere X hardware is designed to operate in resource-constrained environments:
- Solar-compatible input
- Low idle power draw
- Supports operation without internet access
- AI prediction and vitals logging handled locally via SD card

---

## 📦 Next Steps

Ensure you've:
- Flashed the firmware (`esp32_healthsphere.ino`)
- Uploaded threshold values to `thresholds.json` on the SD card
- Verified all pins are connected per the schematic

---
> For software and AI-related documentation, see the [`software/`](../software/) folder.
