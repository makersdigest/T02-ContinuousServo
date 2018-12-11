# Maker's Digest
## Raspberry Pi Continuous Servo Example
This example has two functions. One to find the range of your servo, and two to demonstrate setting the speed & direction.

To run a continuous servo we need to find the STOPPED, FORWARD Full and REVERSE Full values. Run Function One to determine
what your ranges are. Once you have determined your ranges, you can STOP the servo by setting the ChangeDutyCycle() method 
to STOPPED.

This servo has a range of +- 2.0. If you ADD 2.0 to 7.31 you will get 9.31, and the servo will move FORWARD at full speed.
if you SUBTRACT 2.0 from 7.31 you will get 5.31 and the servo will move in REVERSE at full speed. You can set ChangeDutyCycle()
to anything between STOPPED and FORWARD or REVERSE values for a slower rotation. Run this program with `sudo python gpio-example.py x.xx`
to test different directions and speeds.

## Function One - Range Finder
To run this function, just run the program with no arguments. `sudo python gpio-example.py` will run it. We are trying
determine three things here:
1. STOPPED value
2. FORWARD Full value
3. REVERSE Full value

It will initially give you a value of 7.31 (which was center for the servo we used in the video). If the servo is moving
at all, change that value up or down by .1 or .01 until it stops. That will be your STOPPED value. This servo has a range
of +- 2.0. Meaning that if we ADD 2.0 to 7.31, it will rotate forward at full speed, and if we SUBTRACT 2.0 from 7.31 it
will rotate backwards at full speed. 2.0 is not a set number, so play with it. You may find that your particular servo 
is +- 2.3 or 1.97. 

## Function Two - Demonstration
This simply accepts a number from the command line as: `sudo gpio-example.py 5.31` and will move the servo for two 
seconds. This is a demonstration of how to set it. 
