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
#########################################################
# WRITE DOES NOT SEEM TO WORK - NEED TO FIGURE OUT WHY
# check tha CR og LF are note added by pyserial
ser.write(b"$PUBX,40,GLL,0,0,0,0*5C\n")
ser.write(b"$PUBX,40,GRS,0,0,0,0*5D\n")
ser.write(b"$PUBX,40,GSA,0,0,0,0*5E\n")
ser.write(b"$PUBX,40,GST,0,0,0,0*5D\n")
ser.write(b"$PUBX,40,GSV,0,0,0,0*5E\n")
ser.write(b"$PUBX,40,ZDA,0,0,0,0*5D\n")
ser.write(b"$PUBX,40,RMT,0,0,0,0*5E\n")
ser.write(b"$PUBX,40,VTG,0,0,0,0*5E\n")

while 1:
    received_message = ser.readline() # the message send from esp32 needs to have a \n newline in the end
    time.sleep(1)
    print(received_message)
    if received_message != b'':
        
        print(received_message,"\n")
## MICROPYTHON EXAMPLE CODE SNIPPET
"""
        # Enable relevant and wanted NMEA frames
        uart.write("$PUBX,40,GGA,1,1,1,0*5B\n")     # Make sure the $GPGGA, $GPRMC and $GPZDA are always enabled
        uart.write("$PUBX,40,RMC,1,1,1,0*46\n")
        uart.write("$PUBX,40,ZDA,1,1,1,0*45\n")

        if self.all_nmea == True:
            uart.write("$PUBX,40,GLL,1,1,1,0*5D\n") # Enable the rest of the NMEA frames, 0x0008
            uart.write("$PUBX,40,GRS,1,1,1,0*5C\n") # 0x0010
            uart.write("$PUBX,40,GSA,1,1,1,0*4F\n") # 0x0020
            uart.write("$PUBX,40,GST,1,1,1,0*5A\n") # 0x0040
            uart.write("$PUBX,40,GSV,1,1,1,0*58\n") # 0x0080
            uart.write("$PUBX,40,VTG,1,1,1,0*5F\n") # 0x0100
        else:  
            uart.write("$PUBX,40,GLL,0,0,0,0*5C\n") # Disable all but the $GPGGA, $GPRMC and $GPZDA frames
            uart.write("$PUBX,40,GRS,0,0,0,0*5D\n")
            uart.write("$PUBX,40,GSA,0,0,0,0*4E\n")
            uart.write("$PUBX,40,GST,0,0,0,0*5B\n")
            uart.write("$PUBX,40,GSV,0,0,0,0*59\n")
            uart.write("$PUBX,40,VTG,0,0,0,0*5E\n")     

"""