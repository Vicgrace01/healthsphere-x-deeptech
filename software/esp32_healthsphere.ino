#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <WiFi.h>
#include "ESP_Mail_Client.h"
#include <SD_MMC.h>

// === LCD Config ===
LiquidCrystal_I2C lcd(0x27, 20, 4); // SDA: GPIO14, SCL: GPIO15

// === Buzzer & LED Pins ===
#define BUZZER_PIN 12
#define ALERT_LED_PIN 13

// === Simulated Sensor Input (mocked for now) ===
float bodyTemp = 38.5;  // Simulated fever temp

// === WiFi Credentials ===
const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";

// === Email Config ===
SMTPSession smtp;
const char* smtp_host = "smtp.gmail.com";
const int smtp_port = 465;
const char* email_sender = "your_email@gmail.com";
const char* sender_password = "your_email_password"; // App password recommended
const char* recipient_email = "weirdvicky21@gmail.com";

// === AI Mock Prediction ===
struct Vitals {
  int systolicBP;
  int diastolicBP;
  int spo2;
  int heartRate;
};

// === Function to simulate ML prediction from temperature ===
Vitals predictVitals(float temp) {
  Vitals vitals;
  if (temp >= 39.0) {
    vitals.systolicBP = 150;
    vitals.diastolicBP = 100;
    vitals.spo2 = 91;
    vitals.heartRate = 110;
  } else if (temp >= 37.5) {
    vitals.systolicBP = 135;
    vitals.diastolicBP = 90;
    vitals.spo2 = 95;
    vitals.heartRate = 95;
  } else {
    vitals.systolicBP = 120;
    vitals.diastolicBP = 80;
    vitals.spo2 = 98;
    vitals.heartRate = 75;
  }
  return vitals;
}

// === Save vitals to SD Card ===
void saveToSD(Vitals vitals, float temp) {
  File logFile = SD_MMC.open("/health_log.csv", FILE_APPEND);
  if (logFile) {
    logFile.printf("%.2f,%d/%d,%d,%d\n", temp, vitals.systolicBP, vitals.diastolicBP, vitals.spo2, vitals.heartRate);
    logFile.close();
  } else {
    Serial.println("[SD] Failed to open file for writing");
  }
}

// === Send Email Alert ===
void sendEmailAlert(Vitals vitals, float temp) {
  SMTP_Message message;
  message.sender.name = "HealthSphere X";
  message.sender.email = email_sender;
  message.subject = "Health Alert: Abnormal Vitals Detected";
  message.addRecipient("Doctor", recipient_email);

  String htmlMsg = "<h3>HealthSphere X Alert</h3>";
  htmlMsg += "<p><strong>Temperature:</strong> " + String(temp) + "°C</p>";
  htmlMsg += "<p><strong>Predicted BP:</strong> " + String(vitals.systolicBP) + "/" + String(vitals.diastolicBP) + " mmHg</p>";
  htmlMsg += "<p><strong>SPO2:</strong> " + String(vitals.spo2) + "%</p>";
  htmlMsg += "<p><strong>Heart Rate:</strong> " + String(vitals.heartRate) + " bpm</p>";

  message.html.content = htmlMsg.c_str();
  message.html.transfer_encoding = Content_Transfer_Encoding::enc_qp;

  smtp.connect(smtp_host, smtp_port);
  smtp.login(email_sender, sender_password);
  smtp.sendMail(message);
  smtp.closeSession();
}

// === Setup ===
void setup() {
  Serial.begin(115200);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(ALERT_LED_PIN, OUTPUT);

  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("HealthSphere X");

  // Init SD Card
  if (!SD_MMC.begin()) {
    Serial.println("[SD] Card Mount Failed");
  } else {
    Serial.println("[SD] Card mounted");
  }

  // Connect WiFi
  WiFi.begin(ssid, password);
  lcd.setCursor(0, 1);
  lcd.print("Connecting WiFi...");
  int retries = 0;
  while (WiFi.status() != WL_CONNECTED && retries < 10) {
    delay(500);
    Serial.print(".");
    retries++;
  }
  bool internetAvailable = WiFi.status() == WL_CONNECTED;

  lcd.setCursor(0, 2);
  lcd.print(internetAvailable ? "WiFi Connected" : "Offline Mode");

  // Predict vitals
  Vitals vitals = predictVitals(bodyTemp);

  // Display on LCD
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Temp: " + String(bodyTemp) + "C");
  lcd.setCursor(0, 1);
  lcd.print("BP: " + String(vitals.systolicBP) + "/" + String(vitals.diastolicBP));
  lcd.setCursor(0, 2);
  lcd.print("SPO2: " + String(vitals.spo2) + "%");
  lcd.setCursor(0, 3);
  lcd.print("HR: " + String(vitals.heartRate) + " bpm");

  // Log to SD
  saveToSD(vitals, bodyTemp);

  // Trigger alerts if vitals are abnormal
  if (vitals.spo2 < 93 || vitals.heartRate > 100 || vitals.systolicBP > 140) {
    digitalWrite(BUZZER_PIN, HIGH);
    digitalWrite(ALERT_LED_PIN, HIGH);
    if (internetAvailable) {
      sendEmailAlert(vitals, bodyTemp);
    } else {
      Serial.println("[INFO] Alert saved to SD for offline mode");
    }
    delay(5000);
    digitalWrite(BUZZER_PIN, LOW);
    digitalWrite(ALERT_LED_PIN, LOW);
  }
}

// === Loop ===
void loop() {
  // In future: poll actual sensor values + camera feed
  delay(30000); // Wait before rechecking (simulate interval)
}
