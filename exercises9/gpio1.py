# Controlling an LED (Digital Output) Question: Write a program to turn on an LED connected to
# GPIO pin 17. Solution:

GPIO.setMode(GPIO.BCM)
led_pin = 17

GPIO.setup(led_pin, OUTPUT)
# turn on LED 
GPIO.output(led_pin, GPIO.HIGH)
sleep(5)

