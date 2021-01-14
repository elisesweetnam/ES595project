int FSRpin = 36;
int Sensor;
int ThisReading;
int LastReading;
int Movement;

void setup() {
Serial.begin(9600);
}

void loop() {
Sensor = analogRead(FSRpin);
LastReading = ThisReading;
ThisReading = Sensor;
Movement= ThisReading - LastReading;
Serial.print("Movement:");
Serial.println(Movement);
delay(100);
}
