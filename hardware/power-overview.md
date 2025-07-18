# HealthSphere X Power Supply Overview

## Power Components
- **2x 18650 Li-ion Batteries** connected in parallel (3.7V)
- **TP4056 Charging Module** to safely charge via USB
- **MT3608 DC-DC Boost Converter** boosts 3.7V to stable 5V
- **Slide Switch** controls power from booster to the ESP32-CAM and sensors
- **Power LED Indicator** lights up when system is active

## Power Flow

[USB Charger]
↓
[TP4056 Module]
↓
[2x Li-ion Batteries] ———→ [MT3608 Booster] —(5V)→ [Slide Switch] → [ESP32-CAM + Components]

- Always check MT3608 output with multimeter before wiring
- Do **not** exceed 5.2V on ESP32-CAM

## Reference
See: `circuit-diagram.png` for full layout.
