##
 # Maker's Digest
 # GPIO Python Servo Example
 # 
 # Dont forget to install scipy! See README.md for details
## 
import RPi.GPIO as GPIO     # Import GPIO Module
from time import sleep      # Import Sleep module from time library
from scipy.interpolate import interp1d  # Import interpolation from scipy
import sys, getopt          # For command line argument

pin = 18                    # Set GPIO pin 18 on raspberry pi
dly = .5                    # Set delay to 500ms (half second (.5))

GPIO.setmode(GPIO.BCM)      # Set mode of GPIO
GPIO.setup(pin, GPIO.OUT)   # Set pin to Output

# Servo expects a pulse every 20ms, thats 50 pulses per second
# 1000ms / 20 = 50 (50 Hertz)
servo = GPIO.PWM(pin, 50)     # Set GPIO pin 18 to 50hz PWM.
servo.start(0)              # PWM start. Duty cycle 0.

CENTER = 7.31                # Duty cycle where the servo is not moving.

# To move the servo in one direction or the other, you will need to give 
# the 'servo.ChangeDutyCycle()' method a number in the range
# you found by running this program with no arguments. For this servo the
# center is 7.31, with a range of +- 2.00. So, passing 5.31 is max speed
# in one direction and 9.31 is max speed in the other direction. If you give
# the methods a number BETWEEN them, then the servo will rotate at a slower
# speed in that direction.

# The example
def main(args=None):
    global CENTER

    try:
        if (len(sys.argv) > 1):                         # Check if argument
            speed = float(sys.argv[1])                  # Read arg & convert to float
            servo.ChangeDutyCycle(speed)                # Set Duty Cycle
            sleep(2)                                    # Let servo run for 2 seconds
        else: 
            while True:
                print "Using value: %.2f" % CENTER      # Tell us what CENTER is.
                servo.ChangeDutyCycle(CENTER)           # Change the Duty Cycle

                newVal = raw_input("Enter new value: ") # Read new input from user
                CENTER = float(newVal)                  # Convert to float

    except KeyboardInterrupt:
        servo.stop()
        GPIO.cleanup()
        
if __name__ == "__main__":
    main()


