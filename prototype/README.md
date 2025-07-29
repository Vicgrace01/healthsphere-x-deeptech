# HealthSphere X – Physical Prototype

This folder documents the construction of the **first physical prototype** of the HealthSphere X device, designed for low-cost, offline-first health diagnostics in rural and resource-limited settings.

## 📦 Enclosure Design

The prototype uses a **transparent plastic food container** (rectangular, Made in Australia) as the housing. This was chosen for its:
- Readily available and low-cost nature
- Adequate space to fit ESP32-CAM, sensors, and power modules
- Transparency for easy inspection and LED visibility

## 🔧 Component Layout

| Component        | Placement/Location                   |
|------------------|---------------------------------------|
| LCD Screen       | Mounted on top of the lid            |
| ESP32-CAM        | Placed on inner side, facing outward |
| IR Sensor (MLX90614) | Same side as camera, close proximity |
| Buzzer           | Attached near rear side              |
| LED bulbs        | Positioned at the front side         |
| Push Button      | Side-mounted (near charging port)    |
| TP4056 Charger   | On same side as button, accessible   |

The internal wiring and logic boards are arranged to ensure compactness and maintainability. Components are held in place using glue or mounting tape.

## ⚙️ Prototype Features

- **Hand-assembled, no 3D print** required
- Fully offline AI prediction capability
- Temperature sensor + camera + feedback system
- Rechargeable via USB (TP4056 module)
- Uses MicroSD card for logging and model thresholds

## 📁 Files in this Folder

| File | Description |
|------|-------------|
| `layout-diagram.png` | Visual layout of components inside the container |
| `build-notes.md` | Detailed steps to replicate this prototype |
| `mockup-final.png` | AI-generated visual mockup of the final design |
| `version-notes.md` | Log of design changes and improvements |

## 🧪 Limitations

- Prototype enclosure is not ruggedized or weatherproof
- Manual cutting and component mounting may affect alignment
- No external casing for wires; internal layout may shift without bracing

## 🛠️ Next Iteration Goals

- Better component bracketing or holders
- Option to 3D-print a more durable and compact enclosure
- Improve visibility and orientation of LCD and camera

---

