#include <WiFi.h>

// Wi-Fi credentials
const char* ssid = "iPhone";
const char* password = "55555505";

void setup() {
  Serial.begin(115200);

  // Start Wi-Fi connection
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");

  // Wait until connected
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  // Connected successfully
  Serial.println("\nWiFi Connected!");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  // Nothing required here
}