#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);

#define LED 2
#define Buzzer 3
#define Sensor A1

void setup() {
  Serial.begin(9200);
  lcd.init();
  lcd.backlight();
  pinMode(LED, OUTPUT);
  pinMode(Buzzer, OUTPUT);
}

void loop() {
  int valor = analogRead(Sensor);
  lcd.setCursor(0, 0);
  lcd.print("Valor :");
  lcd.print(valor);
  lcd.print("  ");

  if (valor > 400) {
    digitalWrite(LED, HIGH);
    digitalWrite(Buzzer, HIGH);
    lcd.setCursor(0, 1);
    lcd.print("Gas Detectado!");
  } else {
    digitalWrite(LED, LOW);
    digitalWrite(Buzzer, LOW);
    lcd.setCursor(0, 1);
    lcd.print("             ");
  }
}