## 🔌 Detailed Wiring Description

| Component            | ESP32-CAM Pin | Notes                                                |
|----------------------|---------------|------------------------------------------------------|
| MLX90614 Temp Sensor | GPIO 14 (SCL) | Use 4.7kΩ pull-up resistors; powered at 3.3V         |
|                      | GPIO 13 (SDA) |                                                      |
| Buzzer               | GPIO 12       | Active buzzer, can be driven directly                |
| LED (Status)         | GPIO 2        | Series resistor (~220Ω) required                     |
| Button (Reset/Alert) | GPIO 0        | Use pull-down resistor (~10kΩ)                       |
| LCD I2C (Optional)   | GPIO 21 (SCL) | Shares I2C bus; check address conflict               |
|                      | GPIO 22 (SDA) |                                                      |
| MicroSD Card Module  | SPI Pins      | CS: GPIO 5, MOSI: GPIO 23, MISO: GPIO 19, SCK: GPIO 18 |
| Power                | 5V/GND        | Use MT3608 boost if powering from battery/solar     |

🔗 [View Full Circuit Diagram](../hardware/circuit-diagram.png)
