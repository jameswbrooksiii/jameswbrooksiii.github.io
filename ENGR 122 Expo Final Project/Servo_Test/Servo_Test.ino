// A simple test script using an isolated circuit only containing the pressure pad
// and servo were communicating with the Arduino correctly and working properly.

// Setup
int PressurePin = A0;
int force;

void setup()
{
  Serial.begin(9600);
}
void loop()
{
  force = analogRead(PressurePin); // Read the pressure being applied to the pressure pad
  Serial.println(force); // Print the pressure applied as a numeric value
                         // This value was used to determine the thresholds of when the 
                         // servo should engage/disengage.
}
