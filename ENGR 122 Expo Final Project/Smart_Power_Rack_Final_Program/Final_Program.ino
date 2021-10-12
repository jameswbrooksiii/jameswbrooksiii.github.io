#include <Servo.h>

// This program was the final version that was used to receive a signal from a pressure sensor
// and output a signal to two servos to engage two mechanical lock, which would then hold the cables
// and the weight in place.

// All members of the group (myself [James Brooks], Trenton Choate, Robert Strange, and Trevor Sallee)
// contributed to testing and developing this code.


// Setup
int PressurePin = A0;
int force;
boolean brakeState = true; //false should mean not active, true means brake is being used
Servo servo1; // Establishing variables
Servo servo2;
int pos = 0;
int servo1Pin = 8; // Establishing pins to be used by the Arduino
int servo2Pin = 9;
int RelayPin = 7;

void setup()
{
  pinMode(RelayPin, OUTPUT);
  servo1.attach(servo1Pin);
  servo2.attach(servo2Pin);
  Serial.begin(9600);
}

// Main
void loop()
{
  force = analogRead(PressurePin); // detects a signal when the pressure pad is pressed
  Serial.println(force);
  
  if(force < 100 && brakeState == false) // when the pressure pad is released and the brake is not engaged,
                                         // engage the lock to catch the weight
  {
    
    for (pos = 0; pos <= 180; pos += 20) // goes from 0 degrees to 180 degrees
    {
    // in steps of 1 degree
    servo1.write(180);              // tell first servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position  
    //Need to test if these value are correct for each SERVO, or if need to be switched around.
    }
    for (pos = 180; pos >= 0; pos -= 20)  // goes from 180 degrees to 0 degrees
    {
    servo2.write(180);              // tell second servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
    //Need to test if these value are correct for each SERVO, or if need to be switched around.
    }

    brakeState = true;
  }
  
  else if(force >= 100 && brakeState == true) // if the pressure pad is pressed again when the brake is engaged,
                                              // the weight lifter is ready, disengage the lock.
  { 
    for (pos = 0; pos <= 180; pos += 20) // goes from 0 degrees to 180 degrees
    {
    // in steps of 1 degree
    servo1.write(0);              // tell first servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position  
    //Need to test if these value are correct for each SERVO, or if need to be switched around.
    }
    
    for (pos = 180; pos >= 0; pos -= 20)  // goes from 180 degrees to 0 degrees
    {
    servo2.write(0);              // tell second servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
    //Need to test if these value are correct for each SERVO, or if need to be switched around.
    }
    
    brakeState = false;
  }
    else
      //Do nothing, because brake is already in not used state, don't want to potentially mess up servo
  Serial.print(" BrakeState: ");
  Serial.println(brakeState);
}
