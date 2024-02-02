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
print(ser.name) # name of the serial port used!
#########################################################
# DISABLING FOLLOWING NMEA SENTENCES:
ser.write(b"$PUBX,40,GLL,0,0,0,0*5C\n")
ser.write(b"$PUBX,40,GRS,0,0,0,0*5D\n")
ser.write(b"$PUBX,40,GSA,0,0,0,0*4E\n")
ser.write(b"$PUBX,40,GST,0,0,0,0*5B\n")
ser.write(b"$PUBX,40,GSV,0,0,0,0*59\n")
ser.write(b"$PUBX,40,VTG,0,0,0,0*5E\n")

while 1:
    received_message = ser.readline() # the message send from esp32 needs to have a \n newline in the end
    time.sleep(1)
    print(received_message)
    if received_message != b'':
        
        print(received_message,"\n")

