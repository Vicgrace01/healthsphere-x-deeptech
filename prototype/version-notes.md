# HealthSphere X – Prototype Version Notes

This file documents the evolution of the HealthSphere X physical prototype, highlighting design changes, feature improvements, and lessons learned across versions.

---

## 📌 Version History

### 🧪 **Version 0.1 – Concept Sketch**
- **Date**: July 2025
- **Format**: Hand-drawn layout and AI-generated mockup
- **Focus**: Component positioning and enclosure feasibility
- **Highlights**:
  - Cylindrical AI model placement
  - Sensor and camera alignment
  - Proposed top-mounted OLED display
- **Issues**:
  - No actual wiring or component integration
  - No real enclosure; purely conceptual

---

### ⚙️ **Version 1.0 – Breadboard Prototype**
- **Date**: July 2025
- **Build Type**: Temporary/test setup on breadboard
- **Materials**: ESP32-CAM, MLX90614, buzzer, LEDs, OLED
- **Highlights**:
  - Successful data logging to MicroSD
  - Predictive logic functional via `predict.py`
  - Manual triggering with push button
- **Issues**:
  - Unstable power from breadboard wiring
  - Camera module easily dislodged
  - No protection or portability

---

### 📦 **Version 1.1 – Enclosed Prototype (Current)**
- **Date**: July 2025
- **Enclosure**: Modified plastic container (no 3D printing)
- **Changes**:
  - All components internally fixed and aligned
  - USB charging exposed via cutout
  - Functional LCD for real-time feedback
- **Improvements**:
  - Power stabilized using TP4056 + 18650
  - Fully offline operation enabled
  - Durable and replicable without specialized tools
- **Limitations**:
  - Lacks dust/water resistance
  - Manual cutting required
  - No dynamic menu interface on LCD (static display only)

---

## ⏭️ Planned Features for V1.2+
| Feature | Goal |
|--------|------|
| Enclosure redesign | More compact and modular layout |
| Battery upgrade | Add solar charge controller or dual-cell support |
| LCD interface | Add menu or multi-screen display |
| User config | Loadable JSON settings file |
| Status indicator | Bi-color LED for device state |

---

## 📁 Related Files

- **Photos**: `media/`
- **Build Guide**: `build-notes.md`
- **Wiring & Power**: `hardware/`

---

## ✅ Status: Stable

Version 1.1 is stable for demonstration, simulation, and future integration testing.
