from time import sleep
import spidev

# Set up SPI interface
spi = spidev.SpiDev()
spi.open(0, 1)
spi.max_speed_hz = 1000000

# Set up MCP23S08 registers
spi.xfer([0x40, 0x00, 0x00])  # Set IODIR to all outputs
spi.xfer([0x40, 0x09, 0x00])  # Set GPIO to all low

# Toggle LED on GP3

spi.xfer([0x40, 0x09, 0x08])  # Set GP3 high
sleep(1)
spi.xfer([0x40, 0x09, 0x00])  # Set GP3 low

# Close SPI interface
spi.close()

