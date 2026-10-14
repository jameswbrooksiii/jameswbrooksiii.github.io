int analogSetpoint;
int analogUCL;
int analogLCL;
int analogS;
float salinitySetpoint = .1;                //targetsalinity
unsigned long startmillis;
unsigned long currentmillis;
unsigned long timelapsed = 0;

void setup() {
  Serial.begin(9600);
  pinMode(8, OUTPUT);              //supply to conductivity sensor
  pinMode(11, OUTPUT);             //supply to left solenoid
  pinMode(12, OUTPUT);             //supply to right solenoid
  analogSetpoint = 1277.9*pow(salinitySetpoint, 0.1335);
  analogUCL = analogSetpoinnt+3;
  analogLCL = analogSetpoint-3;
  Serial.print("Salinity Setpoint = "); Serial.print(salinitySetpoint);
  Serial.print("Analog Setpoint = "); Serial.print(analogSetpoint);
  Serial.print("Analog LCL = "); Serial.print(analogLCL);
  Serial.print("Analog UCL = "); Serial.print(analogUCL);
  }

void loop() {
   starmillis = millis();
   timelapsed = startmillis - currentmillis;
   digitalWrite(8,HIGH);          // apply 5V to the conductivity sensor
   delay(100);                    // hold the voltage at pin 8 for 0.1s
   int analogS=analogRead(0);     // read voltage on + side of 10kohm resistor
   digitalWrite(8,LOW);           // turn off power to the conductivity sensor
   Serial.println(analogS);       // print the analog input reading (0 to 1023) 
   delay(1000);                   // delay 1 second between measurements
   Serial.print("Time Signed = "); Serial.print(timelapsed);

   if (analogSetpoint < analogLCL if timelapsed > 1000) add_salt();
   else if (analogSetpoint > analogUCL if timelapsed > 1000) add_DIwater();
}

