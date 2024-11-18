#include "DHT.h"  // Biblioteca para o sensor de temperatura e umidade DHT
#define DHTPIN 2  // Pino de conexão do sensor DHT
#define DHTTYPE DHT11  // Tipo de sensor DHT

DHT dht(DHTPIN, DHTTYPE);  // Criação do objeto para o sensor DHT

#include <Wire.h>  // Biblioteca para comunicação I2C
#include <LiquidCrystal_I2C.h> // Biblioteca para controle do display LCD via I2C

LiquidCrystal_I2C lcd(0x27, 16, 2); // Endereço I2C do LCD e o tamanho

void setup() {
  Serial.begin(9600);  // Comunicação serial
  Serial.println(F("DHTxx teste!"));  // Mensagem inicial no monitor serial

  dht.begin();  // Inicializa o sensor DHT11

  lcd.begin();  // Inicializa o display LCD
}

void loop() {
  float h = dht.readHumidity();  // Lê a umidade
  float t = dht.readTemperature();  // Lê a temperatura

  if (isnan(h) || isnan(t)) {  // Verifica falha de leitura
    Serial.println(F("Falha de leitura do sensor DHT!"));
    return;
  }

  float hic = dht.computeHeatIndex(t, h, false);  // Calcula o índice de calor

  // Exibe os valores no monitor serial
  Serial.print(F("Umidade: "));
  Serial.print(h);
  Serial.print(F("%  Temperatura: "));
  Serial.print(t);
  Serial.print(F("°C "));

  lcd.setBacklight(HIGH);  // Garante que o LCD tenha luz de fundo

  // Exibe umidade no LCD
  lcd.setCursor(0, 0); 
  lcd.print(F("Humidade: "));
  lcd.setCursor(10, 0);
  lcd.print(round(h));
  lcd.setCursor(12, 0);
  lcd.print(F(" %"));
  delay(3000);  // Atraso de 3 segundos

  // Exibe temperatura no LCD
  lcd.setCursor(0, 1);
  lcd.print(F("Tempo: "));
  lcd.setCursor(7, 1);
  lcd.print(round(t));
  lcd.setCursor(9, 1);
  lcd.write(32);  // Escreve espaço
  lcd.write(223);  // Símbolo de grau
  lcd.print(F("C"));
  delay(3000);  // Atraso de 3 segundos
}
