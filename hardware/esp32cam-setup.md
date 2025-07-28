# ESP32-CAM Setup Guide

This guide covers how to configure, wire, and power the ESP32-CAM for HealthSphere X, a low-power AI health assistant.

---

## 1. Tools Required

- Arduino IDE (v1.8+ or 2.x)
- USB-to-Serial Adapter (3.3V logic level)
- Jumper wires (male-to-female recommended)
- 100µF capacitor (recommended for power stability)

---

## 2. Arduino IDE Configuration

1. Go to `File` → `Preferences`
2. Add this to **Additional Board Manager URLs**:  

https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json

3. Open `Tools` → `Board Manager`, search for `esp32` and install.
4. Select:
- **Board**: "AI Thinker ESP32-CAM"
- **Port**: Your COM port
- **Upload Speed**: 115200
- **Partition Scheme**: "Huge App (3MB No OTA/1MB SPIFFS)"

---

## 3. Upload Wiring (Flashing)

| ESP32-CAM Pin | USB-to-Serial Pin |
|---------------|-------------------|
| U0R (RX)      | TX                |
| U0T (TX)      | RX                |
| GND           | GND               |
| 5V            | 5V (Stable source)|
| IO0           | GND (during upload only) |

### Upload Process:
1. Hold `IO0` to GND.
2. Press **RESET** once to enter flash mode.
3. Upload your code via Arduino IDE.
4. After upload: disconnect `IO0`, press RESET again to boot.

---

## 4. Power Considerations

- ESP32-CAM can draw up to **250–300mA**, especially when Wi-Fi or camera is active.
- We recommend:
- **MT3608 booster** to deliver a steady 5V from Li-ion battery
- **100µF–470µF capacitor** across VCC and GND to avoid brownouts
- **Use thick power wires** (22 AWG or lower) to reduce drop

> ⚠️ A weak or unstable 5V source is the #1 reason for unexpected resets or boot failures.

---

## 5. Peripheral Pin Mapping (HealthSphere X)

| Peripheral          | ESP32-CAM Pin |
|---------------------|---------------|
| LCD SDA             | GPIO14        |
| LCD SCL             | GPIO15        |
| MLX90614 SDA        | GPIO14 (shared) |
| MLX90614 SCL        | GPIO15 (shared) |
| Buzzer              | GPIO12        |
| RGB Warning LED     | GPIO13        |

> 🧠 **Note**: The LCD and MLX90614 share I²C lines — this is possible since both use I²C protocol. Make sure their addresses are set correctly and don’t conflict.

---

## 6. Testing Output

- Open **Serial Monitor** at `115200` baud.
- You should see:
- Boot messages from ESP32
- Temperature readings from MLX90614
- AI prediction logs (if integrated)

---

## 7. Example Code

- Visit [`/software/`](../software) folder for sample Arduino and AI integration code.
- Or test individual modules (sensor, LCD) before combining logic.

---

## 8. Troubleshooting Tips

| Issue                        | Possible Cause                     |
|-----------------------------|------------------------------------|
| Upload fails                 | IO0 not grounded or wrong COM port |
| ESP32 restarts endlessly     | Weak 5V power / missing capacitor  |
| LCD not displaying           | I2C address conflict or loose wire |
| Camera not working           | Bad power or flash library error   |

---

## 📷 Wiring Diagram

Include a Fritzing or hand-labeled image here once available:

hardware/circuit-diagram.png

---

_This setup is optimized for a low-power, portable deployment environment with offline-first logic and minimal external dependencies._
