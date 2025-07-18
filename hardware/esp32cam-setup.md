# ESP32-CAM Setup Guide

## 1. Tools Required
- Arduino IDE (v1.8 or later)
- USB to Serial Adapter (3.3V logic)
- Jumper wires

## 2. Board Setup
In Arduino IDE:
- Go to `Preferences` and add board URL:  
  `https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json`
- Install the "esp32" board package under `Boards Manager`
- Select:
  - **Board**: "AI Thinker ESP32-CAM"
  - **Port**: Your USB COM port
  - **Upload Speed**: 115200
  - **Partition Scheme**: "Huge App"

## 3. Wiring for Upload
| ESP32-CAM Pin | USB-to-Serial |
|---------------|----------------|
| U0R (RX)      | TX             |
| U0T (TX)      | RX             |
| GND           | GND            |
| 5V            | 5V             |
| IO0 → GND     | (To enter flash mode) |

- Hold `IO0` to GND, press RESET, then upload code.
- Remove `IO0` after flashing is done.

## 4. Power Considerations
ESP32-CAM can draw >250mA during Wi-Fi. Use:
- Stable 5V (from MT3608 booster)
- Capacitor across VCC/GND (e.g., 100µF) to prevent brownout

## 5. Peripheral Pin Mapping
| Function         | Pin      |
|------------------|----------|
| LCD SDA          | GPIO14   |
| LCD SCL          | GPIO15   |
| Buzzer           | GPIO12   |
| Warning LED      | GPIO13   |
| MLX90614 (I2C)   | GPIO14/15 (shared with LCD) |
