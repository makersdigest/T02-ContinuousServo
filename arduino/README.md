# Maker's Digest
## Arduino Continuous Servo Control

To run this sketch, we need to have the Serial Monitor open in the Arduino IDE. Click `'Tools' -> 'Serial Monitor'` to open
up the Serial Monitor. You will also need to set it to 'No Line Ending' otherwise it resets back to 0 every time you enter
a value. You can set 'No Line Ending' in the left most dropdown box on the bottom of the serial monitor.

To control a continuous servo, we give the `s1.write()` function a value between 0 and 180. But 0 is not stopped. 90 is stopped,
and anything below 90 down to 0 will move the servo in reverse at different speeds, and anything above 90 up to 180 will
move the servo foward at different speeds.

However, the circuit is very sensetive and the values of the resistors we put on there are *very* close, but not perfect. Most
commertial continuous servos have a trim pot that you can change so that the servo is stopped at the value of 90. But since
we did not add a trim pot, we just need to adjust the value of stopped. Play with the values until you find what number
(usually +- 5 from 90) stops the servo. Then play go down from 90 by 10's to see where full speed that direction is. Then go 
up by 10's from 90 to see where full speed in the other direction is. You can use these values in your own projects and sketches.
