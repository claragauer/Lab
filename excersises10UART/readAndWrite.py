# Writing and reading data interchangeably:

import serial
import time 

ser = serial.Serial('/dev/ttyUSB0', 9600)

try: 
    while True: 
        ser.write(b"Hello world")
        sleep(5)
        data = ser.readline()
        print(data)
except KeyboardInterrupt:
    pass
finally: 
    ser.close()
    
    