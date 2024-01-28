import spidev
import time

# Hvis dupont kabel forbindes til gp4 og skiftes mellem gnd og 3v3 vil "knaptrykket registreres, men der sker ikke noget når selve knappen trykkes

# Create a SpiDev object
spi = spidev.SpiDev()

# Open SPI bus 0 for device 0
spi.open(0, 1)
spi.max_speed_hz = 5000
#Set the MCP23S08P IODIR register to input for GP4
spi.xfer2([0x40, 0x00, 0x10])

while True:
    # Read the GPIO register
    resp = spi.xfer2([0x41, 0x09, 0x00])
    print(resp)
    time.sleep(1)
    # Check if the button connected to GP4 is pressed
    print(resp[2] & 0x10)
    if resp[2] & 0x10:
        print("Button pressed!")
    # Wait for a while before the next check
    time.sleep(0.1)

