/*
 * Maker's Digest
 * 
 * Servo in continuous mode takes a value from 0 - 180 just like regular servos
 * but now it will reverse direction on either side of 90. 0 will be one way,
 * 180 will be the other. However, since our resistors that we added dont
 * *exactly* center it, we need to figure out what the "stop" value is. 
 * 
 * In this sketch, it will default to 90, then you can enter new values through
 * the serial monitor to find where the servo will stop. That will be your new
 * stop value. 
 */
#include <Servo.h>

Servo s1;           // Instantiate Servo Object

int pin = 14;       // Pin 14 is Analog 0
int center = 90;    // Set to default 90

void setup() {
  pinMode(pin, OUTPUT);   // Set to OUTPUT mode
  s1.attach(pin);         // Attach to servo object
  
  Serial.begin(19200);
  Serial.println("Makers Digest: Ready");
}

void loop() {
  Serial.print("Setting center to: ");  // Let us know current value
  Serial.println(center);               // ^^
  
  s1.write(center);                     // Write to Servo

  if (Serial.available() > 0 ) {        // Check if serial data available
    center = Serial.parseInt();         // Read data & Convert to int

    Serial.print("Received new value: "); // Let us know NEW value
    Serial.println(center);               // ^^
  }
  
  delay(1000);                          // Let servo run for 1 second
}
