int FSRpin = 36;
int Sensor;
int ThisReading;
int LastReading;
int Movement;
int Movementsq;

void setup() {
Serial.begin(9600);
}

void loop() {
Sensor = analogRead(FSRpin);
LastReading = ThisReading;
ThisReading = Sensor;
Movement= ThisReading - LastReading;
Movementsq= sqrt(sq(Movement));
Serial.println(Movementsq);
delay(500);
}
