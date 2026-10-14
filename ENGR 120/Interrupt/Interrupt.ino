int redLED   = 9;
int greenLED = 10;
int blueLED  = 11;

volatile int whiskerState = 0; //variable for reading whisker status

void setup(){
  pinMode(2,INPUT);
  pinMode(8,OUTPUT);
  pinMode(redLED, OUTPUT);
  pinMode(greenLED, OUTPUT);
  pinMode(blueLED, OUTPUT);
  Serial.begin(9600);
  attachInterrupt(0, whisker, CHANGE); //interrupt 0 maps to pin 2

}
void loop(){ 
    for (int i=0; i<256; i++) {
    analogWrite(redLED,255-i);
    analogWrite(greenLED,i);
    delay(10);

  }
  for (int i=0; i<256; i++) {
    analogWrite(redLED,i);
    analogWrite(greenLED,255-i);
    delay(10);
  }
}

void whisker(){
  whiskerState=digitalRead(2);
  digitalWrite(8, whiskerState); 
  Serial.println(whiskerState);
}

