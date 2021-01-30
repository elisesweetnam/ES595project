#include <stdio.h>

int FSRpin = 36;
int Sensor;
int ThisReading;
int LastReading;
int Movement;
int Movementsq;

int a[6]={0,0,0,0,0,0};

int start_incrementer;
int average = 0;

void setup()
{
  Serial.begin(9600);
//  pinMode(2, INPUT);  // or whichever pin
//  a[6] = {0, 0, 0, 0, 0, 0};
  start_incrementer = 0;
}

void loop()
{
  // analogRead a pin or wherever you want the data to come from
  Sensor = analogRead(FSRpin);
  LastReading = ThisReading;
  ThisReading = Sensor;
  Movement= ThisReading - LastReading;
  Movementsq= sqrt(sq(Movement));
  Serial.println(Movementsq);
  
  // make sure at least 10 values are gathered before starting to compare the array elements
  // this makes sure you avoid reading the initial array of 0s so you don't find an artificial match at the start of the program
  if(start_incrementer < 6)
  {
    // shift oldest to the end of array and newest at the start of the array
    a[5] = a[4];
    a[4] = a[3];
    a[3] = a[2];
    a[2] = a[1];
    a[1] = a[0];
    a[0] = Movementsq;
    
    // add this loop to the counter
    start_incrementer++;
  }
  else
  {
// create an average value of the running array 
      average = (a[0]+a[1]+a[2]+a[3]+a[5])/6;
      if (average >= 2000){
      Serial.println("alert");
      }
      
    // add to the array and keep looking for more matches
    // shift oldest to the end of array and newest at the start of the array
    // the 7th oldest value naturally falls off the end
    a[5] = a[4];
    a[4] = a[3];
    a[3] = a[2];
    a[2] = a[1];
    a[1] = a[0];
    a[0] = Movementsq;
  }
  delay(1000);
}
