# HealthSphere X — Offline-First Predictive Health Monitoring

**HealthSphere X** is a low-power AI-powered diagnostic device designed for rural and underserved areas. It runs on an ESP32 microcontroller, performs illness prediction locally, and logs vital data to an SD card — all without internet access.

## Features
- 💡 Predicts illness severity based on temperature, age, and medical history
- ⚡ Optimized for ESP32 with SD card logging (offline-first)
- 🔐 Privacy-first: No cloud dependency
- 🧠 AI model inference from local storage
- 🧪 Simulation scripts for development/testing
- 🌡️ Threshold logic for dynamic alerts

---

## Project Structure

| File | Description |
|------|-------------|
| `esp32_healthsphere.ino` | Core firmware for ESP32 (reads data, predicts, logs) |
| `predict.py` | AI logic for illness condition prediction |
| `thresholds.py` | Defines risk thresholds used in prediction |
| `simulate.py` | Simulates multiple prediction cases for testing |
| `prediction_log.json` | Auto-generated logs from local predictions |
| `README.md` | Project overview and structure explanation |

---

## Usage

### On ESP32
- Flash `esp32_healthsphere.ino` via Arduino IDE
- Ensure SD card is inserted for data logging
- Input temperature and vitals via connected sensor
- Device will:
  1. Predict illness level
  2. Store result in `prediction_log.json` (SD)
  3. Display recommendation

### On PC (for development)
- Run `simulate.py` to generate test predictions
- Adjust `thresholds.py` to test new logic
- Analyze outputs using `prediction_log.json`

---

## Simulation Example

```bash
python simulate.py

