#from EmulatorGUI import GPIO
import RPi.GPIO as GPIO
import time
import traceback

# Set up the GPIO numbering mode
GPIO.setmode(GPIO.BCM)

# Set up GPIO14 and GPIO04 as outputs
GPIO.setup(14, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

try:
    while True:
        # Turn GPIO14 and GPIO04 ON
        GPIO.output(14, GPIO.HIGH)
        GPIO.output(4, GPIO.HIGH)
        print("GPIO14 and GPIO04 are ON")
        
        # Wait for 1 second
        time.sleep(1)
        
        # Turn GPIO14 and GPIO04 OFF
        GPIO.output(14, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        print("GPIO14 and GPIO04 are OFF")
        
        # Wait for 1 second
        time.sleep(1)
        
except KeyboardInterrupt:
    # Clean up GPIO settings before exiting
    GPIO.cleanup() # 
    print("Program terminated and GPIO cleaned up")