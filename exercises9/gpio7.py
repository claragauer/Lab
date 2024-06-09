# Toggle an LED with a Button (Digital Input and Output) Question: Write a program to toggle an
# LED connected to GPIO pin 17 when a button connected to GPIO pin 27 is pressed.

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
ledPin = 17
buttonPin = 27

# Typically, you only configure inputs with pull-up-down resistors. Without a pull-up resistor, the state
# of the pin can be undefined when no signal is actively driving it. Output pins are managed by setting HIGH 
# or LOW via the program. Thus, there is no risk of the pin floating because the pin is always driven to a known state
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.HIGH)

GPIO.output(ledPin, GPIO.LOW)
input = GPIO.input(buttonPin)

try: 
    while True: # it always checks if that is the case 
        # low = button is pressed
        if (input == GPIO.LOW): 
            # toggling the state: not GPIO.input(ledPin)), means having the inverse state of at the moment 
            GPIO.output(ledPin, not GPIO.input(ledPin))
            # debounce delay
            sleep(0.2)
        
except KeyboardInterrupt: 
    pass

finally: 
    GPIO.cleanup()
