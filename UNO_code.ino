#include <LiquidCrystal.h>
LiquidCrystal lcd (13, 12, 11, 10, 9, 8);

void setup() {
  lcd.begin(16, 2);
  Serial.begin(9600);
}

void loop() {
  int pirState = digitalRead(2);
  lcd.setCursor(0,0);
  lcd.print("Welcome");
  if(pirState == LOW){
    Serial.write("cam_stop");
    lcd.setCursor(0,1);
    lcd.print("CamOff");
    delay(200);
    lcd.clear();
  }
  else if(pirState == HIGH){
    Serial.write("cam_start");
    lcd.setCursor(0,1);
    lcd.print("CamOn");
    delay(200);
    lcd.clear();
  }

}
