String heaterstatus;
#include <SoftwareSerial.h>
SoftwareSerial mySerial(3,2);


void setup() 
{
  pinMode(11, OUTPUT); //Power for Conductivity Sensor
  pinMode(8, OUTPUT); //power for Heater
  pinMode(2, OUTPUT); //Digital pin for LCD Screen
  pinMode(12, OUTPUT); // Digital Output pin for Saltwater
  pinMode(3, OUTPUT); //Digital Output pin for DI Water

  mySerial.write(254);  mySerial.write(1);    // clear screen & move to top left position
  mySerial.begin(9600); delay(500);
  mySerial.write(254); mySerial.write(134);
  mySerial.write("But, Y?"); //print "team" starting at (0,6):
  mySerial.write(254); mySerial.write(194);
  mySerial.write("LCL"); //print "LCL" starting at (1,2):
  mySerial.write(254); mySerial.write(201);
  mySerial.write("SP"); //print "SP" starting at (1,9):
  mySerial.write(254); mySerial.write(206);
  mySerial.write("UCL"); //print "UCL" starting at (1,14): 
  mySerial.write(254); mySerial.write(212);
  mySerial.write("TEMP="); //prints "TEMP=" starting at (3,0):
  mySerial.write(254); mySerial.write(222);
  mySerial.write("HEATER="); //prints "HEATER=" starting at (3,10):
}

void loop() 
{
  int cSensorReturn = analogRead(0);
  int thermistorReturn = analogRead(5); 
  int setpoint;
  setpoint=25;
  ThermistorProgram(setpoint, thermistorReturn);
}

int ThermistorProgram(int setpoint, int thermistorReturn)
{
  float analogSetpoint = 213*pow(setpoint,0.319);
  float thermistorCelsius = pow((thermistorReturn / 213), 3.135);
  float SDeviation = 0.48936;
  float UCLpoint = setpoint + (3*SDeviation);
  float LCLpoint = setpoint - (3*SDeviation);
  float analogUCL = 213*(pow(UCLpoint,0.319));
  float analogLCL = 213*(pow(LCLpoint,0.319));
  if(thermistorReturn > analogUCL)
  {
    Serial.println("Heater off");
    digitalWrite(8,LOW);
    heaterstatus = "OFF";
  }
  else if(thermistorReturn < analogLCL)
  {
    Serial.println("Heater on");
    digitalWrite(8, HIGH);
    heaterstatus = "ON";
  }
  else
  {
    Serial.println("Within Deadband Space");
  }
  LCDProgram(thermistorReturn, LCLpoint, UCLpoint, setpoint);
}

int SalinityProgram(int cSensorReturn)      //Run program for Salinity Control
{
  
}

void SD_CalcThermistor()        //Obtain the Standard Deviation for Thermistor
{
  int Values[20];
  for(int x = 0; x < 20; x++)
  {
    int value = analogRead(5);
    Values[x] = value;
    Serial.println(value);
    delay(5000);
  }
}
void SD_CalcCSensor()           //Obtain the Standard Deviation for Thermistor
{
  int Values[20];
  for(int x = 0; x < 20; x++)
  {
    digitalWrite(11,HIGH);          // apply 5V to the conductivity sensor
    delay(100);                    // hold the voltage at pin 8 for 0.1s
    int analogS = analogRead(0);     // read voltage on + side of 10kohm resistor
    Values[x] = analogS;
    digitalWrite(11,LOW);           // turn off power to the conductivity sensor
    Serial.println(analogS);       // print the analog input reading (0 to 1023) 
    delay(1000);                   // delay 1 second between measurements
  }
}

void LCDProgram(float thermistorReturn, float LCLpoint, float UCLpoint, int setpoint)
{
  // Slap this baby down in void loop:
  //(0,0) means Row 0, Column 0 on the LCD screen:  
  int thermistorC = pow((thermistorReturn / 213), 3.135);
  mySerial.write(254); mySerial.write(150);
  mySerial.print(LCLpoint,1); //prints the value of the LCL in Celsius starting at (2,2) THIS IS JUST A PLACEHOLDER NAME, BE SURE TO CHANGE THIS TO YOUR PROPER DECLARED CODE:
  mySerial.write(254); mySerial.write(157);
  mySerial.print(setpoint); //prints the value of the setpoint in Celsius starting at (2,9) THIS IS JUST A PLACEHOLDER NAME, BE SURE TO CHANGE THIS TO YOUR PROPER DECLARED CODE:
  mySerial.write(254); mySerial.write(162);
  mySerial.print(UCLpoint,1); //prints the value of the UCL in Celsius starting at (2,14) THIS IS JUST A PLACEHOLDER NAME, BE SURE TO CHANGE THIS TO YOUR PROPER DECLARED CODE:
  mySerial.write(254); mySerial.write(217);
  mySerial.print(thermistorC); //prints the value of the temperature reading in Celsius starting at (3,5) THIS IS JUST A PLACEHOLDER NAME, BE SURE TO CHANGE THIS TO YOUR PROPER DECLARED CODE:
  mySerial.write(254); mySerial.write(229);
  mySerial.print(heaterstatus); //prints the heater status (on or off) starting at (3,17) THIS IS JUST A PLACEHOLDER NAME, BE SURE TO CHANGE THIS TO YOUR PROPER DECLARED CODE:
  delay(1000);
} 

