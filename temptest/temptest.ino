//Sketch to print temp/humidity
// Include the DHT library
#include "DHT.h"

// Define PIN vars
#define DHTPIN 2
#define DHTPIN2 4
#define DHTPIN3 6
#define DHTPIN4 8
#define DHTPIN5 10
#define DHTPIN6 12
#define DHTPIN7 3
#define DHTTYPE DHT22

// Initialize dht and dht2 vars
DHT dht1(DHTPIN, DHTTYPE);
DHT dht2(DHTPIN2, DHTTYPE);
DHT dht3(DHTPIN3, DHTTYPE);
DHT dht4(DHTPIN4, DHTTYPE);
DHT dht5(DHTPIN5, DHTTYPE);
DHT dht6(DHTPIN6, DHTTYPE);
DHT dht7(DHTPIN7, DHTTYPE);

void setup() {
  Serial.begin(9600); 
  dht1.begin();
  dht2.begin();
  dht3.begin();
  dht4.begin();
  dht5.begin();
  dht6.begin();
  dht7.begin();
}

void loop() {
  float h1 = dht1.readHumidity();
  float t1 = dht1.readTemperature(); 
  float h2 = dht2.readHumidity();
  float t2 = dht2.readTemperature(); 
  float h3 = dht3.readHumidity();
  float t3 = dht3.readTemperature(); 
  float h4 = dht4.readHumidity();
  float t4 = dht4.readTemperature(); 
  float h5 = dht5.readHumidity();
  float t5 = dht5.readTemperature(); 
  float h6 = dht6.readHumidity();
  float t6 = dht6.readTemperature(); 
  float h7 = dht7.readHumidity();
  float t7 = dht7.readTemperature(); 
 
   // Check if any reads failed and exit early (to try again).
  if (isnan(h1) || isnan(t1) || isnan(h2) || isnan(t2)) {
    Serial.println("Sensor read fail. Retrying....");
  }
  else {
    // Separate sensors with a semicolon, separate temp/humidity with a colon
    Serial.print(cToF(t1));
    Serial.print(":");  
    Serial.print(h1);
    Serial.print(";");
    Serial.print(cToF(t2));
    Serial.print(":");  
    Serial.print(h2);
    Serial.print(";");
    Serial.print(cToF(t3));
    Serial.print(":");  
    Serial.print(h3);
    Serial.print(";");
    Serial.print(cToF(t4));
    Serial.print(":");  
    Serial.print(h4);
    Serial.print(";");
    Serial.print(cToF(t5));
    Serial.print(":");  
    Serial.print(h5);
    Serial.print(";");
    Serial.print(cToF(t6));
    Serial.print(":");  
    Serial.print(h6);
    Serial.print(";");
    Serial.print(cToF(t7));
    Serial.print(":");  
    Serial.print(h7);
    Serial.println();
    delay(60000);
  }
}

float cToF(float x){
  float y;
  y = (x*1.8)+32;
  return y;
}
