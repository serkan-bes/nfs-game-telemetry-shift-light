const int ledPins[] = {2,3,4,5,6,7,8,9,10,11,12}; // LED pinlerin

void setup() {
  Serial.begin(115200);
  for (int i = 0; i < 11; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
}

void loop() {
  if (Serial.available() > 0) {
    int level = Serial.read(); // Python'dan gelen 0-8 arası değer
    
    for (int i = 0; i<11 ; i++ ){
      if (i < level) {
        digitalWrite(ledPins[i], HIGH);
      } else {
        digitalWrite(ledPins[i], LOW);
      }
    }
  }
}
