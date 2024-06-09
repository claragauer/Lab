import serial
import time
import RPi.GPIO as GPIO

# Constants
READ_MOTION_STATUS = b'a'
MOTION_DETECTED = b'Y'

# Configure the serial port
ser = serial.Serial(
    port='/dev/serial0', 
    baudrate=9600,
    timeout=1,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE
)

# Configure GPIO
LED_PIN = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)

def check_motion():
    ser.write(READ_MOTION_STATUS)
    # short delay to give the sensor enough time to respond
    time.sleep(0.2)
    if ser.in_waiting > 0:
        # reads one byte 
        module_response = ser.read(1)
        return module_response
    return None

if __name__ == "__main__":
    try:
        while True:
            motion_status = check_motion()
            if motion_status == MOTION_DETECTED:
                GPIO.output(LED_PIN, GPIO.HIGH)
                print("Motion detected!")
            else:
                GPIO.output(LED_PIN, GPIO.LOW)
                print("No motion detected.")
            time.sleep(0.2)  # Pause between checks
    except KeyboardInterrupt:
        ser.close()
        GPIO.cleanup()
        print("Serial port closed and GPIO cleaned up")
