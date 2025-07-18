# HealthSphere X – Component List

| Component                     | Quantity | Description / Notes                                      |
|------------------------------|----------|-----------------------------------------------------------|
| ESP32-CAM (AI Thinker)       | 1        | Core controller board                                     |
| 20x4 I2C LCD Display          | 1        | SDA to GPIO14, SCL to GPIO15                              |
| MLX90614 IR Temperature Sensor | 1      | Non-contact sensor, I2C (same bus as LCD)                 |
| Active Buzzer                | 1        | Alert indicator                                           |
| Red LED                      | 1        | Temperature warning indicator                             |
| 18650 Li-ion Battery         | 2        | Connected in parallel (3.7V output)                       |
| TP4056 Charging Module       | 1        | With protection circuit, charges via Micro USB           |
| MT3608 DC Boost Converter    | 1        | Boosts 3.7V to 5V for ESP32-CAM and peripherals           |
| Slide ON/OFF Switch          | 1        | Controls power from booster output                        |
| Power Status LED             | 1        | Shows device is powered                                   |
| Resistors (330Ω - 1kΩ)       | ~3       | For LED + buzzer protection                               |
| Jumper Wires                 | Lots     | Female-female or female-male                              |
| Breadboard or Vero Board     | 1        | For building the prototype                                |
| Plastic Casing               | 1        | Takeaway pack or any compact enclosure                    |
