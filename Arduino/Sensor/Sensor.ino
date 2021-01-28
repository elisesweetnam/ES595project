int FSRpin = 36;
int FSRreading;

void setup() {
Serial.begin(9600);
}

void loop() {
FSRreading = analogRead(FSRpin);
Serial.print("Reading:");
Serial.println(FSRreading);
delay(100);
}
