#include "DHT.h"

#define DHTPIN 4        // GPIO where DHT11 is connected
#define DHTTYPE DHT11   // Define sensor type

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  Serial.println("DHT11 Sensor Test");
  dht.begin();
}

void loop() {
  delay(2000); // DHT11 needs 2 seconds delay

  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature(); // Celsius

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.print(" %  |  ");

  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" °C");
}
