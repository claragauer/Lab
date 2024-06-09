import RPi.GPIO as GPIO  # Import the GPIO library to control the GPIO pins
import time  # Import the time library for delays and timing

# Define pin numbers
trigPin = 13  # Pin to trigger the ultrasonic pulse (output)
echoPin = 12  # Pin to receive the echo from the ultrasonic sensor (input)
led = 11      # Pin for the red LED (output)
led2 = 10     # Pin for the green LED (output)

# Setup GPIO mode
GPIO.setmode(GPIO.BOARD)  # Set the pin numbering scheme to use physical pin numbers on the GPIO header
GPIO.setup(trigPin, GPIO.OUT)  # Set trigPin as an output pin
GPIO.setup(echoPin, GPIO.IN)   # Set echoPin as an input pin
GPIO.setup(led, GPIO.OUT)      # Set led as an output pin
GPIO.setup(led2, GPIO.OUT)     # Set led2 as an output pin

def measure_distance():
    # Function to measure distance using the HC-SR04 sensor
    # The sensor is triggered by sending a high pulse of at least 10 microseconds to trigPin
    # the pulse tells the sensor to emit an ultrasonic burst
    # when the trigger pin receives the high pulse, the sensor emits ultrasonic sound waves
    # the sensor waits for the sound waves to bounce off an object and return to the sensor 
    # when the sensor detects the returning echo, the echoPin goes high and stays high until the echo pulse ends 
    
    # Send a pulse to trigger the sensor
    GPIO.output(trigPin, GPIO.LOW)  # Ensure the trigger pin is low to start with
    time.sleep(0.000002)  # Wait for 2 microseconds to ensure a clean signal
    GPIO.output(trigPin, GPIO.HIGH)  # Set the trigger pin high
    time.sleep(0.00001)  # Wait for 10 microseconds to send a pulse
    GPIO.output(trigPin, GPIO.LOW)  # Set the trigger pin low again
    
    # Measure the time of the echo
    while GPIO.input(echoPin) == 0:  # Wait until the echo pin goes high
        pulse_start = time.time()  # Record the start time of the pulse
        
    while GPIO.input(echoPin) == 1:  # Wait until the echo pin goes low
        pulse_end = time.time()  # Record the end time of the pulse
        
    pulse_duration = pulse_end - pulse_start  # Calculate the duration of the pulse
    distance = pulse_duration * 17150  # Convert time to distance (in cm)
    
    return distance  # Return the measured distance

try:
    while True:  # Infinite loop to continuously measure distance
        distance = measure_distance()  # Get the distance from the sensor
        if distance < 4:  # If the distance is less than 4 cm
            GPIO.output(led, GPIO.HIGH)  # Turn on the red LED
            GPIO.output(led2, GPIO.LOW)  # Turn off the green LED
        else:  # If the distance is 4 cm or more
            GPIO.output(led, GPIO.LOW)  # Turn off the red LED
            GPIO.output(led2, GPIO.HIGH)  # Turn on the green LED
        
        if distance >= 200 or distance <= 0:  # If the distance is out of range (either too far or invalid)
            print("Out of range")  # Print a message indicating the distance is out of range
        else:
            print(f"{distance:.1f} cm")  # Print the measured distance in cm, formatted to one decimal place
        
        time.sleep(0.5)  # Wait for 500 milliseconds before the next measurement

except KeyboardInterrupt:  # Catch the KeyboardInterrupt exception (e.g., when the user presses Ctrl+C)
    print("Measurement stopped by User")  # Print a message indicating that the measurement was stopped
    GPIO.cleanup()  # Reset the GPIO pins to their default state
