#include <SoftwareSerial.h>
SoftwareSerial LCDScreen(3, 2);
bool DebugSet;
String heaterStatus;
void setup() 
{
  pinMode(13, OUTPUT);
  Serial.begin(4800);
  DebugSet = true;
  
  //LCD Screen Setup
  LCDScreen.begin(9600);  delay(500);
  LCDScreen.write(254); LCDScreen.write(1);
  LCDScreen.write(254); LCDScreen.write(132);
  LCDScreen.write("But why tho");
  LCDScreen.write(254); LCDScreen.write(194);
  LCDScreen.write("UCL");
  LCDScreen.write(254); LCDScreen.write(201);
  LCDScreen.write("SP");
  LCDScreen.write(254); LCDScreen.write(207);
  LCDScreen.write("LCL");
  LCDScreen.write(254); LCDScreen.write(212);
  LCDScreen.write("TEMP=");
  LCDScreen.write(254); LCDScreen.write(222);
  LCDScreen.write("HEATER:");
}

void loop() 
{
  ThermistorMethod();
}

void ThermistorMethod()
{
  int currentTemp = analogRead(0);
  float currentTC = (0.1047*currentTemp) - 28.801;
  
  int setpoint = 25;
  float analogSetpoint = (setpoint + 28.801) / 0.1047;

  float StandardDeviation = 0.587142949;
  
  float UCL = analogSetpoint + (StandardDeviation*3);
  float UCLC = (0.1047*UCL) - 28.801;
  
  float LCL = analogSetpoint - (StandardDeviation*3);
  float LCLC = (0.1047*LCL) - 28.801;
  DetermineHeaterStatus(currentTemp, UCL, LCL);
  LCDUpdate(UCLC, setpoint, LCLC, currentTC);
  
  if(DebugSet == true)
  {
    DebugMethod(currentTemp, currentTC, setpoint, analogSetpoint, UCLC, LCLC);
  }
  
  
}

void LCDUpdate(float UCLC, int setpoint, float LCLC, float currentTC)
{
  LCDScreen.write(254); LCDScreen.write(150);
  LCDScreen.print(UCLC, 1); //Prints The UCL in Celsius to two decimal places
  LCDScreen.write(254); LCDScreen.write(157);
  LCDScreen.print(setpoint); //Prints the setpoint in Celsius
  LCDScreen.write(254); LCDScreen.write(163);
  LCDScreen.print(LCLC, 1); //Prints the LCL in Celsius to two decimal places
  LCDScreen.write(254); LCDScreen.write(217);
  LCDScreen.print(currentTC, 1); //Prints the current temp in Celsius to two decimal places
  LCDScreen.write(254); LCDScreen.write(229);
  LCDScreen.print(heaterStatus);
  delay(2000);
}
void DetermineHeaterStatus(int currentTemp, float UCL, float LCL)
{
  if(currentTemp < LCL)
  {
    heaterStatus = "ON";
    digitalWrite(13, HIGH);
  }
  else if(currentTemp > UCL)
  {
    heaterStatus = "OFF";
    digitalWrite(13, LOW);
  }
  else
  {
    Serial.println("In Deadband Space");
  }
}
void DebugMethod(int currentTemp, float currentTC, int setpoint, float analogSetpoint, float UCLC, float LCLC)
{
  Serial.print("CurrentTemp: "); Serial.print(currentTemp);
  Serial.println();
  Serial.print("CurrentTemp Celsius: "); Serial.print(currentTC);
  Serial.println();
  Serial.print("Setpoint: "); Serial.print(setpoint);
  Serial.println();
  Serial.print("Setpoint(Analog): "); Serial.print(analogSetpoint);
  Serial.println();
  Serial.print("UCL: "); Serial.print(UCLC);
  Serial.println();
  Serial.print("LCL: "); Serial.print(LCLC);
  Serial.println();
  Serial.print("Heater Status: "); Serial.print(heaterStatus);
  Serial.println();
  Serial.println();
  delay(2000);
}

