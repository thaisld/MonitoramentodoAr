#include "DHT.h"
#define DHTPIN 2 

# define DHTTYPE DHT11     

DHT dht(DHTPIN, DHTTYPE);

#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  Serial.begin(9600);
  Serial.println(F("DHTxx teste!"));

  dht.begin();

  lcd.begin();

}

void loop() {
  
  float h = dht.readHumidity();
  
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t)) {
    Serial.println(F("Falha de leitura do sensor DHT!"));
    return;
  }

  float hic = dht.computeHeatIndex(t, h, false);

  Serial.print(F("Umidade: "));
  Serial.print(h);
  Serial.print(F("%  Temperatura: "));
  Serial.print(t);
  Serial.print(F("°C "));

  lcd.setBacklight(HIGH);

  lcd.setCursor(0, 0);
  lcd.print(F("Humidade: "));
  lcd.setCursor(10, 0);
  lcd.print(round(h));
  lcd.setCursor(12, 0);
  lcd.print(F(" %"));
  delay(3000);

  lcd.setCursor(0, 1);
  lcd.print(F("Tempo: "));
  lcd.setCursor(7, 1);
  lcd.print(round(t));
  lcd.setCursor(9, 1);
  lcd.write(32);  
  lcd.write(223); 
  lcd.print(F("C"));
  delay(3000);

}