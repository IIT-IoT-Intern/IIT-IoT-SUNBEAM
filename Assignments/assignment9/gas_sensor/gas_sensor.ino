#define MQ2_PIN 35

void setup() {
  Serial.begin(115200);
}

void loop() {
  int gasValue = analogRead(MQ2_PIN);
  Serial.print("Gas Value: ");
  Serial.println(gasValue);

  if (gasValue > 1500) {
    Serial.println("⚠ GAS / SMOKE DETECTED!");
  }
  delay(1000);
}
