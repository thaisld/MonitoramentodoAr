#include <LiquidCrystal_I2C.h>  // Biblioteca para controle do display LCD
LiquidCrystal_I2C lcd(0x27, 16, 2);  // Define o endereço I2C e o tamanho do LCD

#define LED 2  // Pino do LED
#define Buzzer 3  // Pino do Buzzer
#define Sensor A1  // Pino do sensor de gás

void setup() {
  Serial.begin(9200);  // Comunicação serial
  lcd.init();  // Inicializa o LCD
  lcd.backlight();  // Ativa a luz de fundo do LCD
  pinMode(LED, OUTPUT);  // Configura o pino do LED como saída
  pinMode(Buzzer, OUTPUT);  // Configura o pino do Buzzer como saída
}

void loop() {
  int valor = analogRead(Sensor);  // Lê o valor do sensor de gás

  lcd.setCursor(0, 0);  // Posiciona o cursor no LCD
  lcd.print("Valor :");
  lcd.print(valor);  // Exibe o valor lido

  if (valor > 400) {  // Verifica se o valor é maior que 400
    digitalWrite(LED, HIGH);  // Aciona o LED
    digitalWrite(Buzzer, HIGH);  // Aciona o Buzzer
    lcd.setCursor(0, 1);  // Move para a segunda linha do LCD
    lcd.print("Gas Detectado!");  // Exibe mensagem de detecção de gás
  } else {
    digitalWrite(LED, LOW);  // Desliga o LED
    digitalWrite(Buzzer, LOW);  // Desliga o Buzzer
    lcd.setCursor(0, 1);  // Move para a segunda linha do LCD
    lcd.print("   ");  // Apaga a mensagem anterior
  }
}
