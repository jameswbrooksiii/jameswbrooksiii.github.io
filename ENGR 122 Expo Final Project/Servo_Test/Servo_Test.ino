int PressurePin = A0;
int force;

void setup()
{
  Serial.begin(9600);
}
void loop()
{
  force = analogRead(PressurePin);
  Serial.println(force);
  
}
