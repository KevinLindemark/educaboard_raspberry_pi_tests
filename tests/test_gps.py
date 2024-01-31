import time
import serial

# Remember to disable login shell and enable serial hardware:
"""sudo raspi-config

From the menu select interfacing options > serial
and when you are asked whether you would like the login shell
to be available over serial, select no. You will then be asked whether
you would like the serial hardware to be enabled, select yes."""

ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
counter=0
print(ser.name) # name of the serial port used!
while 1:
    received_message = ser.readline() # the message send from esp32 needs to have a \n newline in the end
    time.sleep(1)
    print(received_message)
    if received_message != b'':
        
        print(received_message,"\n")
