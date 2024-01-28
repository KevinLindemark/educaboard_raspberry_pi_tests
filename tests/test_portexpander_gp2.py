import spidev
from time import sleep

# Set up SPI interface
spi = spidev.SpiDev()
spi.open(0, 1)
spi.max_speed_hz = 1000000

# Set up MCP23S08 registers
spi.xfer([0x40, 0x00, 0x00])  # Set IODIR to all outputs
spi.xfer([0x40, 0x09, 0x00])  # Set GPIO to all low

# Toggle LED on GP2

spi.xfer([0x40, 0x09, 0x00])  # Set GP2 low
sleep(1)
spi.xfer([0x40, 0x09, 0x04])  # Set GP2 high
# Close SPI interface
spi.close()

