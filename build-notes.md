# HealthSphere X – Prototype Build Notes

This document outlines the step-by-step process used to assemble the first working prototype of the HealthSphere X device. It is intended to help others replicate the build using low-cost, widely available components and no 3D printing.

---

## 🔩 Materials Used

- **Enclosure**: Transparent rectangular food container (plastic, ~15×10×7 cm)
- **Microcontroller**: ESP32-CAM
- **Temperature Sensor**: MLX90614 IR sensor
- **LCD**: 0.96" I2C OLED display
- **Buzzer**: Passive buzzer module
- **LEDs**: 2 × 3mm red and green LED bulbs
- **Button**: Momentary tactile push button
- **Power Module**: TP4056 Lithium battery charging module
- **Battery**: 18650 Li-ion cell or 3.7V LiPo
- **Other**: MicroSD card module, jumper wires, breadboard (optional), mounting tape, glue gun

---

## 🛠️ Assembly Steps

### 1. **Prepare the Enclosure**
- Use a precision knife or rotary tool to cut holes for:
  - The camera lens
  - The IR sensor
  - USB charging port
  - LED indicators
  - Push button
- Clean surfaces and ensure snug fits to prevent component shifting.

### 2. **Mount the Core Components**
- Fix the ESP32-CAM inside the container so that the camera aligns with the lens cutout.
- Place the MLX90614 near the camera for aligned sensing.
- Mount the OLED display on the lid or top surface using glue/tape.
- Attach the buzzer and LED bulbs in their respective positions (rear and front).
- Glue the TP4056 board close to a cutout for USB access.

### 3. **Wiring Connections**
- Solder or connect components to the ESP32-CAM as per the wiring diagram (`circuit-diagram.png` in `hardware/` folder).
- Use the I2C pins for OLED and IR sensor.
- Route LED, buzzer, and button to designated GPIO pins as configured in `esp32_healthsphere.ino`.

### 4. **Power Setup**
- Connect the TP4056 to the 18650 cell and route output to the ESP32 power pins (5V/GND).
- Double-check polarity and current limits.

### 5. **Insert MicroSD Card**
- Load thresholds and prediction code onto the SD card before inserting into the ESP32.
- Format as FAT32.

### 6. **Test the System**
- Power on the device.
- Observe the LCD, LEDs, and buzzer for response.
- Trigger test readings using the button.
- Use serial monitor or SD logs to verify output.

---

## 🔍 Troubleshooting

| Issue | Solution |
|-------|----------|
| No display on OLED | Check I2C address and wiring |
| No response from sensor | Verify voltage compatibility (3.3V for MLX90614) |
| Camera not detected | Reflash ESP32 and check MicroSD formatting |
| Device restarts | Check power stability or faulty battery |

---

## 🧪 Notes & Observations

- A second prototype should include internal bracing or 3D-printed holders for component stability.
- Use female headers for easy swap of sensors or modules.
- Transparent case helps visualize LED status and debug faster.

---

## ✅ Status

- Build completed ✅
- All core features tested (LCD, sensor, buzzer, LED, prediction)
- Ready for community replication or iteration

