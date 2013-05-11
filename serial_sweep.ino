#include <Servo.h>

// serial_sweep
// by dbnr 
// control servo with serial
 
Servo myservo;             // create servo object to control a servo 
int pos = 95;              // variable to store the servo position 
int incomingByte = 0;      //varible to store serial data
const int ledPin = 13;     // onboard led
 
 
void setup() 
{ 
  myservo.attach(9);       // attaches the servo on pin 9 to the servo object
  Serial.begin(9600);      // opens serial port, sets data rate to 9600 bps 
  pinMode(ledPin, OUTPUT); // sets led as output
  myservo.write(pos);      // sets servo to start in center
} 
 
 
void loop() 
{ 
  if (Serial.available() > 0) 
  {                
    // read the incoming byte:
    incomingByte = Serial.read();
    // say what you got:                
    Serial.print("I received: ");
    Serial.println(incomingByte, DEC);
    
    // if the data is not null - flash led
    if (incomingByte != 0)
    {
      flash(1);
    }
    
    //if data = a (ascii 97) & servo posistion is not maxed out
    if (incomingByte == 97 && pos != 185)
    {
      //add 10 to pos
      pos += 10;
      //write new pos
      myservo.write(pos);
    }
    
    // if data = b (ascii 98) and servo posistion is not at minimum
    else if (incomingByte == 98 && pos != 5)
    {
      //subtract 10 from pos
      pos -= 10
      //write new pos
      myservo.write(pos);
    }
  }
  // delay serial read 
  delay(50);
 
} 



// function for flash
void flash(int n)
{
  for (int i = 0; i < n; i++)
  {
    digitalWrite(ledPin, HIGH);
    delay(10);
    digitalWrite(ledPin, LOW);
  }
}

