int redLED   = 9;
int greenLED = 10;
int blueLED  = 11;
 
void setup() {
  pinMode(redLED, OUTPUT);
  pinMode(greenLED, OUTPUT);
  pinMode(blueLED, OUTPUT);  
}
 
void loop() {
    analogWrite(redLED, 255);
    delay (250);
    analogWrite(redLED, 0);
    delay (1);
    analogWrite(blueLED, 255);
    delay(250);
    analogWrite(blueLED, 0);
    delay(1);
  } 


