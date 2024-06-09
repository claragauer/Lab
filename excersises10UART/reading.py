# Reading a fixed number of bytes:

import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)

# Read 10 bytes from the serial port
data = ser.read(10)
print(data)
ser.close()
