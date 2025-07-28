# Software Folder – HealthSphere X

This folder contains all the core software components of the **HealthSphere X** prototype, designed for offline-first rural diagnostics powered by ESP32 and local AI prediction.

## File Overview

| File | Purpose |
|------|---------|
| `esp32_healthsphere.ino` | Embedded Arduino code for ESP32. Collects temperature data and logs predictions to SD card. No internet required. |
| `predict.py` | AI-driven logic for predicting temperature-related health conditions using vitals and medical history. |
| `thresholds.py` | Contains defined thresholds and logic ranges for interpreting temperature and risk levels. Used by `predict.py`. |
| `simulate.py` | Runs simulated cases and generates prediction logs as a CSV file. |
| `simulate.csv` | Output file from simulation — can be used for testing, training, or evaluation. |
| `README.md` | This document. Describes purpose and links between all software files. |
| `.keep` | (Optional) Keeps folder alive in Git if empty during init.

## AI Integration

- The AI model is lightweight and runs **fully offline** on microcontrollers.
- Predictions use hand-crafted rules via `predict.py`, suitable for embedded environments with low compute capacity.
- Thresholds are easily modifiable via `thresholds.py`.

## Simulation

Run `simulate.py` to:
- Validate AI predictions.
- Export results to `simulate.csv`.
- Test AI without hardware.

## Dependencies

Only Python standard libraries are used (no external packages). Compatible with Python 3.6+.

---

