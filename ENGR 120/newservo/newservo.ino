#include <Servo.h>
Servo myservo1;

void setup() {
  myservo1.attach(9);
}

void loop() {
  myservo1.writeMicroseconds(600);
  delay(650);
  myservo1.writeMicroseconds(2400);
  delay(490);
}

