void setup() {
  pinMode(7, INPUT);
  Serial.begin(9600);
  tone(8,38000); 
}
 
void loop() {
  int detect=digitalRead(7);
  Serial.println(detect);
}


